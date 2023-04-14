"""
Retrieve text snippets from the corpus.
"""

from konsepy.get_text_snippets import get_text_snippets_cli

from config import PACKAGE_NAME


def get_text_snippets():
    get_text_snippets_cli(PACKAGE_NAME)


if __name__ == '__main__':
    get_text_snippets()
