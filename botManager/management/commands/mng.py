from telebot import TeleBot
from .handlers import register_handlers

class token:
    first = '6187649922:AAEJndzvpZTwBIYYBlZatm99mmu3Zpmb1_0'
    second = '6892175189:AAEMI715E2eFEY0aVaKQOoQ3MGoPYVeIBvQ'


class Bots:
    lst = []
    dp_flag = False
    dp = None

    def __init__(self, btoken):
        self.token = btoken
        self.bot = TeleBot(btoken)
        register_handlers(self.bot)
        if not Bots.dp_flag:
            Bots.dp_flag = True
        Bots.lst.append(self)
        self.id = len(Bots.lst) - 1

    def start(self):
        self.bot.infinity_polling()

    def print(self):
        print(self.id)


if __name__ == '__main__':
    while True:
        Bots(token.first)
        bot = Bots.lst[0]
        bot.print()
        bot.start()
        while True:
            pass
