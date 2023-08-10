#2 is argv.py


while True:
    try:
        filename = input("Enter the name of the file to open: ")
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
        break
    except (FileNotFoundError, IOError):
        print("File not found. Please enter a valid filename.")
    except Exception as e:
        print("An error occurred:", e)
        break
