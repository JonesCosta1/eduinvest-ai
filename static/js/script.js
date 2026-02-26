// Função para enviar a mensagem
async function sendMessage() {
    const input = document.getElementById('user-input');
    const chatBox = document.getElementById('chat-box');
    const message = input.value.trim();

    // Se o input estiver vazio, não faz nada
    if (!message) return;

    // 1. Adiciona a mensagem do usuário na tela
    appendMessage('user', message);
    input.value = ''; // Limpa o campo

    try {
        // 2. Envia a mensagem para o servidor Flask
        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: message })
        });

        // 3. Verifica se o servidor respondeu com sucesso
        if (!response.ok) {
            throw new Error('Falha na resposta do servidor');
        }

        const data = await response.json();

        // 4. Adiciona a resposta da IA na tela
        if (data.response) {
            appendMessage('bot', data.response);
        } else if (data.error) {
            appendMessage('bot', "Erro: " + data.error);
        }

    } catch (error) {
        console.error("Erro técnico:", error);
        appendMessage('bot', "Erro ao conectar com o servidor. Verifique se o Flask está rodando.");
    }
}

// Função auxiliar para criar os balões de chat
function appendMessage(sender, text) {
    const chatBox = document.getElementById('chat-box');
    const msgDiv = document.createElement('div');
    
    // Define a classe CSS baseada em quem enviou
    msgDiv.className = sender === 'user' ? 'user-msg' : 'bot-msg';
    msgDiv.innerText = text;
    
    chatBox.appendChild(msgDiv);
    
    // Faz o scroll automático para a última mensagem
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Função para as sugestões de cliques rápidos
function setQuery(text) {
    const input = document.getElementById('user-input');
    input.value = text;
    input.focus();
}

// Permite enviar a mensagem apertando "Enter"
document.getElementById('user-input')?.addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});

