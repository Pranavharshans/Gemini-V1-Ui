import textwrap
import streamlit as st
import google.generativeai as genai

# INSERT GEMINI API KEY HERE
genai.configure(api_key='')

def format_text(text):
    return textwrap.fill(text, width=80)

def main():
    st.title("Gemini Text Generation")

    model = genai.GenerativeModel('gemini-pro')

    user_input = st.text_input("Enter a prompt:")
    
    if st.button("Generate"):
        if user_input.upper() == 'END GEMINI':
            st.text("Exiting Gemini...")
        else:
            response = model.generate_content(user_input)
            formatted_text = format_text(response.text)
            st.text(formatted_text)


main()
