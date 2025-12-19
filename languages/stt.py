import whisper

model = whisper.load_model("small")

def speech_to_text(audio_file):
    result = model.transcribe(audio_file, language="te")
    return result["text"]
