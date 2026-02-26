import os
import google.generativeai as genai

# Configuração da API
genai.configure(api_key=os.getenv("API_KEY"))

SYSTEM_PROMPT = """
Seu nome é Eduardo, um assessor de investimentos sênior, amigável e muito objetivo.
Use óculos, headphone e esteja sempre feliz.

REGRAS DE RESPOSTA:
1. Responda em no máximo 3 frases curtas.
2. Seja direto: explique o conceito e dê um exemplo rápido.
3. Termine SEMPRE sugerindo UMA pergunta para o usuário continuar.
4. Jamais envie avisos legais longos ou listas enormes.
"""

def gerar_resposta(mensagem_usuario, historico):
    try:
        # Testando o modelo de última geração (Preview)
        model = genai.GenerativeModel('models/gemini-3-flash-preview')
# AQUI ESTÁ O SEGREDO: Combinar o Prompt com a mensagem
        prompt_final = f"{SYSTEM_PROMPT}\n\nPergunta do usuário: {mensagem_usuario}"
        
        response = model.generate_content(prompt_final)
        return response.text
    except Exception as e:
        return f"Erro real: {e}"
    


    
