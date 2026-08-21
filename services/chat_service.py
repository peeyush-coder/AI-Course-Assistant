from services.rag_service import RAGService

from database.database import save_chat


class ChatService:

    def __init__(self):

        self.rag = RAGService()

    def ask(self, question):

        result = self.rag.ask(question)

        save_chat(

            question,

            result["answer"]

        )

        return result