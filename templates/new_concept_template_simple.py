"""
This file should not be edited. It is just a template for creating additional templates.

Steps for creating a new category:
1. Copy-paste this file to $PROJECT_PATH/src/$PROJECT_NAME/concepts
2. Name new file something like `concept.py`
3. Fix statements on the relevant lines marked # TODO
4. Copy-paste `test_concept_template` file in tests directory
5. Name new file to something like `test_concept.py`
6. Fix statements on relevant lines marked # TODO
7. Add `ConceptCategory` and `RUN_REGEXES_FUNC` to `run_all.py`
8. (Less important) Add the `run_file_on_concept` function to the `tests/test_run_regex_and_output` file.
"""
import enum
import re

from konsepy.rxsearch import search_all_regex_func
from konsepy.context.negation import check_if_negated


class ConceptCategory(enum.Enum):  # TODO: change 'Concept' to relevant concept name
    """Start from 1; each must be distinct; use CAPITAL_LETTERS_WITH_UNDERSCORE is possible"""
    CONCEPT_NAME = 1
    NEGATED = 0
    UNKNOWN = -1


REGEXES = [
  (re.compile(r'\bconcept\b', re.I),
   ConceptCategory.CONCEPT_NAME,
   [  # list of functions
     lambda **kwargs: check_if_negated(neg_concept=ConceptCategory.NEGATED, **kwargs),
   ]
   ),
]

RUN_REGEXES_FUNC = search_all_regex_func(REGEXES)
