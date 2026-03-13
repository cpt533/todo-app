import argparse

TASK_FILE = ".tasks.txt"


def add_task(task):
    """Function: add_task

    Input - a task to add to the list
    Return - nothing
    """


def list_tasks():
    with open(TASK_FILE, "r") as file:
        tasks = [line.strip() for line in file]
        numbered_tasks = [f"{i}. {task}" for i, task in enumerate(tasks, start=1)]
        return "\n".join(numbered_tasks)


def remove_task(index):
    return


def main():
    parser = argparse.ArgumentParser(description="Command-line Todo List")
    parser.add_argument("-a", "--add", help="Add a new task")
    parser.add_argument("-l", "--list", action="store_true", help="List all tasks")
    parser.add_argument("-r", "--remove", help="Remove a task by index")

    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.list:
        tasks = list_tasks()
        print(tasks)
    elif args.remove:
        remove_task(int(args.remove))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
