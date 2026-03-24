"""
Creative Hook Agent
Part of the Performance Marketing Agents project.

Entry point: runs the full pipeline from Reddit research to Google Doc output.

Usage:
    python main.py --subreddits r/entrepreneur r/marketing --product "your product"
"""

import argparse
import logging
from agent.reddit_scraper import RedditScraper
from agent.hook_generator import HookGenerator
from agent.iteration_engine import IterationEngine
from agent.scorer import Scorer
from agent.doc_builder import DocBuilder
import config

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)


def parse_args():
    parser = argparse.ArgumentParser(description="Creative Hook Agent")
    parser.add_argument(
        "--subreddits",
        nargs="+",
        default=config.DEFAULT_SUBREDDITS,
        help="Subreddits to scan (e.g. r/entrepreneur r/marketing)",
    )
    parser.add_argument(
        "--product",
        type=str,
        required=True,
        help="Product or service to generate hooks for",
    )
    parser.add_argument(
        "--audience",
        type=str,
        default=config.DEFAULT_AUDIENCE,
        help="Target audience description",
    )
    parser.add_argument(
        "--platform",
        type=str,
        default=config.DEFAULT_PLATFORM,
        choices=["instagram", "tiktok", "youtube", "facebook", "linkedin"],
        help="Ad platform (affects hook length and tone)",
    )
    parser.add_argument(
        "--post-limit",
        type=int,
        default=config.POST_LIMIT,
        help="Number of posts to scrape per subreddit",
    )
    return parser.parse_args()


def run(args):
    logger.info("Starting Creative Hook Agent")
    logger.info(f"Product: {args.product}")
    logger.info(f"Subreddits: {args.subreddits}")
    logger.info(f"Platform: {args.platform}")

    # Step 1: Reddit Research
    logger.info("Step 1/5 — Scraping Reddit...")
    scraper = RedditScraper(subreddits=args.subreddits, post_limit=args.post_limit)
    reddit_data = scraper.scrape()
    research = scraper.synthesise(reddit_data, product=args.product)
    logger.info(f"  Scraped {reddit_data['post_count']} posts, {reddit_data['comment_count']} comments")

    # Step 2: Generate Initial Hooks
    logger.info("Step 2/5 — Generating initial hooks...")
    generator = HookGenerator(product=args.product, audience=args.audience, platform=args.platform)
    initial_hooks = generator.generate(research_summary=research["summary"])
    logger.info(f"  Generated {len(initial_hooks)} hooks")

    # Step 3: Iterative Refinement (3 rounds)
    logger.info("Step 3/5 — Running 3 iteration cycles...")
    engine = IterationEngine(
        product=args.product,
        platform=args.platform,
        max_iterations=config.MAX_ITERATIONS,
        target_score=config.TARGET_SCORE,
    )
    iterations = engine.run(hooks=initial_hooks)
    logger.info(f"  Completed {len(iterations)} iterations")

    # Step 4: Final Scoring + CTAs
    logger.info("Step 4/5 — Final scoring and CTA generation...")
    scorer = Scorer(platform=args.platform)
    final_output = scorer.score_and_generate_ctas(hooks=iterations[-1]["hooks"])

    if not final_output["all_passed"]:
        logger.warning("  Some hooks did not reach 10/10 — running emergency rewrite...")
        final_output = engine.emergency_rewrite(final_output)

    logger.info("  All hooks confirmed at 10/10 ✓")

    # Step 5: Build Google Doc
    logger.info("Step 5/5 — Building Google Doc...")
    builder = DocBuilder()
    doc_url = builder.build(
        product=args.product,
        subreddits=args.subreddits,
        reddit_data=reddit_data,
        research=research,
        initial_hooks=initial_hooks,
        iterations=iterations,
        final_output=final_output,
    )

    logger.info(f"\n✓ Done. Google Doc created: {doc_url}")
    return doc_url


if __name__ == "__main__":
    args = parse_args()
    run(args)
