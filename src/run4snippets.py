"""
Run all (or the specified) concepts and create a jsonlines file intended as input for manual review
    in the textual_review_app.

"""
from konsepy.run4snippets import main

from config import PACKAGE_NAME

if __name__ == '__main__':
    main(package_name=PACKAGE_NAME)
