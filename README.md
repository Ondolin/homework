This repository contains a template for your homework submission.

# Structure

This template assumes that you will have multiple exercise sheets, each containing multiple tasks.

```

project
├── init.py
├── make_exercise.py
├── exercise_1
│   ├── make_task.py
│   ├── main.txt
│   └── task
│       ├── task_1.txt
│       ├── task_2.txt
│       └── task_3.txt
├── exercise_2
│   ├── make_task.py
│   ├── main.txt
│   └── task
│       ├── task_1.txt
│       └── task_2.txt


```

## Init

```bash
python init.py
```

Run this to create the project structure, including the project name and your group members names.

## Make Exercise

```bash
python make_exercise.py
```

This command will create a new exercise sheet. It will ask you for the exercise name.

## Make Task

```bash
python make_task.py <name>
```

This command will create a latex subfile for your task. It will automatically add the subfile import into the main.tex file.

## Make a PDF

```bash
latexmk
mv ./out/main.pdf ./Exercise.pdf
```

## Nomenclature

1. Project = The name of the subject
2. Exercise = The entire homework sheet
3. Task = Most exercise sheets contain multiple tasks

## Disclamer

All scrips in this template should ask you before they overwrite files. It is recommended to backup files before overwriting.
