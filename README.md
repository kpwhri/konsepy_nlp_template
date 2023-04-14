# Konsepy NLP Template

A template for building regex-based NLP algorithms using the konsepy framework.

## About/Terminology

Konsepy works around the idea of a `concept`. A `concept` is a semantic category which might have multple representations in text. For example, a concept might be SOCIAL_ISOLATION which targets any text describing this in text (e.g., 'no friends', 'lacks social support', etc.). Another could be COUGHING which might be described in text as 'coughs', 'hacking', 'wheeze', etc. The selection of concepts will depend on the particular application. If you only care about a single output category, it's sufficient to just have a single target concept.

Each `concept` is assigned a set of regular expressions which are used to assign a concept to a section of text. These regular expressions each receive an individual label.


### About Negation
Negation is not currently supported at the regular expression level, so if negation is important for your particular application (e.g., 'coughing' vs 'not coughing'), this can be done as either two concepts or two different regular expressions.

## Getting Started

### Prerequisites

* Python 3.9+
* Download/clone this project
  * The path to this location will be referred to as `$PATH` in the instructions below (this might be `C:\code`, etc.)
* (Optional) setup a virtual environment to isolate this particular installation
  * `cd $PATH\konsepy_nlp_template`
  * `python -m venv .venv`
    * The full path to `python.exe` might need to be specified in this command
  * Activate: `.venv/scripts/activate.[ps1|sh]`
    * Now, `python` will run from the command line
* Install required packages:
  * `pip install requirements.txt`
* A corpus file
  * In the future, other data sources will be included, for now it must be `csv` or `sas7bdat`
  * Columns (these can be configured to use different names, but it's easiest if you select these names)
    * `studyid`: (required) subject-level identifier; if not important/relevant, set all instances to `1`
    * `note_id`: (required) note-level identifier; unique identifier for each note
    * `note_text`: (required) text associated with each note
    * `note_date`: (optional) date of note; not used by algorithm so probably easiest to ignore
    * corpus may contain other columns which will be ignored

### Setup

* Pick a name for your project (e.g., `cough_nlp`): `$PROJECT_NAME`
  * The name should be lowercase using only letters and underscores
  * We will call `$PROJECT_PATH` the path `$PATH/$PROJECT_NAME` (e.g., C:\code\cough_nlp)
* Rename the directory in $PATH to from `konsepy_nlp_template` to $PROJECT_NAME
* Rename the directory in $PROJECT_PATH/src from `example_nlp` to $PROJECT_NAME
* Open $PROJECT_PATH/config.py and replace `example_nlp` with $PROJECT_NAME

### Running on Command Line

There are a number of tools to simplify running/testing the various steps, but this guide will be written with the command line in mind (in particular, Powershell on Windows)

Before running any of the commands in the following sections, always be sure that you have prepared your shell with these commands:

* Navigate to project path
  * `cd $PROJECT_PATH`
* Initialize virtual environment
  * `.venv\scripts\activate.ps1`
* Set PYTHONPATH to include project (so Python knows where to find your code)
  * `$env:PYTHONPATH=$PROJECT_PATH\src`

### Creating A New Concept

In creating a new concept, we will approach it in the style of test-driven development. We will first identify an examplar piece of text (either drawn from our corpus or, my preference, inspired by it), and then write a regular expression to make sure that our test case is captured.

* Copy over concept and test files to appropriate directories and rename
  * Copy `new_concept_template.py` to $PROJECT_PATH/src/$PROJECT_NAME/concepts
    * Rename the file to your concept (e.g., `cough.py`)
      * The name should be lowercase letters and underscores only
  * Copy `test_concept_template.py` to $PROJECT_PATH/tests
    * Rename the file to `test_` + your concept (e.g., `test_cough.py`)
  * Open both files and follow the steps inside the files (you can search on the phrase `TODO` to find relevant sections to setup)
* It's usually easiest to have both files opened side-by-side
* Create some test text (e.g., 'He has been coughing without relief.') and place it in `test_concept.py` file, overwriting thhe 'Text excerpt...' on line 11
  * Create a regular expression in `concept.py` on line 26, replacing the `\bconcept\b` with a target regex
  * You can use a site like `https://regexr.com/` to help develop your regular expressions, but beware of placing your own text online (if, e.g., it contains PHI) -- that's why it's often best to use illustrative examples.
* Now, run your tests
  * `pytest tests`
  * You should see a report highlighting, in particular, where your tests failed (if they did)
  * Fix the issue and then move to the next example

### Finding Example Test

To find example text (text 'snippets'), you can use the `$PROJECT_PATH/src/get_text_snippets.py`. These can help identify examplese of these terms/phrases in the text.

Usage:
```bash
# get text snippets when the letters 'cough' appear in corpus.csv and output to the directory `out`
python src/get_text_snippets.py --input-files corpus.csv --outdir out --regexes COUGH==cough
```

### Running Code Against a Corpus

Once the regular expressions have been built and tested, the next step is running them against the corpus.

Usage:
```bash
python src/run_all.py --input-files corpus.csv --outdir out
```

## Roadmap

* Create a complete, concrete example walking through all the steps using the `sample/corpus.csv`.
* Turn into 'cookiecutter' so that setup will be done automatically.
