import telebot
from telebot import types

token = 'Your token'
bot = telebot.TeleBot(token)


def create_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    drink_btn = types.InlineKeyboardButton(text='Хочу пить', callback_data='1')
    eat_btn = types.InlineKeyboardButton(text='Хочу есть', callback_data='2')
    walk_btn = types.InlineKeyboardButton(text='Хочу гулять', callback_data='3')
    sleep_btn = types.InlineKeyboardButton(text='Хочу спать', callback_data='4')
    joke_btn = types.InlineKeyboardButton(text='Хочу шутку', callback_data='5')
    keyboard.add(drink_btn)
    keyboard.add(eat_btn)
    keyboard.add(walk_btn)
    keyboard.add(sleep_btn)
    keyboard.add(joke_btn)
    return keyboard


@bot.message_handler(commands=['start'])
def start_bot(message):
    keyboard = create_keyboard()
    bot.send_message(
        message.chat.id,
        'Добрый день! Выберите, что вы хотите',
        reply_markup=keyboard
    )


@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    keyboard = create_keyboard()
    if call.message:
        if call.data == '1':
            img = open('9-17.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption='Картинка воды',
                reply_markup=keyboard
            )
            img.close()
        if call.data == '2':
            img = open('darzoves2.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption='Картинка еды',
                reply_markup=keyboard
            )
            img.close()
        if call.data == '3':
            img = open('2105-001.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption='Картинка прогулки',
                reply_markup=keyboard
            )
            img.close()
        if call.data == '4':
            img = open('zhirnyy-lobok5.jpeg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption='Картинка сна',
                reply_markup=keyboard
            )
            img.close()
        if call.data == '5':
            img = open('j22.jpg', 'rb')
            bot.send_photo(
                chat_id=call.message.chat.id,
                photo=img,
                caption='Картинка шутки',
                reply_markup=keyboard
            )
            img.close()


if __name__ == '__main__':
    bot.polling(none_stop=True)
