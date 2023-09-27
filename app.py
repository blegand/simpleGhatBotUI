# Importing required packages
import streamlit as st
import openai
import promptlayer

#configure the Streamlit page by setting the page title and displaying a title and sidebar with some information about the chatbot

st.set_page_config(page_title="Chat with HBCUGPT")
st.title("Chat with HBCUGPT")
st.sidebar.markdown("Developed by Legand Burge](https://profiles.howard.edu/legand-burge", unsafe_allow_html=True)
st.sidebar.markdown("Current Version: 0.0.1")
st.sidebar.markdown("Using GPT-4 API")
st.sidebar.markdown("Not optimised")
st.sidebar.markdown("May run out of OpenAI credits")

OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
promptlayer.api_key = st.secrets["PROMPTLAYER"]

#Define the AI Model

#MODEL = "gpt-3"
#MODEL = "gpt-3.5-turbo"
#MODEL = "gpt-3.5-turbo-0613"
#MODEL = "gpt-3.5-turbo-16k"
#MODEL = "gpt-3.5-turbo-16k-0613"
MODEL = "gpt-4"
#MODEL = "gpt-4-0613"
#MODEL = "gpt-4-32k-0613"

# Swap out your 'import openai'
openai = promptlayer.openai

if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = MODEL

#Define the prompt

if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.messages.append({
            "role": "system",
            "content": f"""
            You are SlimGPT an expert Historically Black College and University (HBCU) cultural historian.
            “historian” means an understanding of the African American experience and culture of HBCUs with well over twenty years historical knowledge.
            You use examples from wikipedia, britanica, uncf, tmcf, and various HBCU websites in your answers, to better illustrate your arguments.
            Your language should be for an 12 year old to understand.
            If you do not know the answer to a question, do not make information up - instead, ask a follow-up question in order to gain more context.
            Use a mix of popular culture and African American vernacular to create an accessible and engaging tone and response.
            Provide your answers in a form of a short paragraph no more than 100 words.
            Start by introducing yourself
            """
        })
    st.session_state.messages.append(   
        {
            "role": "user",
            "content": ""
        })
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": ""
        })

for message in st.session_state.messages:
    if message["role"] in ["user", "assistant"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if prompt := st.chat_input("Ask me anything about HBCUs?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        for response in openai.ChatCompletion.create(
            model=st.session_state["openai_model"],
            messages=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
            stream=True,
            pl_tags=["slimchatbot"],
        ):
            full_response += response.choices[0].delta.get("content", "")
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
