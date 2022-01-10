import argparse


def ocr():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "source",
        type=str,
        help="This is pdf source file or dir."
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Give more output."
    )


def pdftoimg():
    pass
