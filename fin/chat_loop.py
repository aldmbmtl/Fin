"""
Handles the primary chat loop for the bot.
"""
# std
try:
    import readline
except ImportError:
    pass

# 3rd
from rich.console import Console
from rich.prompt import Prompt

# local
from .engine import Engine


def start_loop():
    """
    Starts the chat loop for the bot.
    """
    console = Console()
    engine = Engine(console)

    try:
        while True:
            user_input = Prompt.ask("")
            if user_input == "exit":
                break
            if user_input == "clear":
                console.clear()
                continue
            engine.prompt(user_input)
    except (KeyboardInterrupt, EOFError):
        return 0
