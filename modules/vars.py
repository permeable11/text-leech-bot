import os

API_ID    = os.environ.get("API_ID", "21763365")
API_HASH  = os.environ.get("API_HASH", "5ff490c712f9a9f139a115b16f83f497")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
