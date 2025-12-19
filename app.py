from languages.stt import speech_to_text
from languages.tts import text_to_speech
from agent.memory import Memory
from agent.planner import plan

memory = Memory()

print("🎙️ Listening to user voice...")
user_text = speech_to_text("input.wav")
print("User:", user_text)

response = plan(user_text, memory)
print("Agent:", response)

text_to_speech(response)
print("✅ Telugu voice response saved as output.wav")
