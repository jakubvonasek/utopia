import os
import subprocess
import sys
import platform

def activate_venv():
    if not os.getenv("VIRTUAL_ENV"):
        print("Virtual environment is not active.")
        if platform.system() == "Windows":
            venv_activate = os.path.join("venv", "Scripts", "activate.bat")
            
        else:
            venv_activate = os.path.join("venv", "bin", "activate")

        print(f"Activating virtual environment from {venv_activate}...")
        
        # Note: subprocess.run will not persist the activation in the current shell.
        # This is a limitation because the script cannot modify the environment of the parent shell.
        subprocess.run([venv_activate], shell=True)
    else:
        print("Virtual environment is already active.")

def run():
    activate_venv()
    subprocess.run([sys.executable, "-m", "src.main"])

def install():
    activate_venv()
    subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

def clean():
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.endswith(".pyc"):
                os.remove(os.path.join(root, file))
        if "__pycache__" in dirs:
            os.rmdir(os.path.join(root, "__pycache__"))

def help():
    print("Python script for running and managing the game project")
    print("")
    print("Usage:")
    print("  python make.py run        - Run the game")
    print("  python make.py activate        - Activate venv")
    print("  python make.py install    - Install dependencies")
    print("  python make.py clean      - Clean up generated files")
    print("  python make.py help       - Show this help message")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "run":
            run()
        elif command == "activate":
            activate_venv()
        elif command == "install":
            install()
        elif command == "clean":
            clean()
        elif command == "help":
            help()
        else:
            print(f"Unknown command: {command}")
            help()
    else:
        help()
