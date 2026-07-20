"""Tests for the todo list module."""

import unittest
from io import StringIO
from unittest.mock import patch

from todo import add_task, remove_task, show_tasks


class TestAddTask(unittest.TestCase):
    """Tests for add_task()."""

    def test_add_task_to_empty_list(self) -> None:
        """Adding a task to an empty list should append it."""
        tasks: list[str] = []
        result = add_task(tasks, "Buy milk")
        self.assertEqual(result, ["Buy milk"])
        self.assertIs(result, tasks)  # Should return the same list object

    def test_add_task_to_existing_list(self) -> None:
        """Adding a task to a non-empty list should append it."""
        tasks = ["Task 1"]
        result = add_task(tasks, "Task 2")
        self.assertEqual(result, ["Task 1", "Task 2"])

    def test_add_task_strips_whitespace(self) -> None:
        """Task strings should be stripped of surrounding whitespace."""
        tasks: list[str] = []
        result = add_task(tasks, "  Hello World  ")
        self.assertEqual(result, ["Hello World"])

    def test_add_empty_task_raises(self) -> None:
        """Adding an empty task should raise ValueError."""
        tasks: list[str] = []
        with self.assertRaises(ValueError):
            add_task(tasks, "")

    def test_add_whitespace_only_task_raises(self) -> None:
        """Adding a whitespace-only task should raise ValueError."""
        tasks: list[str] = []
        with self.assertRaises(ValueError):
            add_task(tasks, "   ")

    def test_add_duplicate_task(self) -> None:
        """Adding a duplicate task should append it (no dedup)."""
        tasks = ["Task A"]
        result = add_task(tasks, "Task A")
        self.assertEqual(result, ["Task A", "Task A"])


class TestRemoveTask(unittest.TestCase):
    """Tests for remove_task()."""

    def test_remove_existing_task(self) -> None:
        """Removing a task that exists should remove it."""
        tasks = ["Task 1", "Task 2", "Task 3"]
        result = remove_task(tasks, "Task 2")
        self.assertEqual(result, ["Task 1", "Task 3"])

    def test_remove_first_task(self) -> None:
        """Removing the first task should work."""
        tasks = ["A", "B", "C"]
        result = remove_task(tasks, "A")
        self.assertEqual(result, ["B", "C"])

    def test_remove_last_task(self) -> None:
        """Removing the last task should work."""
        tasks = ["A", "B", "C"]
        result = remove_task(tasks, "C")
        self.assertEqual(result, ["A", "B"])

    def test_remove_nonexistent_task(self) -> None:
        """Removing a task that doesn't exist should leave list unchanged."""
        tasks = ["Task 1"]
        result = remove_task(tasks, "Nonexistent")
        self.assertEqual(result, ["Task 1"])

    def test_remove_from_empty_list(self) -> None:
        """Removing from an empty list should return empty list."""
        tasks: list[str] = []
        result = remove_task(tasks, "Anything")
        self.assertEqual(result, [])

    def test_remove_only_first_occurrence(self) -> None:
        """list.remove removes only the first matching item."""
        tasks = ["X", "Y", "X"]
        result = remove_task(tasks, "X")
        self.assertEqual(result, ["Y", "X"])


class TestShowTasks(unittest.TestCase):
    """Tests for show_tasks()."""

    def test_show_tasks_with_items(self) -> None:
        """show_tasks should print numbered tasks."""
        tasks = ["Buy milk", "Walk dog"]
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            show_tasks(tasks)
            output = mock_stdout.getvalue()
        self.assertIn("Tasks:", output)
        self.assertIn("1. Buy milk", output)
        self.assertIn("2. Walk dog", output)

    def test_show_tasks_empty_list(self) -> None:
        """show_tasks should print a message for an empty list."""
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            show_tasks([])
            output = mock_stdout.getvalue()
        self.assertIn("No tasks", output)

    def test_show_tasks_returns_none(self) -> None:
        """show_tasks should return None."""
        result = show_tasks(["Task"])
        self.assertIsNone(result)


class TestMainDemo(unittest.TestCase):
    """Tests for the main() demo function."""

    def test_main_runs_without_error(self) -> None:
        """The main demo block should run without raising exceptions."""
        import todo
        with patch("sys.stdout", new_callable=StringIO):
            todo.main()  # Should not raise


if __name__ == "__main__":
    unittest.main()
