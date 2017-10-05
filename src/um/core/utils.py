"""Utility functions."""
import os
import tempfile

from subprocess import PIPE, Popen


def pdflatex(template):
    """Generate a PDF from LaTeX template and return the binary file.

    Accepts templates as string or as encoded (bytes) string.
    """
    try:
        encoded_template = template.encode('utf-8')
    except AttributeError:  # pragma: no cover
        encoded_template = template

    tempdir = tempfile.mkdtemp()

    for _ in range(2):  # noqa: F402
        process = Popen(
            ['pdflatex', '-output-directory', tempdir],
            stdin=PIPE,
            stdout=PIPE,
        )
        process.communicate(encoded_template)

    f = open(os.path.join(tempdir, 'texput.pdf'), 'rb')
    return f
