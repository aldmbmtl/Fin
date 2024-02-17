"""
Handles the primary chat loop for the bot.

This module contains a function named `start_loop()` that starts the main chat loop for the bot. The chat loop is implemented using the `Console` and `Prompt` classes from the rich library to provide interactive input/output handling.

The main engine responsible for code rendering, loading, and saving is accessed via the `Engine` class defined in `engine.py`.
"""
import os
import difflib
from .engine import Engine
from rich.console import Console
from rich.prompt import Prompt


def start_loop():
    """Starts the chat loop for the bot."""
    console = Console()
    engine = Engine(console)

    try:
        while True:
            user_input = Prompt.ask("")

            if user_input == "exit":
                break

            elif user_input == "clear":
                console.clear()
                continue

            elif user_input == "save":
                table, renders = engine.code_renders()
                console.print(table)
                options = [str(render["id"]) for render in renders] + ["cancel"]
                console.print(
                    "Select one of the following options to save the code to a file."
                )
                console.print("Options: " + ",".join(options))

                while True:
                    selection = Prompt.ask()

                    if selection in options:
                        break

                    else:
                        console.print(
                            f"Invalid selection. Please select one of the following options: {','.join(options)}"
                        )

                if selection == "cancel":
                    continue

                console.print(f"Loaded Files: {engine.loaded_files}")
                target = Prompt.ask("Save to")
                generated = renders[int(selection)]["code"]
                new = generated.strip().splitlines()

                if os.path.exists(target):
                    with open(target, "r") as f:
                        existing = f.read()
                    original = existing.strip().splitlines()

                    for line in difflib.unified_diff(
                        original,
                        new,
                        fromfile="generated",
                        tofile="original",
                        lineterm="",
                    ):
                        console.print(line)

                confirm = Prompt.ask("Save?")
                if confirm == "yes":
                    with open(target, "w") as f:
                        f.write(generated)
                    break

                continue

            engine.prompt(user_input)

    except (KeyboardInterrupt, EOFError):
        return 0
