#!/usr/bin/env python
# sourcery skip: docstrings-for-modules

from distutils.core import setup

setup(
    name="AiPromptMaster",
    version="0.0.1",
    description="An experimental attempt to automate prompting for text-based AI",
    author="Davide Del Papa",
    author_email="davidedelpapa@gmail.com",
    packages=["aipromtmaster"],
    scripts=["bin/aiprompt"],
)
