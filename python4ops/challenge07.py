import os

def generate_directory_structure(user_path):
    try:
        # Validate if the provided path is a valid directory
        if not os.path.isdir(user_path):
            print("Error: The provided path is not a valid directory.")
            return

        # Use os.walk to iterate through all directories, sub-directories, and files
        for dirpath, dirnames, filenames in os.walk(user_path):
            print(f"Directory: {dirpath}")
            for filename in filenames:
                print(f"  File: {filename}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Ask the user for a file path
    user_input_path = input("Enter a directory path: ")

    # Call the function with the user-provided path
    generate_directory_structure(user_input_path)
