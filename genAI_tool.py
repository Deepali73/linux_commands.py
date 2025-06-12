import os
import subprocess
import google.generativeai as genai

# Replace your Gemini API key here for use
genai.configure(api_key="YOUR_GEMINI_API_KEY")

# Convert natural language to a Linux shell command using Gemini
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

# Execute the shell command safely
def run_linux_command(command):
    if "rm -rf /" in command:
        print("Unsafe command detected. Aborted for safety.")
        return
    try:
        print(f"Interpreted Linux Command: {command}")
        subprocess.run(command, shell=True, check=True)
        print("Command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error during execution: {e}")

# Show supported prompt examples
def show_supported_examples():
    print("\nExample Prompts You Can Use:")
    print("- Create a folder called test123")
    print("- List everything inside the Downloads folder")
    print("- Delete the folder named test123")
    print("- Rename folder old to new")
    print("- Move file data.txt to backup")
    print("- Copy notes.pdf to Documents")
    print("- Delete file temp.txt")
    print("- Show current directory")
    print("- Check disk usage")
    print("- help (to see this list again)")
    print("- exit / quit (to close the assistant)\n")

# Main loop
def main():
    print("\nNatural Language Linux Assistant (Gemini)")
    print("Type your file system task in plain English.")
    print("Type 'help' to see examples, or 'exit' to quit.")

    while True:
        user_input = input("\nYour request: ").strip()
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye.")
            break
        elif user_input.lower() == 'help':
            show_supported_examples()
        else:
            command = interpret_to_linux_command(user_input)
            run_linux_command(command)

if __name__ == "__main__":
    main()
