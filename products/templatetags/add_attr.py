from django import template

register = template.Library()


@register.filter(name="add_attr")
def add_attr(field, css):
    attrs = {}
    name_attr, value_attr = css.split(":")
    attrs[name_attr] = value_attr
    return field.as_widget(attrs=attrs)