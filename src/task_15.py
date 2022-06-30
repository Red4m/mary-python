"""Создать таблицу продуктов.
Атрибуты продукта: id, название, цена, количество, комментарий.
Реализовать CRUD(создание, чтение, обновление по id, удаление по id) для продуктов.
Создать пользовательский интерфейс."""

from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import delete, update
from classes import Product
from connection import engine

Session = sessionmaker(bind=engine)


def insert_pr():
    session = Session()
    product = Product(
        input('Enter name '),
        float(input('Enter price ')),
        int(input('Enter quantity ')),
        input('Enter comment '))
    session.add(product)
    session.commit()


def delete_pr():
    session = Session()
    session.execute(delete(Product).where(Product.id == int(input('Enter id for delete '))))
    session.commit()


def update_pr():
    session = Session()
    field = input('Enter a field to change(name, price, quantity or comment) ')
    if field == 'name':
        session.execute(update(Product).where(Product.id == int(input('Enter id for change ')))
                        .values(name=input(f'Enter a new {field} ')))
    elif field == 'price':
        session.execute(update(Product).where(Product.id == int(input('Enter id for change ')))
                        .values(price=input(f'Enter a new {field} ')))
    elif field == 'quantity':
        session.execute(update(Product).where(Product.id == int(input('Enter id for change ')))
                        .values(quantity=input(f'Enter a new {field} ')))
    elif field == 'comment':
        session.execute(update(Product).where(Product.id == int(input('Enter id for change ')))
                        .values(comment=input(f'Enter a new {field} ')))
    session.commit()


def show_pr():
    session = Session()
    for instance in session.query(Product).order_by(Product.id):
        print(instance)
    session.commit()


main_handler = {
    1: show_pr,
    2: insert_pr,
    3: update_pr,
    4: delete_pr,
}
