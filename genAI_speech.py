import os
import subprocess
import google.generativeai as genai
import speech_recognition as sr
import pyttsx3

# Configure Gemini API
genai.configure(api_key="YOUR_GEMINI_API_KEY")  # Replace with your real key

# Text-to-speech engine setup
engine = pyttsx3.init()

def speak(text):
    print(f"\n[Assistant]: {text}")
    engine.say(text)
    engine.runAndWait()

# Convert natural language to Linux command using Gemini
def interpret_to_linux_command(prompt):
    model = genai.GenerativeModel("gemini-pro")

    system_message = """
Convert the user's natural language instruction into a single Linux shell command.
Only return the shell command, nothing else.

Examples:
- "Create a folder called test" -> mkdir test
- "List files in Downloads" -> ls Downloads
- "Remove folder named temp" -> rm -r temp
- "Rename folder old to new" -> mv old new
- "Move file a.txt to backup" -> mv a.txt backup
- "Delete file note.txt" -> rm note.txt
- "Copy data.csv to Documents" -> cp data.csv Documents/
- "Print the current directory" -> pwd
- "Show disk usage" -> df -h

If you don't understand, return: echo "Sorry, I didn’t understand the request."
"""
    full_prompt = f"{system_message}\n\nUser: {prompt}\nCommand:"
    response = model.generate_content(full_prompt)
    return response.text.strip()

# Execute command safely
def run_linux_command(command):
    if "rm -rf /" in command:
        speak("Unsafe command detected. Execution aborted.")
        return
    try:
        speak(f"Executing: {command}")
        subprocess.run(command, shell=True, check=True)
        speak("Command executed successfully.")
    except subprocess.CalledProcessError as e:
        speak(f"Error during execution: {e}")

# Speech to text input
def get_voice_input():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("\n Speak your request:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        speak("Sorry, I couldn't understand what you said.")
    except sr.RequestError:
        speak("Speech recognition service is not available.")
    return ""

# Show supported prompts
def show_supported_examples():
    examples = [
        "Create a folder called test123",
        "List everything inside the Downloads folder",
        "Delete the folder named test123",
        "Rename folder old to new",
        "Move file data.txt to backup",
        "Copy notes.pdf to Documents",
        "Delete file temp.txt",
        "Show current directory",
        "Check disk usage",
        "Say help",
        "Say exit or quit"
    ]
    speak("Here are some example commands you can try:")
    for example in examples:
        print(f"- {example}")

# Main interaction loop
def main():
    speak("Welcome to the Linux Assistant with voice support!")
    speak("Say 'help' to see examples or 'exit' to quit.")

    while True:
        user_input = get_voice_input()
        if not user_input:
            continue

        user_input = user_input.lower()
        if user_input in ['exit', 'quit']:
            speak("Goodbye!")
            break
        elif user_input == 'help':
            show_supported_examples()
        else:
            command = interpret_to_linux_command(user_input)
            run_linux_command(command)

if __name__ == "__main__":
    main()
