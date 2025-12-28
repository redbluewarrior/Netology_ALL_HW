import sqlalchemy
from sqlalchemy.orm import sessionmaker

from config import DSN
from models import create_table, drop_table
from models import Users, User_Word_couple, Word_couples

engine  = sqlalchemy.create_engine(DSN)


Session = sessionmaker(bind=engine)
session = Session()

drop_table(engine)
create_table(engine)

def add_word_couple(word_en, word_ru):
    word1 = Word_couples(word_en=word_en, word_ru=word_ru)
    session.add(word1)
    session.commit()

def add_user(chat_id):
    user = Users(chat_id=chat_id)
    session.add(user)
    session.commit()

couples_range = [('red','красный'),
                 ('blue', 'синий'),
                 ('green', 'зеленый'),
                 ('yellow', 'желтый'),
                 ('black', 'черный'),
                 ('white', 'белый'),
                 ('house', 'дом'),
                 ('car', 'машина'),
                 ('cat', 'кот'),
                 ('dog', 'собака'),
                 ('time', 'время'),
                 ('water', 'вода'),
                 ('man', 'мужчина'),
                 ('woman', 'женщина'),
                 ('child', 'ребенок'),
                 ('city', 'город'),
                 ('book', 'книга'),
                 ('day', 'день'),
                 ('night', 'ночь'),
                 ('friend', 'друг'),
                 ('life', 'жизнь'),
                 ('work', 'работа'),
                 ('year', 'год'),
                 ('word', 'слово'),
                 ('number', 'число'),
                 ('good', 'хорошо')
                 ]

for word_en, word_ru in couples_range:
    add_word_couple(word_en=word_en, word_ru=word_ru)


session.close()
