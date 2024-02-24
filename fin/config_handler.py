"""
Load configuration from yaml file that is in the current directory.
"""
# std
import os
from pathlib import Path

# 3rd party
import yaml


__all__ = ["load_config"]


CONFIG = None
HOME_CONFIG = Path('~').expanduser()
LOCAL_CONFIG = Path.cwd()

for path in [LOCAL_CONFIG, HOME_CONFIG]:
    config_path = path / ".fin.yaml"
    if config_path.exists():
        with config_path.open("r") as file:
            config = yaml.safe_load(file)
        CONFIG = config


def load_config() -> dict:
    """
    Load configuration from yaml file that is in the current directory.
    """
    return CONFIG
