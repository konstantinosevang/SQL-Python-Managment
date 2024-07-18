import subprocess

def run_setup():
    """
    Run the database setup script.
    """
    subprocess.run(["python", "db_setup.py"])

def run_gui():
    """
    Run the GUI script.
    """
    subprocess.run(["python", "gui.py"])

def main():
    """
    Main function to integrate setup and GUI scripts.
    """
    print("Running database setup...")
    run_setup()
    print("Database setup complete.")
    
    print("Running GUI...")
    run_gui()

if __name__ == "__main__":
    main()
