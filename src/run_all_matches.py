from pathlib import Path

from konsepy.cli import add_outdir_and_infiles, add_run_all_args, parse_and_clean_args
from konsepy.run_all_matches import run_all_matches

from config import PACKAGE_NAME


def run_all_concept_matches(input_files, outdir: Path,
                            id_label, noteid_label, notedate_label, notetext_label, noteorder_label=None,
                            incremental_output_only=False, concepts=None, **kwargs):
    run_all_matches(
        input_files, outdir, PACKAGE_NAME,
        id_label=id_label, noteid_label=noteid_label,
        notedate_label=notedate_label, notetext_label=notetext_label,
        noteorder_label=noteorder_label,
        concepts=concepts,
        **kwargs,
    )


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(fromfile_prefix_chars='@!')
    add_outdir_and_infiles(parser)
    add_run_all_args(parser)
    run_all_concept_matches(**parse_and_clean_args(parser))
