with open('output.txt','w') as file1:
    starting=str(input("Enter text to write to the file: "))
    file1.write(starting + "\n")
    print("Data successfully written to output.txt")

with open('output.txt','a') as file1:
    appending=str(input("Enter additional text to append: "))
    file1.write(appending)
    print("Data successfully appended.")

with open('output.txt','r') as file1:
    reading=file1.read()
    print("Final content of 'output.txt':\n"+reading)

