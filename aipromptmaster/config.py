"""
Configuration object
"""
from os import PathLike, getenv, path
from typing import Union

import toml
from dotenv import load_dotenv


class Singleton(type):
    """Defines a Singleton class

    To use in classes metadata to ensure only one object is created for that class
    """

    _instances = {}

    def __call__(self, *args, **kwargs):
        """Call method for the singleton"""
        if self not in self._instances:
            self._instances[self] = super(Singleton, self).__call__(*args, **kwargs)
        return self._instances[self]


class Config(metaclass=Singleton):
    """Configuration object"""

    # TODO: migrating to Pyhton 3.10+, the following should be
    #       def __init__(self, filename: str | PathLike = "aipromptmaster.toml"):
    #       removing the Union import
    def __init__(self, filename: Union[str, PathLike] = "aipromptmaster.toml"):
        """
        Config init method

        Singleton: called just once
        :param filename: name of the .toml file for configuration
        """
        self._config = {}
        load_dotenv()

        # Load TOML file if exists
        if path.exists(filename):
            with open(filename, "r") as f:
                self._config = toml.load(f)

    # Helper to get variable from toml, .env (or environment) or from a default
    def _get_property(
        self, toml_section: str, property_name: str, default_var: str = ""
    ):
        env_var = getenv(property_name.upper())
        cat = self._config.get(toml_section.lower(), {})
        return cat.get(property_name.lower(), env_var or default_var)

    @property
    def fast_llm_model(self) -> str:
        """
        The fast language model

        :default: 'gpt-3.5-turbo'
        """
        return self._get_property("language_model", "FAST_LLM_MODEL", "gpt-3.5-turbo")
