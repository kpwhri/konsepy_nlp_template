"""
Run on only a single concept.

Usage:
    python run_concept.py --input-files corpus.csv --outdir out --concepts cough

"""

from pathlib import Path

from konsepy.cli import concept_cli
from konsepy.regex import run_regex_and_output

from config import PACKAGE_NAME


def run_concepts(input_files, outdir: Path, concepts, **kwargs):
    run_regex_and_output(PACKAGE_NAME, input_files, outdir, *concepts, **kwargs)


if __name__ == '__main__':
    concept_cli(run_concepts)
