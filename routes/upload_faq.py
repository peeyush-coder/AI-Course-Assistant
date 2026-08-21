from flask import Blueprint, request, render_template
from ingestion.uploader import DocumentUploader
import os

upload_faq = Blueprint("upload_faq", __name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@upload_faq.route("/upload-faq", methods=["GET", "POST"])
def upload_faq_file():

    if request.method == "POST":

        file = request.files["file"]

        if not file:
            return "No file"

        path = os.path.join(UPLOAD_FOLDER, file.filename)

        file.save(path)

        uploader = DocumentUploader()

        chunks = uploader.upload(path)

        return f"{chunks} chunks uploaded successfully."

    return render_template("upload_faq.html")