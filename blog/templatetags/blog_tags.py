from django import template

register = template.Library()


def reactions(obj_set, item):
    return len([value.reaction for value in obj_set if value.reaction == item])


register.filter('reactions', reactions)
