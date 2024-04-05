import csv

from scrapper import settings


def get_writer(f) -> csv.DictWriter:
    writer = csv.DictWriter(f, fieldnames=\
            ['id', 
             'Тип',
             'Артикул', 
             'Имя',
             'Опубликован', 
             'Рекомендуемый?',
             'Видимость в каталоге', 
             'Краткое описание', 
             'Описание', 
             'Дата начала действия скидки',
             'Дата окончания действия скидки',
             'Статус налога',
             'Налоговый класс',
             'Наличие',
             'Запасы',
             'Величина малых запасов',
             'Возможен ли предзаказ?',
             'Продано индивидуально?',
             'Вес (кг)',
             'Длина (см)',
             'Ширина (см)', 
             'Высота (см)', 
             'Разрешить отзывы от клиентов?',
             'Примечание к покупке',
             'Акционная цена', 
             'Базовая цена', 
             'Категории', 
             'Метки',
             'Класс доставки', 
             'Изображения', 
             '360 вид',
             'Лимит загрузок',
             'Дней срока загрузки', 
             'Родительский', 
             'Сгруппированные товары', 
             'Апсэлы', 
             'Кросселы', 
             'Мета: woovina_disable_breadcrumbs', 
             'Текст кнопки', 
             'Позиция',
             'Название атрибута 1', 
             'Значения атрибутов 1',
             'Видимость атрибута 1', 
             'Глобальный атрибут 1', 
             'Название атрибута 2',
             'Значения атрибутов 2',
             'Видимость атрибута 2',
             'Глобальный атрибут 2',
             'Название атрибута 3', 
             'Значения атрибутов 3',
             'Видимость атрибута 3', 
             'Глобальный атрибут 3',
             'Название атрибута 4',
             'Значения атрибутов 4',
             'Видимость атрибута 4', 
             'Глобальный атрибут 4'])
    return writer
    

def write_headers():
    with open(f'{settings.PATH.scrapped}/products-table.csv', 'w', encoding='utf-8') as f:
        writer = get_writer(f)
        writer.writeheader()


def write_variable(variable: dict):
    with open(f'{settings.PATH.scrapped}/products-table.csv', 'a', encoding='utf-8') as f:
        writer = get_writer(f)
        variations = variable.pop('variations')
        writer.writerow(variable)
        writer.writerows(variations)