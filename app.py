import telebot
from dotenv import load_dotenv
import os
import sqlalchemy as sa
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
load_dotenv()


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(sa.String(50))
    chat_id: Mapped[int] = mapped_column()

    def __repr__(self):
        return f"Username: {self.name} with id={self.id}"


engine = create_engine("sqlite:///app.db", echo=True)

Base.metadata.create_all(engine)

token = os.getenv("TOKEN")
sql_bot = telebot.TeleBot(token=token, parse_mode=None)

state = {}


@sql_bot.message_handler(commands=["start"])
def start_handler(message):
    print(message)
    state[message.from_user.id] = "get_name"
    text = "Привет, как тебя зовут?"
    sql_bot.send_message(message.chat.id, text)


@sql_bot.message_handler(func=lambda m: True)
def other(message):
    if state[message.from_user.id] == "get_name":
        name = message.text
        with Session(engine) as session:
            user = User(
                    id=message.from_user.id,
                    name=name,
                    chat_id=message.chat.id
                    )

            session.add(user)

            session.commit()

        state[message.from_user.id] == "saved"
        sql_bot.send_message(message.chat.id, "Я тебя запомнил")


print("Запускаю бота...")
sql_bot.infinity_polling()
