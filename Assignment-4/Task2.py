# Task 2: Write and Append Data to a File
 
# Problem Statement: Write a Python program that:
# 1.   Takes user input and writes it to a file named output.txt.
# 2.   Appends additional data to the same file.
# 3.   Reads and displays the final content of the file.


fh=open("output.txt",'wt')
fh.write(input("Enter text to write to the file:"))
fh.write("\n")
fh.close()
print("Data successfully written to output.txt.\n")

fh=open("output.txt",'at')
fh.write(input("Enter additional text to append:"))
print("Data successfully appended.\n")
fh.close()

try:
    fh=open("output.txt",'rt')
except:
    print("Error occured")
else:
    line1=fh.readline()
    line2=fh.readline()

    print(f"Final content of output.txt:\n{line1}{line2}")
finally:
    fh.close()


