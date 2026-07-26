# 🎤 Voice-to-Voice AI Assistant

## Overview

This project is a Voice-to-Voice AI Assistant developed using Python. The assistant records the user's voice, converts it into text using Whisper, generates an AI response using Cohere, and converts the response back into speech using Google Text-to-Speech (gTTS).

---

## Project Workflow

```text
User Voice
     ↓
Speech-to-Text (Whisper)
     ↓
AI Processing (Cohere)
     ↓
Text-to-Speech (gTTS)
     ↓
Voice Response
```

---

## Libraries Used

### 1. Whisper
Used to convert the recorded voice into text.

### 2. Cohere
Used as the Large Language Model (LLM) to generate intelligent responses.

### 3. gTTS
Used to convert the AI-generated text into speech.

### 4. Gradio
Used to build the web interface for recording audio and displaying the conversation.

### 5. FFmpeg
Required by Whisper to process audio files.

### 6. os
Used to configure the FFmpeg path on Windows.

---

## Code Explanation

### Import Libraries

```python
import os
import cohere
import whisper
import gradio as gr
from gtts import gTTS
```

These libraries provide speech recognition, AI response generation, text-to-speech conversion, and the web interface.

### Connect to Cohere

The program asks the user to enter the Cohere API Key, then connects to the Cohere model.

### Load Whisper

The Whisper model is loaded once when the application starts.

### Speech-to-Text

The recorded voice is converted into text using:

```python
whisper_model.transcribe(audio_path)
```

### AI Response

The recognized text is sent to Cohere using:

```python
co.chat(...)
```

### Text-to-Speech

The generated response is converted into an MP3 file using:

```python
gTTS(...)
```

### Gradio Interface

Gradio provides:
- Voice recording
- Audio upload
- Conversation display
- AI voice playback

---

## How to Run

1. Create a virtual environment.
2. Install the required libraries.
3. Run:


```bash
python app.py
```

4. Enter the Cohere API Key.
5. Open the Gradio link.
6. Record your voice and press **Submit**.

---

## Project Demo

🎥 A demonstration video is included in this repository showing the complete workflow of the application.

https://github.com/user-attachments/assets/359d0a98-d6ad-48e8-8cc5-b1995a83444e

---

## Author

Developed by **Amal yasser Computer and Network Engineering Student  
University of Jeddah**
