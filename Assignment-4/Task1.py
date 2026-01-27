# Task 1: Read a File and Handle Errors 
# Problem Statement:  Write a Python program that:
# 1.   Opens and reads a text file named sample.txt.
# 2.   Prints its content line by line.
# 3.   Handles errors gracefully if the file does not exist.


fh=open("sample.txt",'wt')
fh.write("This is a sample text file.\n")
fh.write("It contains multiple lines.\n")
fh.close()

print("Reading file content:\n")
try:
    fh=open("sample.txt",'rt')
    

except FileNotFoundError:
    print(f"Error: The file 'sample.txt' was not found.")

else:
    line_1=fh.readline()
    line_2=fh.readline()
    print(f"Line 1: {line_1}")
    print(f"Line 2: {line_2}")
finally:
    fh.close()


