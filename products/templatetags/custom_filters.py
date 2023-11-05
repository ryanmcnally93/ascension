from django import template

register = template.Library()


@register.filter(name='is_item_id_in_list')
def is_item_id_in_list(item_list, item_id):
    return any(int(item.get('item_id')) == item_id for item in item_list)


@register.simple_tag(name='find_quantity')
def find_quantity(item_list, item_id, date, time):
    for item in item_list:
        if str(item.get('item_id')) == str(item_id):
            if int(item_id) > 23:
                if str(item.get('date')) == str(date):
                    print(len(time))
                    return len(time)
                else:
                    continue
            else:
                return item.get('quantity')
    return 0 

@register.simple_tag(name='find_item_subtotal')
def find_item_subtotal(item_list, item_id):
    for item in item_list:
        if str(item.get('item_id')) == str(item_id):
            return item.get('item_subtotal')
    return 0