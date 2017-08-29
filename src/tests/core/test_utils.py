"""Unit test the utility function."""
import magic

from um.core.utils import pdflatex


template = '''
\\documentclass{article}\n
\\begin{document}\n
This is a document.\n
\\end{document}
'''


def test_pdflatex_creates_pdf_from_latex_template():

    result = pdflatex(template)

    assert magic.from_buffer(result.read(1024)).startswith('PDF document')
