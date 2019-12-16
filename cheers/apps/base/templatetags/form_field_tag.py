from django import template

register = template.Library()


# -------------------------------------------------------------------------------
# form_field_tag
# -------------------------------------------------------------------------------
@register.inclusion_tag('base/tags/form-field-tag.html')
def form_field_tag(field, showLabel=True):
    """
    Returns a common template for rendering form fields.
    """

    return {
        'field': field,
        'showLabel': showLabel
    }
