# 🎙️ Voice Assistant (Speech Recognition & Text-to-Speech)

This project uses SpeechRecognition and pyttsx3 to create a simple voice assistant. It listens to the user's voice, converts it to text, and responds with a predefined voice output.

**🚀 Features**

✅ Converts speech to text using Google's Speech API

✅ Text-to-speech (TTS) response using pyttsx3

✅ Handles background noise for better recognition

✅ Error handling for API failures and unclear speech


**🛠️ Installation**

Ensure you have Python installed, then install the required dependencies:

1. bash

2. Copy

3. Edit

4. pip install SpeechRecognition pyttsx3

**🔹 How It Works**
1. The program listens to your voice using your microphone.

2. It processes the audio and converts it into text.

3. Based on the recognized text, it responds with a voice message.

4. If no voice is detected or an error occurs, it displays an appropriate message.

**📌 Usage**

Run the script:

1. bash

2. Copy

3. Edit

4. python script.py

You'll hear responses like:

"Hi" (if voice input is detected)

"I am also very happy. By the way, you are looking so handsome today!"

**⚠️ Notes**

1. Ensure your microphone is working properly.

2. An active internet connection is required for speech recognition.

3. Adjust recognizer.adjust_for_ambient_noise(source, duration=1) for better results in noisy environments.

**🎯 Future Improvements**

1. Add custom voice commands and responses.

2. Implement offline speech recognition.

3. Improve accuracy with AI models.
