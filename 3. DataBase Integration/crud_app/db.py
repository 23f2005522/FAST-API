## any thing about db setup and connection


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from pathlib import Path
import os

load_dotenv(Path(__file__).with_name(".env"))

USERNAME = os.getenv("DB_USERNAME")
PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST")
DATABASE = os.getenv("DB_NAME")

if not all((USERNAME, PASSWORD, HOST, DATABASE)):
    raise RuntimeError("DB_USERNAME, DB_PASSWORD, DB_HOST, and DB_NAME must be set in .env")

SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{USERNAME}:{PASSWORD}@{HOST}/{DATABASE}?sslmode=require&channel_binding=require"
)


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()
