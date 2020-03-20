# Source: https://pypi.org/project/python-dotenv/
# settings.py
from dotenv import load_dotenv
#load_dotenv()

# OR, the same with increased verbosity
load_dotenv(verbose=True)

# OR, explicitly providing path to '.env'
#from pathlib import Path  # python3 only
#env_path = Path('.') / '.env'
#load_dotenv(dotenv_path=env_path)

# here is how to consume now the variables from the .env file
import os
SECRET_KEY = os.getenv("EMAIL")
print(f'SECRET_EMAIL: {SECRET_KEY}')

DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
print(f'DATABASE_PASSWORD: {DATABASE_PASSWORD}')