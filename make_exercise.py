import shutil
from pathlib import Path

# I know that this is not very resource efficient, but if it matters you are using this script wrong...
def get_exercise_number():
    try:
        value = int(input("Exercise number: "))
    except ValueError:
        print("Please enter a number!")
        value = get_exercise_number()
    return value

exercise_number = get_exercise_number()

generated_dir = Path("./.generated")
exercise_dir = Path("./exercise_" + str(exercise_number))

print(exercise_dir)

# Overwrite the generated directory if it exists?
if exercise_dir.is_dir():
    overwrite = input("Generated directory already exists. Overwrite? (y/n) ")
    if overwrite == "y":
        shutil.rmtree(exercise_dir)
    else:
        print("Aborting.")
        exit()

shutil.copytree(generated_dir, exercise_dir)

# Read in the file
with open("./exercise_" + str(exercise_number) + "/main.tex", 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('{EXERCISE_NUMBER}', str(exercise_number))

# Write the file out again
with open("./exercise_" + str(exercise_number) + "/main.tex", 'w') as file:
  file.write(filedata)
