def file_read_write():
    """
    Reads from input.txt, converts text to uppercase,
    and writes the result to output.txt
    """
    try:
        with open("input.txt", "r") as infile:
            content = infile.read()

        # Modify content (example: uppercase)
        modified_content = content.upper()

        with open("output.txt", "w") as outfile:
            outfile.write(modified_content)

        print("✅ File has been read and modified version written to output.txt")

    except FileNotFoundError:
        print("❌ input.txt not found. Please make sure the file exists.")
    except Exception as e:
        print(f"⚠️ An error occurred: {e}")


def error_handling_lab():
    """
    Asks user for a filename and tries to read it.
    Handles errors if file doesn't exist or can't be read.
    """
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, "r") as f:
            print("📂 File content:")
            print(f.read())
    except FileNotFoundError:
        print("❌ The file does not exist. Please try again.")
    except PermissionError:
        print("⚠️ You don’t have permission to read this file.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")


if __name__ == "__main__":
    print("=== Week 4 Assignment ===")
    print("1. File Read & Write Challenge")
    print("2. Error Handling Lab")

    choice = input("Choose (1/2): ")

    if choice == "1":
        file_read_write()
    elif choice == "2":
        error_handling_lab()
    else:
        print("❌ Invalid choice.")
