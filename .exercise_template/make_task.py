import sys
import shutil
from pathlib import Path

try:
    task_number = int(sys.argv[1])
except ValueError:
    print("Please specify a correct task number!")
    sys.exit(1)


task_path = Path("./tasks/task_" + str(task_number) + ".tex")

if task_path.exists():
    overwrite = input("Task already exists. Overwrite? (y/n) ")
    if overwrite == 'y':
        task_path.unlink()
    
    else:
        sys.exit(0)

shutil.copyfile("../.task_template.tex", "./tasks/task_" + str(task_number) + ".tex")

# Read in the file
with open("./tasks/task_" + str(task_number) + ".tex", 'r') as file :
  filedata = file.read()

# Replace the target string
filedata = filedata.replace('{TASK_NAME}', str(task_number))

# Write the file out again
with open("./tasks/task_" + str(task_number) + ".tex", 'w') as file:
  file.write(filedata)

# Read in the file
with open("./main.tex", 'r') as file :
  filedata = file.read()

before_begin_tasks = ""
between_tasks = []
after_end_tasks = ""

before = True
after = False

for line in filedata.splitlines():
    if '% BEGIN TASKS' in line:
        before = False
    if '% END TASKS' in line:
        after = True
    if before:
        before_begin_tasks += line + '\n'
    if after:
        after_end_tasks += line + '\n'
    if not before and not after:
        between_tasks.append(line)

between_tasks.appand("\t\subfile{./tasks/task_" + str(task_number) + ".tex}")

between_tasks.sort()

# Write the file out again
filedata = before_begin_tasks + ("".join([item for item in between_tasks])) + after_end_tasks

# remove the last newline
filedata = filedata[:-1]

# Write the file out again
with open("./main.tex", 'w') as file:
  file.write(filedata)


