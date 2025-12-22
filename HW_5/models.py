import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'publisher'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(100), nullable=False)

    def __str__(self):
        return f'{self.id}: {self.name}'

class Book(Base):
    __tablename__ = 'book'

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String(100), nullable=False)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey('publisher.id'), nullable=False)

    publisher = relationship(Publisher, backref='books')

    def __str__(self):
        return f'{self.id}: Название: "{self.title}", Id Издателя: {self.id_publisher}'

class Shop(Base):
    __tablename__ = 'shop'

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(100), nullable=False)

class Stock(Base):
    __tablename__ = 'stock'

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey('book.id'), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey('shop.id'), nullable=False)
    count = sq.Column(sq.Integer)

    bk = relationship(Book, backref='stocks')
    shop = relationship(Shop, backref='stocks')

    def __str__(self):
        return f'{self.id}: Id книги: {self.id_book} Id магазина: {self.id_shop} Количество на складе:{self.count}'

class Sale(Base):
    __tablename__ = 'sale'

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.FLOAT, nullable=False)
    date_sale = sq.Column(sq.DateTime, nullable=False)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey('stock.id'), nullable=False)
    count = sq.Column(sq.Integer)

    stock = relationship(Stock, backref='stocks')

    def __str__(self):
        return (f'{self.id}: Цена: {self.price}'
                f'Id Магазина{self.id_shop} Дата продажи:{self.date_sale}'
                f'id магазина:{self.id_stock} Количество: {self.count}')

def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

