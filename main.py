import os

# Ask for a directory path and read all files and folders in it
dir_path = input("Please enter a directory path: ")
files_and_folders = os.listdir(dir_path)

# Sort the list of files and folders alphabetically
files_and_folders.sort()

# Open the text file with emails and read the emails
with open("emails.txt", "r") as file:
    emails = file.readlines()

# Sort the list of emails alphabetically
emails.sort()

# Open the new text file to write the sorted list
with open("original-txt-file-listed.txt", "w") as file:
    # Write the sorted list of files and folders
    file.write("Files and folders in " + dir_path + ":\n")
    for item in files_and_folders:
        file.write(item + "\n")

    # Write the sorted list of emails
    file.write("\nSorted emails:\n")
    for email in emails:
        file.write(email)
