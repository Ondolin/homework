import shutil
from pathlib import Path

template_dir = Path("./.exercise_template")
generated_dir = Path("./.generated")

# Overwrite the generated directory if it exists?
if generated_dir.is_dir():
    overwrite = input("Generated directory already exists. Overwrite? (y/n) ")
    if overwrite == "y":
        shutil.rmtree(generated_dir)
    else:
        print("Aborting.")
        exit()

shutil.copytree(template_dir, generated_dir)

subject_name = input("Enter subject name: ")

print("Names of your group members")

group_members = []

while True:
    name = input("Name: ")
    if name == "":
        break
    else:
        group_members.append(name)

group_member = (" \\\\ \n\t".join([item for item in group_members]))

# Read in the file
with open('./.generated/main.tex', 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('{SUBJECT}', subject_name)
filedata = filedata.replace('{GROUP_MEMBERS}', group_member)

# Write the file out again
with open('./.generated/main.tex', 'w') as file:
  file.write(filedata)
