import telebot
from telebot import types

bot = telebot.TeleBot('5687626154:AAGQBmWDvj0pqJRsf9BRRQFDV4A4QCVVLBE')


@bot.message_handler(commands=['start'])
def start(m, res=False):
    bot.send_message(m.chat.id, "Я на связи. Напиши что-нибудь")

@bot.message_handler(content_types=['text'])
def default_text(message):
    if message.text == 'Нажми меня' or message.text == 'Назад':
        keyboard = types.ReplyKeyboardMarkup()
        item_1 = types.KeyboardButton(text='Давай начнем')
        keyboard.add(item_1)
        bot.send_message(message.chat.id, 'Привет! Давай начнем', reply_markup=keyboard)

    elif message.text == 'Давай начнем':
        keyboard = types.ReplyKeyboardMarkup()
        item_2 = types.KeyboardButton(text='Точные науки')
        item_3 = types.KeyboardButton(text='Гуманитарные науки')
        keyboard.add(item_2, item_3)
        bot.send_message(message.chat.id, 'Выбери что по душе', reply_markup=keyboard)

    elif message.text == 'Точные науки':
        keyboard = types.ReplyKeyboardMarkup()
        item_2 = types.KeyboardButton(text='Математика/физика')
        item_3 = types.KeyboardButton(text='Химия/биология')
        keyboard.add(item_2, item_3)
        bot.send_message(message.chat.id, 'Выбери что по душе', reply_markup=keyboard)

    elif message.text == 'Математика/физика':
        keyboard = types.ReplyKeyboardMarkup()
        item_2 = types.KeyboardButton(text='Назад')
        keyboard.add(item_2)
        bot.send_message(message.chat.id, 'Тебе в баумана.Начнем снова', reply_markup=keyboard)

    elif message.text == 'Химия/биология':
        keyboard = types.ReplyKeyboardMarkup()
        item_2 = types.KeyboardButton(text='Назад')
        keyboard.add(item_2)
        bot.send_message(message.chat.id, 'Тебе в политех.Начнем снова', reply_markup=keyboard)

    elif message.text == 'Гуманитарные науки':
        keyboard = types.ReplyKeyboardMarkup()
        item_2 = types.KeyboardButton(text='История')
        item_3 = types.KeyboardButton(text='Литература')
        keyboard.add(item_2, item_3)
        bot.send_message(message.chat.id, 'Выбери что по душе', reply_markup=keyboard)

    elif message.text == 'История':
        keyboard = types.ReplyKeyboardMarkup()
        item_2 = types.KeyboardButton(text='Назад')
        keyboard.add(item_2)
        bot.send_message(message.chat.id, 'Тебе на раскоп.Начнем снова', reply_markup=keyboard)

    elif message.text == 'Литература':
        keyboard = types.ReplyKeyboardMarkup()
        item_2 = types.KeyboardButton(text='Назад')
        keyboard.add(item_2)
        bot.send_message(message.chat.id, 'Точно? давай в педагоги.Начнем снова', reply_markup=keyboard)


bot.polling(none_stop=True, interval=0)
