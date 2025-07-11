try:
    with open("sample.txt", 'r') as file:
        print("Reading file content:")
        reading_line = file.readlines()
        for i in reading_line:
            print("Line:", i)
except FileNotFoundError:
        print("Error: The file 'sample.txt' was not found.")
