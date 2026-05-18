"""Simple score extraction example.

Goal:
    Find text like "score: 10" and return only the number, not an enum/category.

Example:
    Input text:
        "The patient's score: 10 today."

    Output:
        ["10"]

How it works:
    1. The regex looks for the word 'score' followed by a number,
    2. The number is captured in a named group called 'target',
    3. extract_all_regex_target() returns the captured 'target' value.
"""

import re

from konsepy.rxsearch import extract_all_regex_target

class ScoreCategory(enum.Enum):
    SCORE = 1

REGEXES = [
    (
        # (?P<target>\d+) means: capture one or more digits and name that captured value 'target'
        # extract_all_regex_target() looks for this "target" group by default
        # Arg0: Regular expression to search for
        re.compile(r'\bscore\s*:\s*(?P<target>\d+)\b', re.I),
        ScoreCategory.SCORE,  # Arg1: Category to output results/scores for
        # Arg2: any postprocessors (apply on the extracted result)
        # Arg3: any preprocessors (apply before running regex, e.g., to exclude a piece of text)
    ),
]

# RUN_REGEXES_FUNC returns all extracted score values
RUN_REGEXES_FUNC = extract_all_regex_target(REGEXES)
