
# Social Support Demo

This is a step-by-step demonstration of how to use the Konsepy NLP Template looking at the concept `SOCIAL_SUPPORT`.

IMPORTANT: Most of this documentation is primarily for BUILDING an algorithm, NOT for running it. For help running, see the `README.md` file, or jump down to [extracting concepts, below](#extracting-concepts). 

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
  * If you receive an error about not being able to run scripts on your system (i.e., restrictive execution policy), try running: `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted -Force`
* `pip install -r requirements.txt`
  * Install requirements
* `$env:PYTHONPATH='C:\code\social_support_nlp\src'`
  * Add to PYTHONPATH
* Also, if you're not sure what a command/file requires, you can find documentation by running `python command.py -h` to print the help menu/usage

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


## Creating a New Concept (Text Snippets)

As interesting as that all is, we still haven't yet gotten started with our NLP. We may have already collected examplars or have a list of keywords to look through. We could just include these keywords in our regular expression (instead of the word 'concept'), but these terms may sometimes be relevant and at other times not-relevant.

In our case, let's suppose we have a starting list of keywords and want to look at the words in context to ensure they are capturing what we expect. Let's build up a command to run `src\get_text_snippets.py`.

* We want to use the corpus file in `sample/corpus.csv`
* We want to create a new output directory called `out` in the present directory
* We want to look for two regex groups
  * The syntax for including these is 'GROUPNAME==regular-expression-pattern'
    * Quotation marks may be required depending on the symbols used
  * SUPPORT: any mention of 'support'
  * COMPANION: any mention of a friend, family member, etc.

* `src\get_text_snippets.py --input-files sample/corpus.csv --outdir out --regexes SUPPORT==support\w* 'COMPANION==(friend|family|son|daughter)'`
* `code out/snippets_20...csv`
  * The output filename will have a timestamp
  * You may want to open in another editor (e.g., Excel)
  * It shows terms with +/- 50 characters the matched term

## Creating a New Concept (Writing Regexes)


* Looking at these examples, looking for just 'social support' might pick up positive or negative social support.
* Let's open up our `social_support.py` and `test_social_support.py` files.
  * In `test_social_support.py`, I'll replace the example text in line 11 with a few examples:
```python
# replace lines 10-14 with:
@pytest.mark.parametrize('text, exp', [
    ('good social support', SocialSupportCategory.POSITIVE),
    ('limited social support', SocialSupportCategory.NEGATIVE),
    ('missing social support', SocialSupportCategory.NEGATIVE),
    # add more tests
])
```
* Re-running our tests, we'll see that they fail (which is what we expect: we haven't yet written the regular expression patterns).
  * `pytest tests`
  * NB: the error has to do with not finding `POSITIVE` or `NEGATIVE`, since `SocialSupportCategory` doesn't have these elements. Let's go fix that.
* In `social_support.py`, 
  * add the POSITIVE and NEGATIVE categories to `SocialSupportCategory` line 22-3:
```python
class SocialSupportCategory(enum.Enum):
    """Start from 1; each must be distinct; use CAPITAL_LETTERS_WITH_UNDERSCORE is possible"""
    POSITIVE = 1  # like 'good social support'
    NEGATIVE = 2  # like 'limited social support'
```
  * add some positive and negative regexes (around lines 26-8)
```python
REGEXES = [
    (re.compile(r'\b(?:good|strong)\s*(?:social\s*support)\b', re.I), SocialSupportCategory.POSITIVE),
    (re.compile(r'\b(?:missing|limited|lack\s*of)\s*(?:social\s*support)\b', re.I), SocialSupportCategory.NEGATIVE),
]
```
  * we can also reformat these so that we can re-use the repeated regular expression values (e.g., of 'social support')
```python
social_support = r'(?:social\s*support)'
REGEXES = [
    (re.compile(fr'\b(?:good|strong)\s*{social_support}\b', re.I), SocialSupportCategory.POSITIVE),
    (re.compile(fr'\b(?:missing|limited|lack\s*of)\s*{social_support}\b', re.I), SocialSupportCategory.NEGATIVE),
]
```
  * We do this in case we want to change this to expand the regex to include 'social' and 'family':
    * `r'(?:(?:social|family)\s*support)`

* Re-run `pytest tests`
  * Note how all of the tests have now passed (`3 passed in 0.11s`)

* Repeat building tests and making them pass until you're ready to run the algorithm.


## Extracting Concepts

Now, we've finished this concept, how can we run this across our corpus of `sample/corpus.csv`?

Let's use the `src/run_all.py` program to run all of the concepts we have built:

* `python .\src\run_all.py --input-files sample/corpus.csv --outdir out`
  * This code will automatically find and run all of your concepts on the specified input files

Let's explore the output:
* `cd out/run_all_20...`
  * Navigate to the specified output directory (we specified `out`)
  * Here, we find 4 files:
    * `category_counts.csv`: how many times each of our categories appeared in the notes
    * `mrn_cateegory_counts.csv`: how many times each of the categories occurred per studyid
    * `notes_category_counts.csv`: how many times each of the categories occurred per note
    * `run_all_20....log`: the associated log file

These files can be merged with the corpus and read by structured data processes to do various analyses.

### Alternatives

If you only want to look at output for a single concept, you can use the `src/run_concept.py` command.

* Ensure that you are in $PROJECT_PATH (we `cd`'d above)
* `python .\src\run_concept.py --concepts social_support --input-files sample/corpus.csv --outdir out`
  * Runs only the concept `social_support`
    * The name of the concept is the name of the file, minus the `.py` extension
    * `social_support.py` has the concept `social_support`

To run multiple concepts, you can specify each one with the `--concepts` flag. Suppose we also had a file of concepts called `src/social_support_nlp/concepts/social_isolation.py`, the concept name would be `social_isolation`. We could run both concepts together using either the `run_all.py` or `run_concept.py` and specify multiple concepts:
* `python .\src\run_concept.py --concepts social_support social_isolation --input-files sample/corpus.csv --outdir out`


### Next Steps in Extracting Concepts

Now that you have created this example, how to create your own concepts? And, how can we determine how many concepts to have?

A 'concept' in this context is a category of regular expressions in which one wants to perform an analysis. In other words, the concepts define the output structured data we want. We may be content with a single concept (i.e., a single output variable) or we may want to subdivide that. Or, perhaps, we start with one variable and then find a greater diversity of language than we initially expected and divide the regular expressions into individual concepts. These might have to do with strict subcategories or with our own confidence.

To create a new concept, follow the steps for [Setting up a New Concept (above)](#creating-a-new-concept-setup), copying the `templates/new_concept_template.py` into `src/example_nlp/concepts`, and the `test_concept_template.py` into `tests`.


## Saving and Sharing

It is important, as well, to 'save' your work, backing it up to ensure that nothing untoward becomes of it. A great way to do this is to use a version control system like `git`. We already setup `git` in [Preparing Environment (above)](#preparing-command-line-environment), so let's consider a good approach for using it.

After getting your tests to pass, let's 'commit' (i.e., 'save') our code. 

First, we need to tell our version control system which files we want it keep track of. (We only want to save certain files -- logs and data generated by the code aren't really important to track, just code.) To see the new files that haven't yet been saved run: `git status`. In red, a number of files might be listed under the heading of 'untracked files'. To add each of these, you can run `git add <file>` with `<file>` being exactly how the files are listed. Alternatively, run `git add *.py` to keep track of all Python files in the current directory, or `git add */*.py` for keeping track of all files in the subdirectories too. Now, running `git status` we see that `git` will track these files for us going forward.

Now, we can 'save'/'commit' these 'tracked' files. We can run `git commit -a -m "added negative category to social support with passing tests"` to officially 'save' this work. Not that in the final quotation marks we have a message summarizing the changes I've made. That's it, they're saved. If we make an error and want to go back to an earlier version, we can find it.

Even though we've saved the file, it's best practice to backup our file. This can be done by 'pushing' it to another location (e.g., a backed-up fileshare or 'remote server' like Github, Gitlab, etc.). First, create the remote repository (on a fileshare, create a new directory somewhere, and then inside run `git init --bare`). Second, tell git where it is (`git remote add origin <path/url>`). Third, 'push' your history of saves to this location (probably just `git push`, but you might need to use `git push origin master`, or, perhaps `git push origin main`).

If this is in a public repository (e.g., a public repo on Github), others can access it. You can also provide more fine-grained permissions.

## Extracting Tags for Training BERT

This framework has largely been constructed to allow the simple augmentation of the manually-crafted NLP algorithm with a BERT model.

* TODO
