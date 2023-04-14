"""
Create training data file for training neural network on concept output.

"""
from konsepy.bio_tag import get_bio_tags
from konsepy.cli import add_outdir_and_infiles

from config import PACKAGE_NAME


def run_biotag(input_files, outdir, **kwargs):
    get_bio_tags(input_files, outdir, package_name=PACKAGE_NAME, **kwargs)


if __name__ == '__main__':
    run_biotag(**vars(add_outdir_and_infiles().parse_args()))
