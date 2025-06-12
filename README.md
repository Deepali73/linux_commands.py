🧠 Natural Language + Voice + Smart Linux Command Assistant
This project combines AI, voice recognition, and command validation into a powerful Linux assistant that understands your instructions, converts them into commands, validates them, suggests fixes, and optionally executes them. Whether you're typing or speaking, it has your terminal tasks covered.

🚀 Features
🔹 1. Natural Language to Linux Command (via Gemini Pro)
Converts natural English like:
"make a folder called test" → mkdir test

Uses Google’s Gemini Pro API for accurate command generation.

Helps beginners and pros write correct commands.

🔹 2. 🎤 Voice Input Support
Speaks to your system and it executes your voice-commanded tasks.

Uses:

SpeechRecognition for audio-to-text

pyttsx3 for speaking responses

🔹 3. ✅ Smart Command Validator & Suggestor
Checks if a Linux command exists.

If mistyped (like gti), it suggests: git.

Executes valid commands and prints errors or output.

