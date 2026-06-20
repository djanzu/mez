"""
Sanitization template filters for XSS mitigation.

Uses bleach to strip dangerous HTML (scripts, event handlers, etc.)
while preserving safe formatting tags.
"""
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

# Allowed HTML tags for blog content, search results, etc.
ALLOWED_TAGS = [
    "p", "br", "b", "i", "u", "em", "strong", "h1", "h2", "h3", "h4",
    "ul", "ol", "li", "a", "blockquote", "pre", "code", "img",
    "table", "thead", "tbody", "tr", "th", "td", "span", "div",
]
ALLOWED_ATTRIBUTES = {
    "a": ["href", "title", "rel"],
    "img": ["src", "alt", "width", "height"],
    "td": ["colspan", "rowspan"],
    "th": ["colspan", "rowspan"],
}
ALLOWED_STYLES = []  # No inline styles for safety


@register.filter
def sanitize_html(value):
    """
    Sanitize HTML content by stripping dangerous tags/attributes
    while preserving safe formatting.

    Usage in templates:
        {{ user_content|sanitize_html }}
    """
    if value is None:
        return ""
    try:
        import bleach
        return mark_safe(
            bleach.clean(
                str(value),
                tags=ALLOWED_TAGS,
                attributes=ALLOWED_ATTRIBUTES,
                styles=ALLOWED_STYLES,
                strip=True,
            )
        )
    except ImportError:
        # Fallback: if bleach is not installed, escape everything
        from django.utils.html import escape
        return escape(value)


@register.filter
def sanitize_email(value):
    """
    Sanitize content for plain-text email output.
    Strips all HTML tags and escapes special characters.

    Usage in templates:
        {{ form_value|sanitize_email }}
    """
    if value is None:
        return ""
    try:
        import bleach
        return bleach.clean(str(value), tags=[], strip=True)
    except ImportError:
        from django.utils.html import escape
        return escape(value)
