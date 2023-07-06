import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ['TOKEN']
ADMINS = os.environ['ADMINS']

I18N_DOMAIN = 'bot'
LOCALES_DIR = Path(__file__).parent
