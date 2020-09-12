import os
from pathlib import Path

from feedback_bot.command_replies import Replies

TG_TOKEN = os.environ["1182899779:AAEYSt4wW2cfCEHDxZtMn-8LJr-sGQ520ic"]
PROXY = os.environ.get("RT_HTTPS_PROXY")
CHAT_ID = int(os.environ["@artemio_official"])
REPLIES: Replies = Replies.load_from_dir(Path(os.environ["COMMAND_REPLIES_PATH"]))
BOT_TIMEOUT = int(os.environ.get("BOT_TIMEOUT", 10))
BOT_RETRIES = int(os.environ.get("BOT_RETRIES", 5))
