from django import template

register = template.Library()


@register.filter(name='is_item_id_in_list')
def is_item_id_in_list(item_list, item_id):
    return any(int(item.get('item_id')) == item_id for item in item_list)


@register.simple_tag(name='find_quantity')
def find_quantity(item_list, item_id):
    for item in item_list:
        if str(item.get('item_id')) == str(item_id):
            return item.get('quantity')
    return 0