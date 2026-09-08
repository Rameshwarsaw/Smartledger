import streamlit as st
import google.generativeai as genai

# Page Title
st.set_page_config(page_title="SmartLedger AI")
st.title("SmartLedger - आपका पर्सनल AI असिस्टेंट")

# Initialize Gemini Model
# अपनी API Key यहाँ पेस्ट करें
API_KEY = "अपनी_API_KEY_यहाँ_लिखें"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')

# Initialize Chat History
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("कुछ पूछें..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate Response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        response = model.generate_content(prompt)
        
        message_placeholder.markdown(response.text)
        st.session_state.messages.append({"role": "assistant", "content": response.text})

