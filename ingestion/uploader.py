import os
import uuid

from ingestion.pdf_loader import PDFLoader
from ingestion.json_loader import JSONLoader
from ingestion.text_splitter import Splitter

from services.embedding_service import EmbeddingService
from services.pinecone_service import PineconeService


class DocumentUploader:

    def __init__(self):
        self.pdf_loader = PDFLoader()
        self.json_loader = JSONLoader()
        self.splitter = Splitter()
        self.embedder = EmbeddingService()
        self.vector_db = PineconeService()

    def upload(self, path):

        extension = os.path.splitext(path)[1].lower()

        # Load file
        if extension == ".pdf":
            text = self.pdf_loader.load(path)

        elif extension == ".json":
            text = self.json_loader.load(path)

        else:
            raise ValueError("Unsupported file type")

        # Split text
        docs = self.splitter.split(text)

        vectors = []

        for doc in docs:
            vector = self.embedder.embed(doc.page_content)

            vectors.append({
                "id": str(uuid.uuid4()),   # prevent overwrite
                "values": vector,
                "metadata": {
                    "text": doc.page_content
                }
            })

        # ✅ DEBUG HERE (correct place)
        print("Uploading vectors:", len(vectors))

        # Upload to Pinecone
        self.vector_db.index.upsert(vectors)

        return len(vectors)