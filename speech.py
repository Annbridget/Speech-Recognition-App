import speech_recognition as sr
import streamlit as st

# Define the function to transcribe speech
def transcribe_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Say something...")
        audio = recognizer.listen(source)
        st.info("Transcribing...")
        try:
            # Using Google Web Speech API
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, I could not understand the audio."
        except sr.RequestError:
            return "Could not request results from Google Speech Recognition service."

# Main Streamlit app
def main():
    st.title("Speech Recognition App")
    st.write("Click the button below and start speaking:")

    if st.button("Start Recording"):
        text = transcribe_speech()
        st.write("Transcription: ", text)

if __name__ == "__main__":
    main()
