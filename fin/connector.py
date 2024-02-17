"""
This module provides a function called get_ollama() that returns a persistent
instance of the Ollama class from LangChain's llms module (imported as llm_module).
This function loads configuration details and creates a new Ollama object with a
specified model and custom base URL, which can then be reused instead of creating a
new instance every time. The global LLM variable is used to store the persistent
Ollama instance for future use within the project, helping to reduce overhead
associated with creating and destroying multiple instances of the Ollama class and
making the program more efficient.
"""
import langchain_community.llms as llm_module
from .config_handler import load_config

LLM = None


def get_ollama() -> llm_module.Ollama:
    """
    Get the persistent Ollama instance used to connect to the Ollama API. The connection is meant to be persistent, so this function should be called instead of creating a new `Ollama` object each time.

    Returns:
        llm_module.Ollama: The persistent Ollama instance.
    """
    global LLM

    if LLM is not None:
        return LLM

    config = load_config()
    llm_config = config["llm"]

    # Create a new Ollama object with the specified model and custom base URL.
    LLM = llm_module.Ollama(model=llm_config["model"])
    LLM.base_url = llm_config["server"]

    return LLM
