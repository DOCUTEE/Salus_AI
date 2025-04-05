from flask import Blueprint, request, jsonify
from google import genai
from google.genai import types


chat_bp = Blueprint('chat', __name__)

# Initialize the genai client
client = genai.Client(api_key="AIzaSyCFjH9sPw5IKRMdNjRuxb3p_qYiEoWium8")
chat = client.chats.create(model="gemini-2.0-flash")

@chat_bp.route('/chat', methods=['POST'])
def chat_with_assistant():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({"error": "Message is required"}), 400

    response = chat.send_message(user_message,
                config = types.GenerateContentConfig(
                    system_instruction=
                    """
                        Giả sử bạn là một chuyên gia dinh dưỡng Salus về ăn uống.
                        Những tin nhắn này là của người khao khát muốn sức khỏe tốt hơn.
                        Hãy nhắn tin giúp đỡ họ thật nhiệt tình nhé.
                        Giải thích ngắn gọn Salus là một tiếng latin
                    """
                    ))
    return jsonify({"response": response.text})

