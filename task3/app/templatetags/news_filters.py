from django import template
from datetime import datetime

register = template.Library()


@register.filter
def format_date(value):
    # Ваш код
    date = datetime.timestamp(datetime.now())
    difference = date - value
    if difference < 600:
        return 'только что'
    elif 600 <= difference < 86400:
        passed_hours = round(difference / 3600)
        return f'{passed_hours} часов назад'
    elif difference >= 86400:
        date_post = datetime.utcfromtimestamp(value).date()
        return date_post.strftime('%Y-%m-%d')
    return value


# необходимо добавить фильтр для поля `score`
@register.filter
def format_score(value):
    if value < -5:
        return 'все плохо'
    elif -5 <= value <= 5:
        return 'нейтрально'
    elif value > 5:
        return 'хорошо'
    return value


@register.filter
def format_num_comments(value):
    # Ваш код
    if value == 0:
        return 'Оставьте комментарий'
    elif 0 < value <= 50:
        return value
    else:
        return "50+"


@register.filter
def format_selftext(value, count):
    if value:
        all_text = value.split()
        if len(all_text) > count * 2:
            start_text = ' '.join(all_text[:count])
            end_text = ' '.join(all_text[-count:])
            return f'{start_text} ... {end_text}'
        return value
    return ''

