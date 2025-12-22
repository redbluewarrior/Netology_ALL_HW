import sqlalchemy
import json
from sqlalchemy.orm import sessionmaker
from models import create_tables, Publisher, Shop, Book, Stock, Sale

DSN = 'postgresql://postgres:postgres@localhost:5432/netology_db_books'
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)
Session = sessionmaker(bind=engine)
session = Session()

with open('fixtures/tests_data.json', 'r') as fd:
    data = json.load(fd)

for record in data:
    model = {
        'publisher': Publisher,
        'shop': Shop,
        'book': Book,
        'stock': Stock,
        'sale': Sale,
    }[record.get('model')]
    session.add(model(id=record.get('pk'), **record.get('fields')))
session.commit()

publisher_name = input()
result = session.query(Book.title, Shop.name, Sale.price, Sale.date_sale
                          ).join(Publisher, Book.publisher
                                 ).join(Stock, Book.id == Stock.id_book
                                        ).join(Shop, Shop.id == Stock.id_shop
                                               ).join(Sale, Stock.id == Sale.id_stock
                                                      ).filter(Publisher.name == publisher_name).all()
for row in result:
    print(f'{row.title} | {row.name} | '
          f'{row.price} | {row.date_sale}')

session.close()