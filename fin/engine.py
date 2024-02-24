"""
Primary handler class to interact with the Ollama API and manage the conversation chain.
"""

# std
import os

# 3rd
from halo import Halo
from rich.table import Table
from rich.console import Console
from rich.padding import Padding
from rich.markdown import Markdown
from rich.progress import track
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferMemory


# local
from .connector import get_ollama
from .config_handler import load_config


class Engine:
    """
    The primary engine for the bot.
    """

    def __init__(self, console: Console):
        """
        initializes the engine.

        this method sets up the llm (language learning model) object from `get_ollama()`
        and retrieves the configuration settings from `load_config()`. It also initializes
        the conversation object and loads any necessary files for reference during the
        conversation.

        note that project languages are specified here, which allows them to be referenced
        later in the conversation chain.
        """
        self.llm = get_ollama()
        self.console = console
        self.config = load_config()
        self.conversation = ConversationChain(
            llm=self.llm, memory=ConversationBufferMemory()
        )
        self.loaded_files = []
        self.last_response = None
        self.languages = self.config["project"]["languages"]

        # initialize session
        self.prepare_conversation()
        self.specify_project_languages()

    def code_renders(self) -> tuple[Table, list[dict[str, str]]]:
        """ """
        blocks = self.last_response.split("```")
        renders = []

        table = Table(
            title="Generated Code", show_lines=True, header_style="bold magenta"
        )
        table.add_column("ID", justify="right", style="cyan", no_wrap=True)
        table.add_column("Code")
        table.add_column("Language", justify="center", style="green")

        idx = 0
        for block in blocks:
            for lang in self.languages:
                if block.startswith(lang):
                    code = block[len(lang) :]
                    table.add_row(str(idx), Markdown(f"```{block}```"), lang)
                    renders.append({"id": idx, "code": code})
                    idx += 1

        return table, renders

    def prepare_conversation(self):
        """
        prepares the conversation object for use in the engine. This method does not change
        the behavior of the conversation chain, but rather sets up some initial settings
        that can be referenced later.
        """
        with Halo(text="Setting expectations...", spinner="dots"):
            self.conversation.invoke("Keep all responses as short as possible.")

    def specify_project_languages(self):
        """
        Reads the config and specifies the project languages in the prompt.
        """
        langs = self.config["project"]["languages"]
        if langs:
            with Halo(text="Setting up languages...", spinner="dots"):
                self.conversation.invoke(
                    f"My project is written in the following languages: {', '.join(langs)}"
                )

    def handle_file_references(self, prompt: str):
        """
        Handles file references in the prompt and generates chain prompts for them.
        """
        tokens = prompt.split(" ")
        paths = []
        for part in tokens:
            if not os.path.exists(part):
                continue
            if part in self.loaded_files:
                continue

            if os.path.isdir(part):
                for dirpath, _, filenames in os.walk(part):
                    if "__pycache__" in dirpath:
                        continue
                    for filename in filenames:
                        paths.append(dirpath + "/" + filename)
                self.loaded_files.append(part)
            else:
                paths.append(part)

        if paths:
            for path in track(paths, description="Loading files"):
                code = open(path, "r").read()
                self.conversation.invoke(
                    f"This code lives in {path} {code} and belongs to the fin package"
                )
                self.loaded_files.append(path)

    def prompt(self, prompt: str):
        """
        Runs the engine with the given user input.
        """
        self.console.print(Markdown("---"))
        self.handle_file_references(prompt)
        with Halo(text="Thinking...", spinner="dots"):
            response = self.conversation.invoke(prompt)["response"]
            self.last_response = response
        self.console.print(Padding(Markdown(response), (2, 4), expand=False))
        self.console.print(Markdown("---"))
