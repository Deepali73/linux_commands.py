import subprocess
import shutil
import difflib

def check_command_exists(command):
    """Check if the command exists in the system's PATH."""
    return shutil.which(command) is not None

def suggest_similar_commands(command, all_commands):
    """Suggest commands similar to the given command."""
    return difflib.get_close_matches(command, all_commands, n=3, cutoff=0.6)

def execute_command(command):
    """Execute the command and handle errors."""
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e.stderr}")
    except FileNotFoundError:
        print("Command not found.")
        # Suggest similar commands
        all_commands = ["ls","date","cal","sudo","touch", "grep", "find", "cat", "python", "git", "docker", "npm", "gcc", "make"]  # Add more commands as needed
        suggestions = suggest_similar_commands(command, all_commands)
        if suggestions:
            print("Did you mean one of these?")
            for suggestion in suggestions:
                print(f"  {suggestion}")
        else:
            print("No similar commands found.")

def main():
    print("\t\t\t WELCOME TO MY TOOLS")
    print("\t\t\t--------------------")
    print()
    
    mycmd = input("Enter Your Linux task: ").strip().split()
    
    if mycmd:
        command = mycmd[0]
        if check_command_exists(command):
            execute_command(mycmd)
        else:
            print(f"'{command}' is not a valid command!!!")
            # Suggest similar commands
            all_commands = ["ls","date","cal","sudo","touch", "grep", "find", "cat", "python", "git", "docker", "npm", "gcc", "make"]  # Add more commands as needed
            suggestions = suggest_similar_commands(command, all_commands)
            if suggestions:
                print("Did you mean one of these?")
                for suggestion in suggestions:
                    print(f"  {suggestion}")
            else:
                print("No similar commands found.So try again!!!")
    else:
        print("No command entered.Please enter it again.")

if __name__ == "__main__":
    main()



