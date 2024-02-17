"""
This module is used to connect to the Ollama API.

The connection is ment to be persistent, so the Ollama instance is stored in a global variable.
"""
# 3rd
from langchain_community.llms import Ollama

# local
from .config_handler import load_config

LLM = None


def get_ollama() -> Ollama:
    """
    Get the Ollama instance
    """
    global LLM

    if LLM is not None:
        return LLM

    config = load_config()
    llm_config = config["llm"]

    LLM = Ollama(model=llm_config["model"])

    # this is a hack since it seems the base_url doesn't seem to be settable from the constructor
    LLM.base_url = llm_config["server"]

    return LLM
