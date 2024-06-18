from flask import Blueprint, g, request, Response, jsonify, stream_with_context, session
from app.web.hooks import login_required, load_model
from app.web.db.models import Pdf, Conversation
from app.chat import build_chat, ChatArgs

bp = Blueprint("conversation", __name__, url_prefix="/api/conversations")


@bp.route("/", methods=["GET"])
@login_required
@load_model(Pdf, lambda r: r.args.get("pdf_id"))
def list_conversations(pdf):
    return [c.as_dict() for c in pdf.conversations]


@bp.route("/", methods=["POST"])
@login_required
@load_model(Pdf, lambda r: r.args.get("pdf_id"))
def create_conversation(pdf):
    conversation = Conversation.create(user_id=g.user.id, pdf_id=pdf.id)

    return conversation.as_dict()


@bp.route("/<string:conversation_id>/messages", methods=["POST"])
@login_required
@load_model(Conversation)
def create_message(conversation):
    input = request.json.get("input")
    streaming = request.args.get("stream", False)

    pdf = conversation.pdf

    chat_args = ChatArgs(
        conversation_id=conversation.id,
        pdf_id=pdf.id,
        streaming=streaming,
        metadata={
            "conversation_id": conversation.id,
            "user_id": g.user.id,
            "pdf_id": pdf.id,
        },
    )

    chat = build_chat(chat_args)

    if not chat:
        return "Chat not yet implemented!"

    if streaming:
        return Response(
            stream_with_context(chat.stream(input)), mimetype="text/event-stream"
        )
    else:
        return jsonify({"role": "assistant", "content": chat.run(input)})


@bp.route("/send-prompt", methods=["POST"])
@login_required
def send_prompt():
    data = request.get_json()
    prompt_text = data.get("prompt")
    
    # Guardar el prompt en la sesión
    session["custom_prompt"] = prompt_text
    
    return jsonify({"message": "Prompt received", "prompt": prompt_text})