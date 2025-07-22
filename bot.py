import telebot
import random
bot = telebot.TeleBot("TOKEN")

#/start
   
@bot.message_handler(commands=['start'])
def send_welcome(message):
        bot.send_message(message.chat.id, "Привет! Я твой Telegram бот. Напиши что-нибудь! /help - список команд")

#/help

@bot.message_handler(commands=['help'])
def help(message):
        bot.send_message(message.chat.id, "/gen_pass - сгенерировать пароль длиной 10 символов\n"
        "/coin - подбросить монетку\n"
        "/stick или /sticker - отправить стикер")

#/gen_pass генератор паролей

@bot.message_handler(commands=['gen_pass'])
def gen_pass(message):
        elements = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        password = ""
        for i in range(10):
                x = random.choice(elements)
                password += x
        bot.reply_to(message, password)

#/coin подбросить монетку

@bot.message_handler(commands=['coin'])
def coin(message):
        x = "🪙"
        bot.reply_to(message, x)

#/stick|/sticker отправить стикер ботом        

@bot.message_handler(commands=['stick'])
def send_stick(message):
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEQdUJobNWHNUlVg_-v7H70JoJOy24FRAAC8gADVp29ChCdi3ZTetJkNgQ")      

@bot.message_handler(commands=['sticker'])
def send_sticker(message):
    bot.send_sticker(message.chat.id, "CAACAgEAAxkBAAEBbTBodl3PznHD-UmXoM608OE2jY6o9AAC7wIAAjsiMUQmqGOwY2tFODYE")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
        bot.reply_to(message, message.text)
    
bot.polling()
