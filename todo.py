"""
todo.py is a to-do list application
uses the command line, storing list as text file.
Users can add, list or remove tasks
"""

import argparse
import os

TASK_FILE = ".tasks.txt"


def add_task(task):
    """
    Function: add_task
    Input - a task for to-do list
    Return - none
    """
    with open(TASK_FILE, "a", encoding="utf-8") as file:
        file.write(task + "\n")


def list_tasks():
    """
    Function: list_tasks
    Input - none
    Return - a numbered string of the tasks
    """
    if not os.path.exists(TASK_FILE):
        return ""

    with open(TASK_FILE, "r", encoding="utf-8") as file:
        tasks = [line.strip() for line in file]

    return "\n".join(f"{i}. {task}" for i, task in enumerate(tasks, start=1))


def remove_task(index: int):
    """
    Function: remove_task
    Input - int, the index of task to remove
    Return - none
    """
    if not os.path.exists(TASK_FILE):
        print("No tasks found.")
        return

    with open(TASK_FILE, "r", encoding="utf-8") as file:
        tasks = file.readlines()

    with open(TASK_FILE, "w", encoding="utf-8") as file:
        for i, task in enumerate(tasks, start=1):
            if i != index:
                file.write(task)

    print("Task removed.")


def remove_word(word: str):
    """
    Function: remove_word
    Input - str, word of task on task list
    Return - none

    """
    if not os.path.exists(TASK_FILE):
        print("No tasks found.")
        return

    with open(TASK_FILE, "r", encoding="utf-8") as file:
        tasks = file.readlines()

    with open(TASK_FILE, "w", encoding="utf-8") as file:
        for task in tasks:
            if word not in task:
                file.write(task)

    print("Task removed.")


def main():
    """Parse arguments."""
    parser = argparse.ArgumentParser(description="Command-line Todo List")
    parser.add_argument("-a", "--add", help="Add a new task")
    parser.add_argument("-l", "--list", action="store_true", help="List all tasks")
    parser.add_argument("-r", "--remove", help="Remove a task by index")
    parser.add_argument("-w", "--word", help="Remove a task by word")

    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.list:
        tasks = list_tasks()
        print(tasks)
    elif args.remove:
        remove_task(int(args.remove))
    elif args.word:
        remove_word(args.word)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
