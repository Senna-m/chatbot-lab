import streamlit as st
from google import genai
from google.genai import types

# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================
st.set_page_config(
    page_title="Assistente de Exames Laboratoriais",
    page_icon="🔬",
    layout="centered"
)

# ============================================================
# SYSTEM PROMPT
# ============================================================
SYSTEM_PROMPT = """Você é um assistente especializado em exames laboratoriais clínicos.
Seu papel é ajudar pacientes e profissionais de saúde a entenderem dúvidas sobre exames laboratoriais de forma clara e acessível.

Você pode ajudar com:
- Explicar o que é cada exame e para que serve
- Descrever como se preparar para um exame (jejum, restrições)
- Explicar o que significam os valores de referência
- Esclarecer dúvidas sobre coleta de amostras (sangue, urina, fezes)
- Explicar siglas e termos técnicos de laudos laboratoriais

Regras importantes:
- Sempre use linguagem clara e acessível, evitando jargão desnecessário
- Nunca faça diagnósticos médicos
- Sempre oriente o paciente a consultar um médico para interpretação dos seus resultados pessoais
- Quando citar valores de referência, deixe claro que podem variar entre laboratórios
- Seja empático e paciente nas respostas
"""

# ============================================================
# CLIENTE GEMINI (nova biblioteca)
# ============================================================
@st.cache_resource
def get_client():
    return genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

client = get_client()

# ============================================================
# INTERFACE
# ============================================================
st.title("🔬 Assistente de Exames Laboratoriais")
st.markdown("Tire suas dúvidas sobre exames laboratoriais de forma simples e clara.")
st.caption("⚠️ Este assistente é informativo e não substitui avaliação médica.")

st.divider()

# Inicializar histórico
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibir histórico
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Entrada do usuário
if prompt := st.chat_input("Digite sua dúvida sobre exames laboratoriais..."):

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Consultando..."):

            # Monta histórico no formato da nova biblioteca
            historico = []
            for msg in st.session_state.messages[:-1]:
                role = "model" if msg["role"] == "assistant" else "user"
                historico.append(
                    types.Content(role=role, parts=[types.Part(text=msg["content"])])
                )

            # Adiciona a mensagem atual
            historico.append(
                types.Content(role="user", parts=[types.Part(text=prompt)])
            )

            try:
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=historico,
                    config=types.GenerateContentConfig(
                        system_instruction=SYSTEM_PROMPT,
                        max_output_tokens=1500,
                    )
                )
                resposta = response.text

            except Exception as e:
                if "429" in str(e) or "ResourceExhausted" in str(e):
                    resposta = "⚠️ Limite de requisições atingido. Aguarde alguns minutos e tente novamente."
                else:
                    resposta = f"❌ Erro: {str(e)}"

            st.markdown(resposta)

    st.session_state.messages.append({"role": "assistant", "content": resposta})

# Botão limpar
if st.session_state.messages:
    if st.button("🗑️ Limpar conversa", use_container_width=False):
        st.session_state.messages = []
        st.rerun()