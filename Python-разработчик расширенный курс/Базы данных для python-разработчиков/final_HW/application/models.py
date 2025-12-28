import sqlalchemy as sq
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'

    id = sq.Column(sq.Integer, primary_key=True)
    chat_id = sq.Column(sq.Integer, unique=True, nullable=False)
    name = sq.Column(sq.String(100), nullable=False)
    surname = sq.Column(sq.String(100), nullable=False)
    step = sq.Column(sq.Integer, default=0)

    def __str__(self):
        return f'{self.id}: {self.chat_id} {self.step}'


class Word_couples(Base):
    __tablename__ = 'word_couples'

    id = sq.Column(sq.Integer, primary_key=True)
    word_en = sq.Column(sq.String(100), nullable=False)
    word_ru = sq.Column(sq.String(100), nullable=False)

    def __str__(self):
        return f'{self.id}: {self.word_en} {self.word_ru}'


class User_Word_couple(Base):
    __tablename__ = 'user_word_couple'

    id = sq.Column(sq.Integer, primary_key=True)
    user_chat_id = sq.Column(sq.Integer, sq.ForeignKey("users.chat_id"), nullable=False)
    word_couple_id = sq.Column(sq.Integer, sq.ForeignKey("word_couples.id"), nullable=False)

    user = relationship(Users, backref='user')
    couple = relationship(Word_couples, backref='word')

    def __str__(self):
        return f'{self.id}) User: {self.user_chat_id} World_couple: {self.word_couple_id}'






def create_table(engine):
    Base.metadata.create_all(engine)

def drop_table(engine):
    Base.metadata.drop_all(engine)

