from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def hello(request):
    text = f'<h1>"Изучаем django"</h1>\n<strong>Автор</strong>: <i>Бараксина Яна</i>'
    return HttpResponse(text)


first_name = 'Иван'
father_name = 'Петрович'
last_name = 'Иванов'
phone = '8-923-600-01-02'
email = 'vasya@mail.ru'


def about(request):
    text1 = f'<div>Имя: <strong>{first_name}</strong></div>'
    text2 = f'<div>Отчество: <strong>{father_name}</strong></div>'
    text3 = f'<div>Фамилия: <strong>{last_name}</strong></div>'
    text4 = f'<div>Телефон: <strong>{phone}</strong></div>'
    text5 = f'<div>email: <strong>{email}</strong></div>'
    text = text1 + text2 + text3 + text4 + text5
    return HttpResponse(text)


items = [
   {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
   {"id": 2, "name": "Куртка кожаная", "quantity": 2},
   {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
   {"id": 7, "name": "Картофель фри", "quantity": 0},
   {"id": 8, "name": "Кепка", "quantity": 124},
]


def item_info(request, item_id):
    item = None
    for each in items:
        if item_id == each['id']:
            item = each
    if item is None:
        text = f'<div>Товар с id={item_id} не найден</div>'
    else:
        text = f'<div>{item["name"]}: {item["quantity"]} шт.</div>'
    text += '<a href="/items/">Назад к списку товаров</a>'
    return HttpResponse(text)


def items_list(request):
    text = '<ol>'
    for each in items:
        text += f'<li><a href="/item/{each["id"]}/">{each["name"]}</a></li>'
    text += '</ol>'
    return HttpResponse(text)
