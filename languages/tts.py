from gtts import gTTS

def text_to_speech(text, output_file="response.wav"):
    tts = gTTS(text=text, lang="te")
    tts.save(output_file)
