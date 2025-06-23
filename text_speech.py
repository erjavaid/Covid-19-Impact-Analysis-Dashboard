import streamlit as st
from gtts import gTTS
def text_speech(text,accent="en",c=0):
    tts=gTTS(text=text,lang=accent)
    tts.save(f"output{c}.mp3")
    return f"output{c}.mp3"




st.title("Text-to-speech conversion")
st.markdown("convert into audio")

text_input=st.text_area("enter your text","hello this is text to speech")
accent=st.selectbox("Select your Accent",["hi","fr","en","de"])

c=0
if st.button("Convert your text"):
    if text_input.strip():
        audio_file=text_speech(text_input,accent,c)
        c+=1
        st.audio(audio_file,format="audio/mp3")
        with open(audio_file,'rb') as file :
            st.download_button(label="Download Audio",data=file,file_name="speech.mp3",mime="audio/mp3")
    else:
        st.warning("please enter the text")

