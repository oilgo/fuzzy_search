from dotenv import load_dotenv
import os


load_dotenv()

HOST = os.getenv('HOST')
PORT = int(os.getenv('PORT'))

DATABASE_URL = f"postgresql://{os.getenv('DATABASES_USER')}:{os.getenv('DATABASES_PASSWORD')}@{os.getenv('DATABASES_HOST')}:{os.getenv('DATABASES_PORT')}/{os.getenv('DATABASES_NAME')}?application_name={os.getenv('APPLICATION_NAME')}"