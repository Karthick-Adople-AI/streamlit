import streamlit as st
import googletrans

class TranslatorApp:

    def __init__(self):

        """
        Initializes the TranslatorApp class.
        """

        # Create an instance of the Google Translate Translator
        self.translator = googletrans.Translator()

    def _getting_key(self, val):
        """
        Returns the language code for the given language name.

        Args:
            val (str): The language name.

        Returns:
            str: The language code corresponding to the language name.
        """

        # Iterate over the language items and compare the input value with the language names
        for key, value in googletrans.LANGUAGES.items():
            if val == value:
                return key

        # If the language name is not found, return a message indicating that the key doesn't exist
        return "key doesn't exist"

    def streamlit_interface(self):

        """
        Runs the Streamlit interface for translation.
        """

        st.markdown("Translator", unsafe_allow_html=True)
        # Set the background color to blue
        st.markdown('', unsafe_allow_html=True)

        # Create a selectbox for language selection
        option = st.selectbox('Select Language', tuple(googletrans.LANGUAGES.values()))

        # Create a text area for inputting the text
        text = st.text_area('Input the text')

        # Translate the text based on the selected language
        translated = self.translator.translate(text, dest=self._getting_key(option))

        # Display the translated text
        st.write(translated.text)


if __name__ == '__main__':
    # Create an instance of TranslatorApp
    app = TranslatorApp()

    # Run the Streamlit interface
    app.streamlit_interface()