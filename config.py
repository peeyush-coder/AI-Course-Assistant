import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    SECRET_KEY = os.getenv("SECRET_KEY", "course-enquiry-secret")

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

    PINECONE_INDEX = os.getenv("PINECONE_INDEX")

    DATABASE = "database/chatbot.db"

    UPLOAD_FOLDER = "uploads"