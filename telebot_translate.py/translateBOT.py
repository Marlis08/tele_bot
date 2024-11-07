# import telebot
# from translate import Translator
# from telebot import types

# translate = Translator



# bot = telebot.TeleBot('7974905170:AAEYa0GjmnUCbFABmvdirx-v3kYBQ-xiBfI')

# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup()
#     btn1 = types.KeyboardButton('Перевести слово на русский! ')
#     btn2 = types.KeyboardButton('Перевести слово на английский! ')
#     btn3 = types.KeyboardButton('Перевести слово на кыргызский!  ')
#     markup.row(btn1)
#     markup.row(btn2, btn3)
#     bot.send_message(message.chat.id, 'TranslateTeleBot вас встречает. Чем вам помочь ?', reply_markup=markup )

# translation_histori = ()

# @bot.message_handler(func=lambda message: message.text == 'перевести текст')
# def handle_translate_prompt(message):
#     user_id = message.chat.id

#     if user_id in translation_histori:
#         histori = translation_histori[user_id]
#         histori_text = '\n'.join([f'{original} -> {translated} ' for original,translated in histori   ])
#         bot.reply_to(message,f"история переводов:\n{histori_text}")
#     else:
#         bot.reply_to(message,"у вас пока нет история перевоодов ")







# bot.polling()



import telebot
from googletrans import Translator
from telebot import types

translator = Translator()

bot = telebot.TeleBot('7974905170:AAEYa0GjmnUCbFABmvdirx-v3kYBQ-xiBfI')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Перевести слово на русский')
    btn2 = types.KeyboardButton('Перевести слово на английский')
    btn3 = types.KeyboardButton('Перевести слово на кыргызский')
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, 'TranslateTeleBot вас встречает. Чем вам помочь?', reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == 'Перевести слово на русский')
def translate_to_russian(message):
    msg = bot.send_message(message.chat.id, 'Введите слово для перевода на русский:')
    bot.register_next_step_handler(msg, perform_translation, 'ru')

@bot.message_handler(func=lambda message: message.text == 'Перевести слово на английский')
def translate_to_english(message):
    msg = bot.send_message(message.chat.id, 'Введите слово для перевода на английский:')
    bot.register_next_step_handler(msg, perform_translation, 'en')

@bot.message_handler(func=lambda message: message.text == 'Перевести слово на кыргызский')
def translate_to_kyrgyz(message):
    msg = bot.send_message(message.chat.id, 'Введите слово для перевода на кыргызский:')
    bot.register_next_step_handler(msg, perform_translation, 'ky')

def perform_translation(message, dest_lang):
    try:
        user_text = message.text
        translated = translator.translate(user_text, dest=dest_lang)
        bot.send_message(message.chat.id, translated.text)
    except Exception as e:
        bot.send_message(message.chat.id, f'Не удалось выполнить перевод: {e}')

bot.polling()



# import telebot
# from translate import Translator
# from telebot import types
# import logging

# # Настройка логирования
# logging.basicConfig(level=logging.INFO)

# # Функция перевода
# def perform_translation(text, dest_lang):
#     try:
#         translator = Translator(to_lang=dest_lang)
#         translation = translator.translate(text)
#         return translation
#     except Exception as e:
#         logging.error(f'Error translating text: {e}')
#         return None

# # Инициализация бота
# bot = telebot.TeleBot('7974905170:AAEYa0GjmnUCbFABmvdirx-v3kYBQ-xiBfI')

# @bot.message_handler(commands=['start'])
# def start(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     btn1 = types.KeyboardButton('Перевести слово на русский')
#     btn2 = types.KeyboardButton('Перевести слово на английский')
#     btn3 = types.KeyboardButton('Перевести слово на кыргызский')
#     markup.add(btn1, btn2, btn3)
#     bot.send_message(message.chat.id, 'TranslateTeleBot вас встречает. Чем вам помочь?', reply_markup=markup)

# @bot.message_handler(func=lambda message: message.text == 'Перевести слово на русский')
# def translate_to_russian(message):
#     msg = bot.send_message(message.chat.id, 'Введите слово для перевода на русский:')
#     bot.register_next_step_handler(msg, handle_translation, 'ru')

# @bot.message_handler(func=lambda message: message.text == 'Перевести слово на английский')
# def translate_to_english(message):
#     msg = bot.send_message(message.chat.id, 'Введите слово для перевода на английский:')
#     bot.register_next_step_handler(msg, handle_translation, 'en')

# @bot.message_handler(func=lambda message: message.text == 'Перевести слово на кыргызский')
# def translate_to_kyrgyz(message):
#     msg = bot.send_message(message.chat.id, 'Введите слово для перевода на кыргызский:')
#     bot.register_next_step_handler(msg, handle_translation, 'ky')

# def handle_translation(message, dest_lang):
#     user_text = message.text
#     translation = perform_translation(user_text, dest_lang)
#     if translation:
#         bot.send_message(message.chat.id, translation)
#     else:
#         bot.send_message(message.chat.id, 'Не удалось выполнить перевод.')

# bot.polling()

