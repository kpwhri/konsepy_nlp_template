import pytest

# TODO: change `example_nlp` to $PROJECT_NAME
# TODO: update `new_concept_template` to filename
# TODO: update `ConceptCategory` to correct concept label
from example_nlp.concepts.new_concept_template import ConceptCategory, REGEXES, RUN_REGEXES_FUNC
from konsepy.regex import search_first_regex


@pytest.mark.parametrize('text, exp', [
    ('Text excerpt containing concept.', ConceptCategory.CONCEPT_NAME),  # TODO: put tests here
    # add more tests
])
def test_run_regexes(text, exp):
    # perhaps you want to use the default RUN_REGEXES_FUNC
    results = set(RUN_REGEXES_FUNC(text))
    # or just find the first in these simple example tests
    results = set(search_first_regex(REGEXES)(text))
    assert exp in results
