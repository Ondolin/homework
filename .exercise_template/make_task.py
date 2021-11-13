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
  main_file = file.read()

before_begin_tasks = ""
between_tasks = []
after_end_tasks = ""

before = True
after = False

for line in main_file.splitlines():
    if '% BEGIN TASKS' in line:
        before = False
        before_begin_tasks += line + '\n'
    elif '% END TASKS' in line:
        after = True
        after_end_tasks += line + '\n'
    elif before:
        before_begin_tasks += line + '\n'
    elif after:
        after_end_tasks += line + '\n'
    elif not before and not after:
        between_tasks.append(line)

new_import = "\t\subfile{./tasks/task_" + str(task_number) + ".tex}"

if not new_import in between_tasks:
    between_tasks.append(new_import)

between_tasks.sort()

# Write the file out again
main_file = before_begin_tasks + ("\n".join([item for item in between_tasks])) + "\n" + after_end_tasks

# Write the file out again
with open("./main.tex", 'w') as file:
  file.write(main_file)


