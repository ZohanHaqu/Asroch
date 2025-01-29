import os
import sys
import subprocess
from datetime import datetime
from getpass import getuser
import string

def openMainDirectory():
    """Opens the main directory based on the operating system."""
    main_dir = "C:\\" if os.name == "nt" else "/"
    os.startfile(main_dir) if os.name == "nt" else subprocess.run(["xdg-open", main_dir])

def restartTerminal():
    """Restarts the terminal by re-executing the current script."""
    print("Restarting terminal...")
    python = sys.executable
    os.execl(python, python, *sys.argv)

def openPowershellTerminal():
    """Opens PowerShell on Windows."""
    if os.name == "nt":
        subprocess.run("powershell", shell=True)
    else:
        print("PowerShell is only available on Windows.")

def openCommandPrompt():
    """Opens Command Prompt on Windows."""
    if os.name == "nt":
        subprocess.run("cmd", shell=True)
    else:
        print("Command Prompt is only available on Windows.")

def simulateFileConversion(command):
    """Simulates the process of converting a file to a new format."""
    try:
        parts = command.split(" to ")
        if len(parts) != 2:
            raise ValueError("Invalid format. Use: convert 'filename.any' to '.newformat'")
        file_name = parts[0].split(" ")[1].strip('"')
        new_format = parts[1].strip()
        if not new_format.startswith("."):
            raise ValueError("The new format must start with a '.' (e.g., .txt).")
        print(f"Converting '{file_name}' to '{new_format}'...")
        print("Conversion completed successfully! (This is a simulated conversion.)")
    except Exception as e:
        print(f"Error: {e}")

def displayAllDrives():
    """Lists all available drives on the computer."""
    if os.name == "nt":  # Windows
        drives = [f"{letter}:\\" for letter in string.ascii_uppercase if os.path.exists(f"{letter}:\\")]
        print("Available Drives:")
        for drive in drives:
            print(f"  {drive}")
    else:  # Linux/macOS
        print("Available Drives:")
        subprocess.run(["df", "-h"])

def triggerApplication(appname):
    """Triggers an application by its name."""
    try:
        subprocess.run(appname, shell=True)
    except Exception as e:
        print(f"Error launching {appname}: {e}")

def about():
    """Displays about information."""
    print("Viso Shell version 1.1")

def listDirectories():
    """Lists all directories in the current working directory."""
    print("Directories:")
    for item in os.listdir():
        if os.path.isdir(item):
            print(f"  {item}")

def changeLanguage():
    """Allows the user to select a language for the shell."""
    languages = ["English", "Spanish", "French", "German", "Chinese", "Japanese"]
    print("Select a language:")
    for i, lang in enumerate(languages, 1):
        print(f"  {i}. {lang}")
    try:
        choice = int(input("Enter the number of your choice: "))
        if 1 <= choice <= len(languages):
            print(f"Language set to {languages[choice - 1]}.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Please enter a valid number.")

def searchFilesOnWebsite(command):
    """Simulates searching files on a website and selecting one to download."""
    try:
        url = command.split(" ")[1]
        print(f"Searching files on {url}...")
        files = ["file1.zip", "file2.tar", "file3.exe (THEY ARE ALL FAKE THIS IS A TEST FEATURE"]
        print("Available files:")
        for i, file in enumerate(files, 1):
            print(f"  {i}. {file}")
        choice = int(input("Enter the number of the file to download: "))
        if 1 <= choice <= len(files):
            print(f"Downloading {files[choice - 1]}...")
            print("Download complete.")
        else:
            print("Invalid choice.")
    except Exception as e:
        print(f"Error: {e}")

def openSystem():
    """Opens System32 on Windows or root directory on Linux/macOS."""
    path = "C:\\Windows\\System32" if os.name == "nt" else "/"
    os.startfile(path) if os.name == "nt" else subprocess.run(["xdg-open", path])

def fetchSystemInfo():
    """Displays system information."""
    print("System Information:")
    print(f"  OS: {os.name}")
    print(f"  Current User: {getuser()}")
    print(f"  Current Directory: {os.getcwd()}")

def describeCommand(command):
    """Describes what a command does."""
    descriptions = {
        "calc": "Opens the calculator application.",
        "notepad": "Opens Notepad.",
        "convert": "Converts a file to a new format.",
    }
    description = descriptions.get(command.split(" ")[0], "No description available for this command.")
    print(description)

def fullRestart():
    """Fully restarts the shell."""
    print("Fully restarting shell...")
    os.execl(sys.executable, sys.executable, *sys.argv)

def exitUnsaved():
    """Exits the shell without saving any state."""
    print("Exiting without saving...")
    sys.exit()

def shell():
    hostname = "ASR"
    username = getuser()  # Get the current username dynamically

    print("Asroch Shell 1.1")
    print("Copyright (C) Sourbert. All rights reserved.")
    print("\nFor more help, visit the help page:please visit the yt channel\n")

    while True:
        try:
            prompt = f"{hostname} C:/Users/{username}> "
            command = input(prompt).strip()
            if not command:
                continue

            if command == "help":
                print("""
Available Commands:
    root                  - Opens the root directory (C:\\ or /).
    restart               - Restarts the terminal.
    powershell!           - Opens PowerShell (Windows only).
    cmd                   - Opens Command Prompt (Windows only).
    convert "file.any" to ".format" - Simulates converting a file to a new format. (CONCEPT/FAKE)
    drives                - Lists all available drives on the computer.
    hello                 - Prints a friendly greeting.
    current_time          - Displays the current date and time.
    calculate <expression> - Evaluates a mathematical expression.
    reverse <text>        - Reverses the given text.
    trigger <appname>     - Triggers an application.
    about                 - Displays about message.
    directory             - Shows all directories.
    change-language       - Opens the language selection menu.
    search <https://example.com> - Searches files on a website.(CONCEPT/FAKE)
    system                - Opens System32 (Windows) or root (/).
    fetch                 - Shows system information.
    what-does-this-command-do <command> - Explains a command.
    full-restart          - Fully restarts the shell.
    exit_unsaved          - Exits the shell without saving.
    exit                  - Exits the shell.
    [any system command]  - Executes the system command.
                """)
            elif command == "root":
                openMainDirectory()
            elif command == "restart":
                restartTerminal()
            elif command == "powershell!":
                openPowershellTerminal()
            elif command == "cmd":
                openCommandPrompt()
            elif command.startswith("convert "):
                simulateFileConversion(command)
            elif command == "drives":
                displayAllDrives()
            elif command == "hello":
                print("Hello! Welcome to your shell.")
            elif command == "current_time":
                print(f"Current date and time: {datetime.now()}")
            elif command.startswith("calculate "):
                try:
                    expression = command[10:]
                    result = eval(expression)
                    print(f"Result: {result}")
                except Exception as e:
                    print(f"Error evaluating expression: {e}")
            elif command.startswith("reverse "):
                text = command[8:]
                print(f"Reversed: {text[::-1]}")
            elif command.startswith("trigger "):
                triggerApplication(command.split(" ")[1])
            elif command == "about":
                about()
            elif command == "directory":
                listDirectories()
            elif command == "change-language":
                changeLanguage()
            elif command.startswith("search "):
                searchFilesOnWebsite(command)
            elif command == "system":
                openSystem()
            elif command == "fetch":
                fetchSystemInfo()
            elif command.startswith("what-does-this-command-do"):
                describeCommand(command.split(" ")[1])
            elif command == "full-restart":
                fullRestart()
            elif command == "exit_unsaved":
                exitUnsaved()
            elif command == "exit":
                print("Goodbye!")
                break
            else:
                try:
                    result = subprocess.run(command, shell=True, text=True)
                except Exception as e:
                    print(f"Command error: {e}")
        except KeyboardInterrupt:
            print("\nType 'exit' to quit the shell.")
        except EOFError:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    shell()
