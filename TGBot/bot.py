import telebot
import random
import os

bot = telebot.TeleBot("8102717177:AAHSZcp2bnLplAaU1Sa6CfOFmU5HjpTcSsw")

#/start
   
@bot.message_handler(commands=['start'])
def send_welcome(message):
        bot.send_message(message.chat.id, "Привет! Я твой Telegram бот. Напиши что-нибудь! /help - список команд")

#/help

@bot.message_handler(commands=['help'])
def help(message):
        with open('help', 'r', encoding='utf-8') as f:
                bot.send_message(message.chat.id, f.read())

@bot.message_handler(commands=['mem'])
def send_mem(message):
       mem_list = os.listdir('mems')
       mem = random.choice(mem_list)
       with open('mems/'+mem, 'rb') as f:
              bot.send_photo(message.chat.id, f)


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

stickers = ["CAACAgIAAxkBAAEQdUJobNWHNUlVg_-v7H70JoJOy24FRAAC8gADVp29ChCdi3ZTetJkNgQ",
            "CAACAgEAAxkBAAEBbTBodl3PznHD-UmXoM608OE2jY6o9AAC7wIAAjsiMUQmqGOwY2tFODYE",
            "CAACAgQAAxkBAAEQ2Ipof5tn3OuV55s4H3UrwSrg5HimhgACFQAD1XH9MSZBWhwJ106WNgQ",
            "CAACAgQAAxkBAAEQ2Ihof5tmi3VLR0dQineSYcvkdy0_SwACCQAD1XH9MXjDnpQAAdiqJTYE",
            "CAACAgQAAxkBAAEQ2IZof5tlE8GLaFAIB2WvWaKAmlpE2QACBAAD1XH9MV0kRSAPQPr-NgQ",
            "CAACAgIAAxkBAAEQ2IRof5tYQ55dserXQo0KS6_jJLv-XwACXQsAAo3c0Unev12H8zdoNTYE",
            "CAACAgIAAxkBAAEQfFRobZxYdmPomD1mk2CRJB1jc5GJ2QACGwoAAk2N0EkeWjg1iHogKDYE",
            "CAACAgIAAxkBAAEQqv9odlZdmGwMN9ONRocMRsrNsyy78wACBwEAAladvQq_tyZhIpO5ojYE",
            "CAACAgIAAxkBAAEQj0JocMjTfNCNnJomKRjWvo_YB7RlzQAC9AADVp29ChFYsPXZ_VVJNgQ",
            "CAACAgIAAxkBAAEQ2Hxof5tLg8rAGQJDCSCl27pc8uvJ_wACRwoAAuzP2EkylUUEUMTcmzYE",
            "CAACAgIAAxkBAAEQ2Hpof5tGAu0R4EGURC5SCEAgB9IVEQAC7QoAAtxe2El5u88_aLyzjzYE",
            "CAACAgIAAxkBAAEQ2Kdof53uzMzR7-r0a0ad8uS32APEwQAC4RQAAlLusUplJUN_99RMJDYE",
            "CAACAgIAAxkBAAEQcoBobAdJBgudQhy62MlC14GN3obsbAACAQADwDZPExguczCrPy1RNgQ"
            ]

@bot.message_handler(commands=['sticker'])
def send_sticker(message):
    bot.send_sticker(message.chat.id, random.choice(stickers))

@bot.message_handler(commands=['recycling'])
def recycyling_inf(message):
        inf = str(message.text.split()[1]) if len(message.text.split()) > 1 else 'helpr'
        try:
                open('recycling/'+inf)
        except IOError as e:
                inf = 'такого типа отходов нет'
        else:
               with open('recycling/'+inf, 'r', encoding='utf-8') as f:
                inf = f.read()
               
        bot.send_message(message.chat.id, inf)
       

@bot.message_handler(func=lambda message: True)
def echo_all(message):
        bot.reply_to(message, message.text)
    
bot.polling()