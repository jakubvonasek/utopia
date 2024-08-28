import os

# Define the project structure
project_structure = {
    "utopia": [
        "assets/images/",
        "assets/sounds/",
        "assets/fonts/",
        "gen_ai/enemy_generator.py",
        "src/__init__.py",
        "src/main.py",
        "src/game.py",
        "src/settings.py",
        "src/player.py",
        "src/enemy.py",
        "src/utils.py",
        "requirements.txt",
        "README.md",
    ]
}

# Function to create the project structure
def create_project_structure(structure):
    for root, files in structure.items():
        # Create the root directory
        if not os.path.exists(root):
            os.mkdir(root)
        # Create each file and directory in the structure
        for file_path in files:
            full_path = os.path.join(root, file_path)
            # Check if it's a directory path (ends with a slash)
            if full_path.endswith("/"):
                os.makedirs(full_path, exist_ok=True)
            else:
                # Create the file and any intermediate directories
                os.makedirs(os.path.dirname(full_path), exist_ok=True)
                with open(full_path, 'w') as f:
                    if "README.md" in full_path:
                        f.write("# My Game Project\n\nThis is a README for my game project.")
                    elif "requirements.txt" in full_path:
                        f.write("pygame\nopenai\n")
                    else:
                        f.write("")  # Create an empty file for other scripts

# Run the function to create the structure
create_project_structure(project_structure)

print("Project structure created successfully.")
