from groq import Groq

from config import Config

from services.prompt_service import SYSTEM_PROMPT


class GroqService:

    def __init__(self):

        self.client = Groq(
            api_key=Config.GROQ_API_KEY
        )

    def generate(self, context, question):

        prompt = f"""

Context:

{context}

Question:

{question}

"""

        response = self.client.chat.completions.create(

            model="llama-3.3-70b-versatile",

            messages=[

                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },

                {
                    "role": "user",
                    "content": prompt
                }

            ],

            temperature=0.2,

            max_tokens=800

        )

        return response.choices[0].message.content