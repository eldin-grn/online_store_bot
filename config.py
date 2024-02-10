from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('TOKEN')
SQLALCHEMY_URL = 'sqlite+aiosqlite:///db.sqlite3'
