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

from konsepy.rxsearch import search_first_regex, search_all_regex
from konsepy.context.negation import check_if_negated
from konsepy.context.other_subject import check_if_other_subject


class ConceptCategory(enum.Enum):  # TODO: change 'Concept' to relevant concept name
    """Start from 1; each must be distinct; use CAPITAL_LETTERS_WITH_UNDERSCORE is possible"""
    CONCEPT_NAME = 1
    NEGATED = 0
    OTHER = 3


# Example custom preprocessor function, in this case, just naively get the first sentence
def first_sentence_only(text):
    end = text.find('.')
    if end == -1:
        yield 0, len(text)
        return
    yield 0, end


# Example custom postprocessor functions (i.e., after regex is found)
def has_exclusion(precontext, postcontext, **kwargs):
    if 'old' in precontext or 'young' in postcontext:
        return ConceptCategory.NEGATED  # change the concept to this instead
    return None  # keep default concept


# naive negation
def skip_if_negated(*, precontext, **_):
    from rxsearch import SKIP
    if 'no ' in precontext.lower() or 'not ' in precontext.lower():
        return SKIP  # don't include this in the output
    return None  # keep default concept


# Basic form of REGEX:
REGEXES = [
    (re.compile(r'\bconcept\b', re.I), ConceptCategory.CONCEPT_NAME),  # TODO: replace this example
    # Here's a more powerful form where the 3rd element list will be used to `check`
    #  the context of the match to ensure it is relevant. Here, we are ensuring that
    #  the match is not negated, and not related to non-subject (e.g., reference to uncle, etc.)
    (re.compile(r'\bconcept\b', re.I),
     ConceptCategory.CONCEPT_NAME,
     [  # list of postprocessor functions
         lambda **kwargs: check_if_negated(neg_concept=ConceptCategory.NEGATED, **kwargs),
         lambda **kwargs: check_if_other_subject(other_concept=ConceptCategory.OTHER, **kwargs),
     ],
     [  # list of preprocessor functions
         first_sentence_only,
     ],
     ),
]

# TODO: keep only one of the following lines (or the last will prevail)
# find only first occurrence of each regex
RUN_REGEXES_FUNC = search_first_regex(REGEXES)
# find all occurrences of all regexes
RUN_REGEXES_FUNC = search_all_regex(REGEXES)


# You can write a custom function, in this form:
def my_custom_search(regexes):
    def _search(text, include_match=False):
        for regex, category, *other in regexes:
            for m in regex.finditer(text):
                yield (category, m) if include_match else category

    return _search
