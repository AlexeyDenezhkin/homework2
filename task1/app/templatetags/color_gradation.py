from django import template


register = template.Library()


@register.filter
def color_gradation(value):
    if value:
        value = float(value)
        if value < 0:
            return '#008000'
        elif 1 <= value <= 2:
            return '#FA8072'
        elif 2 < value <= 5:
            return '#FF6347'
        elif value > 5:
            return '#FF0000'
        else:
            return ''
    return ''
