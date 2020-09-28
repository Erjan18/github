import telebot
print("Бот запущен!")
token = '1197470307:AAHnWda85aRmcqPfEWDtwMF7QiNnF4VlMPU'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Опять работать?!")
@bot.message_handler(content_types=['text'])
def send_message(message):
    if message.text.lower()=='привет':
        bot.send_message(message.chat.id,'Здравствуйте!')
    elif message.text.lower() == 'как дела?':
        bot.send_message(message.chat.id,'крутоооо, а у тебя?')
    elif message.text.lower() == 'отлично':
        bot.send_message(message.chat.id,'Так держать')
    elif message.text.lower() == 'хорошо':
        bot.send_message(message.chat.id,'Кто бы сомневался')
    elif message.text.lower() == 'кто лучший игрок':
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAMQX3HlYPMFlEeIeR8f1yOv79_5exkAAhYAA1oeUBXzaBXcgsATXRsE')
    elif message.text.lower() == 'кто тебе нравиться':
        bot.send_sticker(message.chat.id,'CAACAgIAAxkBAAMUX3Hn0AJT02RGRh-tIXdZfgQz72EAAioAA3j6-xfQm9a1pUIWpBsE')
    elif message.text.lower() == 'скинь ссылку на youtube':
        bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=gHgv19ip-0c')

@bot.message_handler(content_types=['sticker'])
def send_stiker(message):
    print(message)
bot.polling()