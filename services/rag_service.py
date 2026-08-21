from services.embedding_service import EmbeddingService
from services.pinecone_service import PineconeService
from services.groq_service import GroqService


class RAGService:

    def __init__(self):
        self.embedding = EmbeddingService()
        self.vector_db = PineconeService()
        self.llm = GroqService()

    def ask(self, question):

        # Step 1: Embed question
        vector = self.embedding.embed(question)

        # Step 2: Search Pinecone
        result = self.vector_db.search(vector)

        print("Search Result:", result)  # debug

        matches = result.get("matches", [])

        if not matches:
            return {
                "answer": "I couldn't find any relevant information in the knowledge base.",
                "sources": []
            }

        # Step 3: Build context properly
        contexts = []

        for match in matches:

            # Optional: filter low-quality matches
            if match.get("score", 0) < 0.5:
                continue

            metadata = match.get("metadata", {})

            # Case 1: PDF / text data
            if "text" in metadata:
                contexts.append(metadata["text"])

            # Case 2: FAQ JSON
            elif "question" in metadata and "answer" in metadata:
                contexts.append(
                    f"Question: {metadata['question']}\nAnswer: {metadata['answer']}"
                )

        # If still empty
        if not contexts:
            return {
                "answer": "I found some matches, but they were not relevant enough.",
                "sources": []
            }

        # Step 4: Combine context
        context = "\n\n".join(contexts)

        # Step 5: Generate answer
        answer = self.llm.generate(
            context=context,
            question=question
        )

        return {
            "answer": answer,
            "sources": contexts
        }