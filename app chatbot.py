import os

ffmpeg_bin = r"C:\Users\amaly\Downloads\ffmpeg-2026-07-23-git-80eb9e99b9-essentials_build\ffmpeg-2026-07-23-git-80eb9e99b9-essentials_build\bin"
os.environ["PATH"] = ffmpeg_bin + os.pathsep + os.environ["PATH"]

import cohere
import whisper
import gradio as gr
from gtts import gTTS

# اطلبي مفتاح Cohere عند تشغيل البرنامج
api_key = input("Enter your Cohere API Key: ")

# تشغيل Cohere
co = cohere.ClientV2(api_key)

# تحميل نموذج Whisper
print("Loading Whisper model...")
whisper_model = whisper.load_model("base")
print("Model loaded successfully!")


def voice_assistant(audio_path):
    if audio_path is None:
        return "Please record your voice first.", None

    # 1. تحويل الصوت إلى نص
    result = whisper_model.transcribe(audio_path)
    user_text = result["text"].strip()

    # 2. إرسال النص إلى Cohere
    response = co.chat(
        model="command-a-03-2025",
        messages=[
            {
                "role": "user",
                "content": user_text
            }
        ]
    )

    assistant_reply = response.message.content[0].text

    # 3. تحويل رد Cohere إلى صوت
    output_audio = "response.mp3"

    tts = gTTS(
        text=assistant_reply,
        lang="en"
    )

    tts.save(output_audio)

    conversation = (
        f"You said: {user_text}\n\n"
        f"AI response: {assistant_reply}"
    )

    return conversation, output_audio


app = gr.Interface(
    fn=voice_assistant,

    inputs=gr.Audio(
        sources=["microphone", "upload"],
        type="filepath",
        label="Record or Upload Your Voice"
    ),

    outputs=[
        gr.Textbox(label="Conversation"),
        gr.Audio(label="AI Voice Response")
    ],

    title="Voice-to-Voice AI Assistant",

    description=(
        "Record your voice. Whisper converts it to text, "
        "Cohere generates a response, and gTTS converts "
        "the response back to audio."
    )
)


app.launch()