"""Unit test the utility function."""
import magic

from um.core.utils import pdflatex


template = '''
\\documentclass{article}\n
\\begin{document}\n
This is a document.\n
\\end{document}
'''


class TestPDFUtilities:

    def test_pdflatex_creates_pdf_from_latex_template(self):

        result = pdflatex(template)

        assert magic.from_buffer(result.read()).startswith('PDF document')
