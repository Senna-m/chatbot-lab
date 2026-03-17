# 🔬 Chatbot de Exames Laboratoriais

Assistente inteligente desenvolvido para auxiliar pacientes e profissionais de saúde na compreensão de exames laboratoriais, utilizando LLM (Gemini) e interface interativa com Streamlit.

<img width="1073" height="896" alt="image" src="https://github.com/user-attachments/assets/5a43d0da-5cdb-4fbd-a90e-c48225f27096" />

---

## 🎯 Problema

A interpretação de exames laboratoriais pode ser complexa para pacientes e até para profissionais em alguns contextos.  
Muitas dúvidas surgem sobre preparo, significado de resultados e termos técnicos, exigindo tempo e conhecimento especializado.

---

## 💡 Solução

Desenvolvi um chatbot inteligente capaz de:

- Explicar exames laboratoriais de forma simples
- Orientar sobre preparo (jejum, coleta, etc.)
- Interpretar conceitos de laudos (sem realizar diagnóstico)
- Responder dúvidas com linguagem acessível

O sistema utiliza um **LLM com instruções controladas (prompt engineering)** para garantir respostas seguras, educativas e alinhadas com boas práticas de saúde.

---

## 🧠 Tecnologias Utilizadas

| Camada        | Tecnologia |
|---------------|------------|
| Linguagem     | Python 3 |
| Interface     | Streamlit |
| IA / LLM      | Google Gemini API |
| Controle de contexto | Histórico de mensagens |
| Configuração  | Streamlit Secrets |

---

## ⚙️ Como Funciona

Usuário faz uma pergunta  
↓  
Mensagem é enviada para o backend  
↓  
Sistema monta histórico da conversa  
↓  
LLM (Gemini) gera resposta baseada em instruções  
↓  
Resposta é exibida na interface

---

## 🧩 Arquitetura
[Usuário]
↓
[Interface Streamlit]
↓
[Backend Python]
↓
[LLM Gemini API]
↓
[Resposta gerada]
↓
[Exibição no chat]

---

## 🔐 Segurança e Boas Práticas

- O chatbot **não realiza diagnósticos médicos**
- Sempre orienta a consulta com um profissional de saúde
- Utiliza **system prompt estruturado** para evitar respostas inadequadas
- Tratamento de erros de API (ex: rate limit)

---

## 🚀 Funcionalidades

✅ Interface de chat interativa  
✅ Histórico de conversa (contexto mantido)  
✅ Prompt controlado para respostas seguras  
✅ Tratamento de erros da API (429, etc.)  
✅ Mensagens organizadas por usuário e assistente  
✅ Botão para limpar conversa  

---

## ▶️ Como rodar localmente

```bash
# 1. Clone o repositório
git clone https://github.com/Senna-m/chatbot-lab.git
cd chatbot-lab

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Configure a API Key no .streamlit/secrets.toml
GEMINI_API_KEY = "sua_chave_aqui"

# 4. Rode a aplicação
streamlit run app.py

