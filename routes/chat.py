from flask import Blueprint

from flask import request

from flask import jsonify

from services.chat_service import ChatService

chat = Blueprint(

    "chat",

    __name__

)


@chat.route(

    "/api/chat",

    methods=["POST"]

)

def chatbot():

    data = request.get_json()

    question = data["question"]

    service = ChatService()

    response = service.ask(question)

    return jsonify(response)