import json


class JSONLoader:

    def load(self, path):

        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        texts = []

        for item in data:

            text = f"""
            Question: {item.get("question")}
            Answer: {item.get("answer")}
            """

            texts.append(text)

        return "\n\n".join(texts)