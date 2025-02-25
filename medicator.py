import streamlit as st
import openai
import time

# Set your Azure OpenAI credentials
api_key = "B08k2G441vX09NJoA6ZHZQ11ztcIL0K88mJi7Wnr5xmA52TJWjGXJQQJ99ALACYeBjFXJ3w3AAABACOGgRro"
endpoint = "https://opanai777777777.openai.azure.com/"
deployment_name = "gpt-35-turbo-16k"

# Initialize the OpenAI API client
openai.api_type = "azure"
openai.api_key = api_key
openai.api_base = endpoint
openai.api_version = "2023-05-15"

def get_advice(illness):
    prompt = f"You are a medical assistant. Provide advice for the following symptoms: {illness}. Include common over-the-counter medications if applicable."
    response = openai.ChatCompletion.create(
        engine=deployment_name,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response['choices'][0]['message']['content'].strip()

def main():
    st.title("Medical Assistant Chatbot")
    st.code('''
▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄
▐░░▌     ▐░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌
▐░▌▐░▌ ▐░▌▐░▌▐░▌          ▐░▌       ▐░▌    ▐░▌     ▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌▐░▌       ▐░▌
▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌    ▐░▌     ▐░▌          ▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌
▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌    ▐░▌     ▐░▌          ▐░░░░░░░░░░░▌     ▐░▌     ▐░▌       ▐░▌▐░░░░░░░░░░░▌
▐░▌   ▀   ▐░▌▐░█▀▀▀▀▀▀▀▀▀ ▐░▌       ▐░▌    ▐░▌     ▐░▌          ▐░█▀▀▀▀▀▀▀█░▌     ▐░▌     ▐░▌       ▐░▌▐░█▀▀▀▀█░█▀▀
▐░▌       ▐░▌▐░▌          ▐░▌       ▐░▌    ▐░▌     ▐░▌          ▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌▐░▌     ▐░▌
▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄▄▄█░▌▄▄▄▄█░█▄▄▄▄ ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌       ▐░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌▐░▌      ▐░▌
▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌     ▐░▌     ▐░░░░░░░░░░░▌▐░▌       ▐░▌
 ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀       ▀       ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀ 
    ''')
    st.write("Welcome to the Medical Assistant Chatbot!")
    st.write("I am Medicator, an artificial intelligence powered assistant that helps you find the right medicines for your symptoms.")
    st.write("I can provide you with information on the best medicines to take for a variety of ailments.")
    st.write("Go on!")

    illness = st.text_input("Please describe your symptoms:")
    
    if st.button("Get Advice"):
        if illness:
            advice = get_advice(illness)
            st.write(f"Advice: {advice}")
        else:
            st.write("Please enter your symptoms.")

if __name__ == "__main__":
    main()
