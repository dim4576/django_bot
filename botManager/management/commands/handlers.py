
from telebot import TeleBot, types
from botManager.models import Chats, Messages


def message2db(message: types.Message, answer=None):
    chat = Chats.objects.get_or_create(chatId=message.from_user.id)[0]
    print(type(chat))
    Messages.objects.create(
        bot=bool(answer),
        chat=chat,
        text=message.text if not answer else answer
    )
    if answer:
        return answer


def register_handlers(bot: TeleBot):
    @bot.message_handler(commands=['start'])
    def cmd_start(message: types.Message):
        message2db(message)
        bot.send_message(message.from_user.id, message2db(message, 'для вывода списка команд введите /help'))

    @bot.message_handler(commands=['help'])
    def cmd_help(message: types.Message):
        message2db(message)
        ans = '/start - базовая команда для регистрации в боте\n' \
              '/help - вывести список команд\n' \
              '/delete - удалить данные о себе из бота'
        bot.send_message(message.from_user.id, message2db(message, ans))

    @bot.message_handler(commands=['delete'])
    def cmd_delete(message: types.Message):
        Chats.objects.filter(chatId=message.from_user.id).delete()
        bot.send_message(message.from_user.id, 'данные успешно удалены')