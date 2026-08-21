from langchain_text_splitters import RecursiveCharacterTextSplitter


class Splitter:

    def split(self, text):

        splitter = RecursiveCharacterTextSplitter(

            chunk_size=700,

            chunk_overlap=100

        )

        return splitter.create_documents([text])