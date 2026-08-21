from pinecone import Pinecone

from config import Config


class PineconeService:

    def __init__(self):

        self.pc = Pinecone(

            api_key=Config.PINECONE_API_KEY

        )

        self.index = self.pc.Index(

            Config.PINECONE_INDEX

        )

    def upload(self, vectors):

        self.index.upsert(

            vectors=vectors

        )

    def search(self, vector):

        return self.index.query(

            vector=vector,

            top_k=5,

            include_metadata=True

        )