from flask import Flask, render_template, request, jsonify, session
from ai.ai_logic import gerar_resposta
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "dev_key_123")

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message")
    
    if not user_message:
        return jsonify({"error": "Mensagem vazia"}), 400

    # Pega o histórico da sessão ou cria um vazio
    chat_history = session.get('chat_history', [])
    
    # Chama a função da IA
    response_text = gerar_resposta(user_message, chat_history)
    
    # Atualiza o histórico (opcional)
    chat_history.append({"role": "user", "content": user_message})
    chat_history.append({"role": "assistant", "content": response_text})
    session['chat_history'] = chat_history

    return jsonify({"response": response_text})

if __name__ == '__main__':
    app.run(debug=os.getenv("FLASK_DEBUG"), port=os.getenv("PORT"))

