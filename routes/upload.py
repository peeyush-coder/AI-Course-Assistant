from flask import Blueprint

from flask import render_template

from flask import request

import os

from ingestion.uploader import DocumentUploader

upload = Blueprint(

    "upload",

    __name__

)


@upload.route(

    "/upload",

    methods=["GET", "POST"]

)

def upload_pdf():

    if request.method == "POST":

        file = request.files["pdf"]

        path = os.path.join(

            "uploads",

            file.filename

        )

        file.save(path)

        uploader = DocumentUploader()

        chunks = uploader.upload(path)

        return f"{chunks} chunks uploaded."

    return render_template(

        "upload.html"

    )
