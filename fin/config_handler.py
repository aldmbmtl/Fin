"""
Load configuration from yaml file that is in the current directory.
"""
# std
from pathlib import Path

# 3rd party
import yaml


CONFIG = None


def load_config() -> dict:
    """
    Load configuration from yaml file that is in the current directory.
    """
    global CONFIG

    if CONFIG is not None:
        return CONFIG

    local_config = Path.cwd() / ".fin.yaml"
    if local_config.exists():
        with open(local_config, "r") as file:
            config = yaml.safe_load(file)
        CONFIG = config
        return config
    raise FileNotFoundError(f"Configuration file not found: {local_config}")
