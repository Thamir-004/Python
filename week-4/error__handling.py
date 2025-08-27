# Asks the user for a filename and handles errors

try:
    filename = input("Enter the filename to read: ")

    # Try opening and reading the file
    with open(filename, "r") as file:
        content = file.read()

    print("\nFile Content:")
    print(content)

except FileNotFoundError:
    print("Error: The file you entered does not exist.")
except PermissionError:
    print("Error: You don't have permission to read this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
