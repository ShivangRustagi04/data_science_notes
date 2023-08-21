import streamlit as st
from deep_translator import GoogleTranslator

def translate_hindi_to_english(hindi_word):
    translator = GoogleTranslator(source='hi', target='en')
    translation = translator.translate(hindi_word)
    return translation

def main():
    st.title("Hindi to English Translator")

    hindi_word = st.text_input("Enter a Hindi word written in English:")
    translated_word = translate_hindi_to_english(hindi_word)

    if hindi_word:
        st.markdown(f"**Translation:** {translated_word}")

if __name__ == "__main__":
    main()
