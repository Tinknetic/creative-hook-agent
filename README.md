# Creative Hook Agent

> Part of the [Performance Marketing Agents](https://github.com/Tinknetic) project.

An AI agent that mines Reddit for what real people are saying, then stress-tests hooks through 3 iterative rewrites until every dimension scores 10/10. Output is a structured Google Doc — research, working drafts, and final copy — ready to pull straight into production.

---

## What It Does

1. **Reddit Research** — Scans target subreddits for the most upvoted, most commented, and most repeated topics. Surfaces the exact language, pain points, desires, and objections your audience uses.

2. **Hook Generation** — Produces 4 distinct hook angles based on the research (problem, desire, curiosity, identity).

3. **Iterative Refinement** — Runs 3 full rewrite cycles. Before each rewrite, the agent diagnoses what's weak, vague, or generic — then rewrites based on that diagnosis. Nothing moves forward unless it earns it.

4. **Scoring** — Every hook is scored across 5 dimensions. All must hit 10/10 before the final output is produced:
   - Specificity
   - Emotional pull
   - Relevance to audience
   - Clarity
   - Scroll-stopping power

5. **Output: Google Doc (3 tabs)**
   - **Research** — Raw Reddit data, top themes, verbatim quotes, patterns
   - **Working Script** — Every iteration, full diagnosis, and rewrite side-by-side
   - **Final Script** — Clean, copy-paste ready. 4 hook options + 2 CTA options

---

## Stack

- **Language:** Python 3.11+
- **Reddit:** PRAW (Reddit API)
- **LLM:** Claude (Anthropic API)
- **Output:** Google Docs API

---

## Folder Structure

```
creative-hook-agent/
├── agent/
│   ├── reddit_scraper.py       # Pulls posts + comments from target subreddits
│   ├── hook_generator.py       # Generates initial 4 hooks from research
│   ├── iteration_engine.py     # Runs 3 diagnosis → rewrite cycles
│   ├── scorer.py               # Scores hooks across 5 dimensions
│   └── doc_builder.py          # Builds and formats the Google Doc output
├── prompts/
│   ├── research_synthesis.md   # Prompt: synthesise Reddit data into themes
│   ├── hook_generation.md      # Prompt: generate 4 hook angles
│   ├── diagnosis.md            # Prompt: diagnose hook weaknesses
│   ├── rewrite.md              # Prompt: rewrite based on diagnosis
│   └── scoring.md              # Prompt: score across 5 dimensions
├── output_templates/
│   └── google_doc_template.md  # Template structure for the 3-tab output doc
├── examples/
│   └── sample_output.md        # Example run: research → working script → final
├── config.py                   # Subreddit targets, scoring thresholds, API config
├── main.py                     # Entry point — run the full agent pipeline
├── requirements.txt
└── README.md
```

---

## Quickstart

```bash
# 1. Clone and install
git clone https://github.com/Tinknetic/creative-hook-agent.git
cd creative-hook-agent
pip install -r requirements.txt

# 2. Set environment variables
export ANTHROPIC_API_KEY=your_key
export REDDIT_CLIENT_ID=your_id
export REDDIT_CLIENT_SECRET=your_secret
export GOOGLE_CREDENTIALS_PATH=path/to/credentials.json

# 3. Run
python main.py --subreddits r/entrepreneur r/marketing --product "your product"
```

---

## Example Output

See [`examples/sample_output.md`](examples/sample_output.md) for a full end-to-end run showing research themes, all 3 iterations with diagnoses, and the final 4 hooks + 2 CTAs.

---

## Part of Performance Marketing Agents

This agent is one module in a broader system for automating performance marketing creative:

| Agent | What It Does |
|---|---|
| **Creative Hook Agent** ← you are here | Reddit research → hooks → iterative refinement |
| Creative Library | Stores winning patterns for reuse |
| Experiment Tracker | Scores and logs what performs |

---

## License

MIT
