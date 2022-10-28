from django import template


register = template.Library()


@register.filter(name='reactions')
def reactions(obj_set, item):
    return len([value.reaction for value in obj_set if value.reaction == item])
