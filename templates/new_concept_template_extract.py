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

REGEXES = [
    (
        # (?P<target>\d+) means: capture one or more digits and name that captured value 'target'
        # extract_all_regex_target() looks for this "target" group by default
        re.compile(r'\bscore\s*:\s*(?P<target>\d+)\b', re.I),
        None,  # default category if no match (required)
    ),
]

# RUN_REGEXES_FUNC returns all extracted score values
RUN_REGEXES_FUNC = extract_all_regex_target(REGEXES)
