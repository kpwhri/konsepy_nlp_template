
# Social Support Demo

This is a step-by-step demonstration of how to use the Konsepy NLP Template looking at the concept `SOCIAL_SUPPORT`.

These will show the command line arguments and reasoning I walk though, using Powershell on Windows (though these same steps should work for any OS, though syntax might be slightly different).

## Initial Setup

I have Python 3.11.0, Visual Studio Code, and Git installed. These are the executables called by `python`, `code`, and `git`, respectively.

We'll use the sample corpus located in `sample/corpus.csv`.

First, let's clone the repository:

* `cd c:\code`
* `git clone https://github.com/kpwhri/konsepy_nlp_template`

Next, we'll rename the directory to better match out concept. We'll call our project ($PROJECT_NAME) 'social_support_nlp'.

* `mv konsepy_nlp_template social_support_nlp`

Now we need to rename the `example_nlp` portions inside the project itself:

* `cd social_support_nlp/src`
* `mv example_nlp social_support_nlp`
* `code config.py`
  * Renamed `example_nlp` to `social_support_nlp`
  * Removed comment (starting with '# ...')
  * Save and close

## Preparing Command Line Environment

* `cd c:\code\social_support_nlp`
  * go back to $PROJECT_NAME
* `rm .git -r -force`
  * Remove .git because we don't want to contribute back to `konsepy_nlp_template`
  * `git init`
    * Initialize fresh repo
* `C:\Users\username\AppData\Local\Programs\Python\Python311\python.exe -m venv .venv`
  * Create virtual environment
* `.venv\scripts\activate.ps1`
  * Activate virtual environment
* `pip install -r requirements.txt`
  * Install requirements
* `$env:PYTHONPATH='C:\code\social_support_nlp\src'`
  * Add to PYTHONPATH

## Creating a New Concept (Setup)

Now, we're finally ready to create a new concept. This might be a 1-concept project, so we'll just call out concept `social_support`.

* `cp .\templates\new_concept_template.py .\src\social_support_nlp\concepts\social_support.py`
  * Copy new template for our concept
* `code .\src\social_support_nlp\concepts\social_support.py`
  * In VS Code:
    * On lines 20 and 26, change `ConceptCategory` to `SocialSupportCategory`
    * I want all regular expression matches (not just the first), so I'll remove line 30 (retaining `search_all_regex`)
    * Save/close
* `cp .\templates\test_concept_template.py .\tests\test_social_support.py`
  * Create test for this concept
* `code .\tests\test_social_support.py`
  * In VS Code:
    * Change line 6, `example_nlp.concepts.new_concept_template` to `social_support_nlp.concepts.social_support`
    * Change lines 6 and 11, `ConceptCategory` to `SocialSupportCategory` like in the `social_support.py` file
    * Save/close
* Run this test with `pytest tests`
  * I see in green that '1 passed in 0.13s'
  * This works because the current regex in `social_support.py` is looking for the word 'concept' (line 26) and 'concept' shows up in the text of `test_social_support.py` on line 11.


## Creating a New Concept (Building)

* TODO
