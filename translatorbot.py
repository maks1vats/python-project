import telebot
from deep_translator import GoogleTranslator

bot = telebot.TeleBot('8342919678:AAGQbzJrhJuGxnW3hoSHaGvyHFYlKAMeuVY')

defaultlang = 'uk'


@bot.message_handler(commands=['start'])
def starttext(message):
    text = (
        "Привіт! Я бот-перекладач.\n"
        "Надішли мені текст і я перекладу його на українську.\n"
        "Для перекладу на іншу мову використовуй формат:\n"
        "<код мови> <текст>\n"
        "Приклади:\n"
        "en Привіт світ (Переклад на англійську)\n"
        "de Привіт світ (Переклад на німецьку)"
    )
    bot.reply_to(message, text)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def translate(message):
    text = message.text.strip()
    lang = defaultlang
    texttotrans = text

    parts = text.split(maxsplit=1)

    if len(parts) > 1 and len(parts[0]) <= 5:
        lang = parts[0].lower()
        texttotrans = parts[1]

    try:
        translator = GoogleTranslator(source='auto', target=lang)
        translated_text = translator.translate(texttotrans)
        answer = (
            f'Переклад на мову {lang}:\n'
            f'{translated_text}'
        )

        bot.reply_to(message, answer)

    except Exception as e:
        errormes = "Сталася помилка при перекладі! Вкажи вірно код мови, на яку хочеш перекласти свій текст!"

        bot.reply_to(message, errormes)


bot.polling(none_stop=True)
