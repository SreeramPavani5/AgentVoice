Voice-First Agentic AI for Government Welfare Schemes
This project implements a voice-first, agentic AI system that helps users identify and apply for government/public welfare schemes using a native Indian language (Telugu).

The system goes beyond a traditional chatbot by demonstrating:

Autonomous decision-making

Agentic reasoning (Planner-style logic)

Tool usage (eligibility checking)

Conversation memory

Failure handling for missing information

End-to-end voice input → reasoning → voice output

WorkFlow:

User Telugu Speech (input.wav)
        ↓
Speech-to-Text (Whisper – Telugu)
        ↓
Agent Planner (Decision Logic + Memory)
        ↓
Eligibility Tool (Government Scheme Logic)
        ↓
Agent Response (Telugu Text)
        ↓
Text-to-Speech (Telugu)
        ↓
Telugu Audio Output (output.wav)

Project Structure:

Agent/
│
├── app.py                 # Main voice-to-voice controller
├── input.wav              # User Telugu voice input
│
├── languages/
│   ├── __init__.py
│   ├── stt.py             # Speech-to-Text module
│   └── tts.py             # Text-to-Speech module
│
├── agent/
│   ├── __init__.py
│   ├── planner.py         # Agent decision logic
│   └── memory.py          # Conversation memory
│
├── tools/
│   ├── __init__.py
│   └── eligibility.py     # Scheme eligibility tool
│
└── requirements.txt

How to Run the Project:

Install Dependencies
pip install whisper gTTS torch ffmpeg-python
Prepare Input Audio

Record a Telugu voice input

Save it as:

input.wav
Example speech:
“నాకు ప్రభుత్వ పథకం కావాలి”

Run the Application
python app.py

Output
Telugu transcription shown in terminal
Telugu voice response generated:
output.wav


Evaluation:

Entire pipeline operates only in Telugu
Demonstrates agentic reasoning, not chatbot behavior
Explicit tool usage and memory
Designed to be demo-ready for evaluation





