"""
Creative Hook Agent — Configuration
"""

import os

# --- Reddit API ---
REDDIT_CLIENT_ID = os.getenv("REDDIT_CLIENT_ID")
REDDIT_CLIENT_SECRET = os.getenv("REDDIT_CLIENT_SECRET")
REDDIT_USER_AGENT = "creative-hook-agent/1.0"

# --- Anthropic ---
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
ANTHROPIC_MODEL = "claude-opus-4-6"

# --- Google ---
GOOGLE_CREDENTIALS_PATH = os.getenv("GOOGLE_CREDENTIALS_PATH", "credentials.json")
GOOGLE_DOC_FOLDER_ID = os.getenv("GOOGLE_DOC_FOLDER_ID")  # Optional: save to specific folder

# --- Scraping ---
POST_LIMIT = 50          # Posts per subreddit
COMMENT_LIMIT = 20       # Top comments per post
MIN_UPVOTES = 10         # Filter out low-signal posts

# --- Agent ---
MAX_ITERATIONS = 3
TARGET_SCORE = 10        # All dimensions must hit this
SCORE_DIMENSIONS = [
    "specificity",
    "emotional_pull",
    "audience_relevance",
    "clarity",
    "scroll_stop_power",
]
HOOK_ANGLES = ["problem_pain", "desire_outcome", "curiosity_interrupt", "identity_tribe"]

# --- Defaults ---
DEFAULT_SUBREDDITS = ["r/entrepreneur", "r/marketing", "r/startups"]
DEFAULT_AUDIENCE = "founders and growth marketers"
DEFAULT_PLATFORM = "instagram"
