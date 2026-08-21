from pypdf import PdfReader


class PDFLoader:

    def load(self, pdf_path):

        reader = PdfReader(pdf_path)

        text = ""

        for page in reader.pages:

            content = page.extract_text()

            if content:

                text += content + "\n"

        return text