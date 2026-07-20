"""A simple todo list module with add, remove, and show operations."""

from typing import Optional


def add_task(tasks: list[str], task: str) -> list[str]:
    """Add a task to the task list.

    Args:
        tasks: The current list of tasks.
        task: The task description to add.

    Returns:
        The updated list of tasks.

    Raises:
        ValueError: If the task string is empty or whitespace-only.
    """
    if not task or not task.strip():
        raise ValueError("Task cannot be empty or whitespace-only.")
    tasks.append(task.strip())
    return tasks


def remove_task(tasks: list[str], task: str) -> list[str]:
    """Remove a task from the task list.

    If the task is not found, the list is returned unchanged.

    Args:
        tasks: The current list of tasks.
        task: The task description to remove.

    Returns:
        The updated list of tasks.
    """
    if task in tasks:
        tasks.remove(task)
    return tasks


def show_tasks(tasks: list[str]) -> None:
    """Print all tasks to stdout with numbering.

    Args:
        tasks: The list of tasks to display.
    """
    if not tasks:
        print("No tasks in the list.")
        return

    print("Tasks:")
    for i, t in enumerate(tasks, start=1):
        print(f"  {i}. {t}")


def main() -> None:
    """Demo the todo list functions."""
    tasks: list[str] = []

    print("=== Todo List Demo ===\n")

    # Add some tasks
    add_task(tasks, "Buy groceries")
    add_task(tasks, "Walk the dog")
    add_task(tasks, "Read a book")

    print("After adding tasks:")
    show_tasks(tasks)

    # Remove a task
    print("\nAfter removing 'Walk the dog':")
    remove_task(tasks, "Walk the dog")
    show_tasks(tasks)

    # Try removing a task that doesn't exist
    print("\nAfter trying to remove a non-existent task:")
    remove_task(tasks, "Nonexistent task")
    show_tasks(tasks)

    # Show empty list
    print("\nEmpty list demo:")
    show_tasks([])


if __name__ == "__main__":
    main()
