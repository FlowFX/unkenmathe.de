from django import template
import markdown

register = template.Library()


@register.filter
def markdownify(text):
    """Convert HTML text to Markdown."""
    return markdown.markdown(text, safe_mode='escape')