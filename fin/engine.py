"""

"""

# std
import os

# 3rd
from halo import Halo
from rich.table import Table
from rich.console import Console
from rich.padding import Padding
from rich.markdown import Markdown
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
        Initializes the engine.
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
        Prepares the conversation chain.
        """
        # with Halo(text='Setting expectations...', spinner='dots'):
        #     self.conversation.invoke(
        #         "Keep all responses as short as possible."
        #     )

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
        for part in tokens:
            if not os.path.exists(part):
                continue
            if part in self.loaded_files:
                continue

            code = open(part, "r").read()
            with Halo(text=f"Loading {part}...", spinner="dots"):
                # noinspection PyTypeChecker
                self.conversation.invoke(f"This code lives in {part} {code}")
                self.loaded_files.append(part)

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
