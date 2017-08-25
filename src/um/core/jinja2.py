"""Utilities for Jinja2/LaTeX stuff."""
from jinja2 import Environment, PackageLoader


jinja2_latex_env = Environment(
    block_start_string='\BLOCK{',
    block_end_string='}',
    variable_start_string='\VAR{',
    variable_end_string='}',
    comment_start_string='\#{',
    comment_end_string='}',
    line_statement_prefix='%%',
    line_comment_prefix='%#',
    autoescape=False,
    trim_blocks=True,
    loader=PackageLoader('um', 'templates/latex'),
)
