import telebot
import random
import csv
from telebot import types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton,InlineKeyboardMarkup, InlineKeyboardButton

bot = telebot.TeleBot(TOKEN)

#keyboard= telebot.types.ReplyKeyboardMarkup(True)
#keyboard.row('Маме','Папе')
#keyboard.row('Девушке/Жене','Парню/Мужу')
#keyboard.row('Бабушке','Дедушке')
#keyboard.row('Ребенку(ж)','Ребенку(м)')
#keyboard.row('Случайный подарок')

@bot.message_handler(commands=['start'])
def start_message(message):   
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    keyboard.row('Маме','Папе')
    keyboard.row('Девушке/Жене','Парню/Мужу')
    keyboard.row('Бабушке','Дедушке')
    keyboard.row('Ребенку(ж)','Ребенку(м)')
    keyboard.row('Случайный подарок')
    bot.send_message(message.chat.id, 'Привет, выбери кому ты хочешь подарок', reply_markup=keyboard)    

def total(filename):
    with open(filename) as r_file:
        row_count = sum(1 for row in r_file)-1 
        return random.randint(1, row_count)
        
        

@bot.message_handler(content_types=['text'])
def send_text(message):
    keyboardd = types.InlineKeyboardMarkup()
    count=1
    
    if message.text.lower() == 'привет' or message.text.lower() =='ку' or message.text.lower() =='здравствуйте' or message.text.lower() =='здравствуй' or message.text.lower() =='qq' or message.text.lower() == 'q':
        bot.send_message(message.chat.id, 'Ещё раз привет!')

    elif message.text.lower() == 'маме' :   
        filename="Мама.csv"     
        with open(filename) as r_file:
            reader = csv.DictReader(r_file, delimiter = ";")
            rand=random.randint(1, total(filename))
            bot.send_message(message.chat.id, 'Я думаю ей понравится это -')
            for row in reader: 
                if count==rand:
                    url_button = types.InlineKeyboardButton(text="Перейти за товаром", url=f"{row['url']}")
                    keyboardd.add(url_button)
                    bot.send_photo(message.chat.id, (row["imeg"]))                
                    bot.send_message(message.chat.id, f'Цена: {row["price"]}', reply_markup=keyboardd)
                count=count+1

    elif message.text.lower() == 'папе' :   
        filename="Папа.csv"     
        with open(filename) as r_file:
            reader = csv.DictReader(r_file, delimiter = ";")
            rand=random.randint(1, total(filename))
            bot.send_message(message.chat.id, 'Я думаю ему понравится это -')
            for row in reader: 
                if count==rand:
                    url_button = types.InlineKeyboardButton(text="Перейти за товаром", url=f"{row['url']}")
                    keyboardd.add(url_button)
                    bot.send_photo(message.chat.id, (row["imeg"]))                
                    bot.send_message(message.chat.id, f'Цена: {row["price"]}', reply_markup=keyboardd)
                count=count+1
            
    elif message.text.lower() == 'девушке' or message.text.lower() == 'жене' or message.text.lower() == 'девушке/жене':   
        filename="Девушка.csv"     
        with open(filename) as r_file:
            reader = csv.DictReader(r_file, delimiter = ";")
            rand=random.randint(1, total(filename))
            bot.send_message(message.chat.id, 'Я думаю ей понравится это -')
            for row in reader: 
                if count==rand:
                    url_button = types.InlineKeyboardButton(text="Перейти за товаром", url=f"{row['url']}")
                    keyboardd.add(url_button)
                    bot.send_photo(message.chat.id, (row["imeg"]))                
                    bot.send_message(message.chat.id, f'Цена: {row["price"]}', reply_markup=keyboardd)
                count=count+1
        
    elif message.text.lower() == 'парню' or message.text.lower() == 'мужу' or message.text.lower() == 'парню/мужу':   
        filename="Парень.csv"     
        with open(filename) as r_file:
            reader = csv.DictReader(r_file, delimiter = ";")
            rand=random.randint(1, total(filename))
            bot.send_message(message.chat.id, 'Я думаю ему понравится это -')
            for row in reader: 
                if count==rand:
                    url_button = types.InlineKeyboardButton(text="Перейти за товаром", url=f"{row['url']}")
                    keyboardd.add(url_button)
                    bot.send_photo(message.chat.id, (row["imeg"]))                
                    bot.send_message(message.chat.id, f'Цена: {row["price"]}', reply_markup=keyboardd)
                count=count+1

    elif message.text.lower() == 'бабушке':   
        filename="Бабушка.csv"     
        with open(filename) as r_file:
            reader = csv.DictReader(r_file, delimiter = ";")
            rand=random.randint(1, total(filename))
            bot.send_message(message.chat.id, 'Я думаю ей понравится это -')
            for row in reader: 
                if count==rand:
                    url_button = types.InlineKeyboardButton(text="Перейти за товаром", url=f"{row['url']}")
                    keyboardd.add(url_button)
                    bot.send_photo(message.chat.id, (row["imeg"]))                
                    bot.send_message(message.chat.id, f'Цена: {row["price"]}', reply_markup=keyboardd)
                count=count+1

    elif message.text.lower() == 'дедушке':   
        filename="Дедушка.csv"     
        with open(filename) as r_file:
            reader = csv.DictReader(r_file, delimiter = ";")
            rand=random.randint(1, total(filename))
            bot.send_message(message.chat.id, 'Я думаю ему понравится это -')
            for row in reader: 
                if count==rand:
                    url_button = types.InlineKeyboardButton(text="Перейти за товаром", url=f"{row['url']}")
                    keyboardd.add(url_button)
                    bot.send_photo(message.chat.id, (row["imeg"]))                
                    bot.send_message(message.chat.id, f'Цена: {row["price"]}', reply_markup=keyboardd)
                count=count+1

    elif message.text.lower() == 'ребенку(ж)':   
        filename="РебенокЖ.csv"     
        with open(filename) as r_file:
            reader = csv.DictReader(r_file, delimiter = ";")
            rand=random.randint(1, total(filename))
            bot.send_message(message.chat.id, 'Я думаю ей понравится это -')
            for row in reader: 
                if count==rand:
                    url_button = types.InlineKeyboardButton(text="Перейти за товаром", url=f"{row['url']}")
                    keyboardd.add(url_button)
                    bot.send_photo(message.chat.id, (row["imeg"]))                
                    bot.send_message(message.chat.id, f'Цена: {row["price"]}', reply_markup=keyboardd)
                count=count+1
    
    elif message.text.lower() == 'ребенку(м)':   
        filename="РебенокМ.csv"     
        with open(filename) as r_file:
            reader = csv.DictReader(r_file, delimiter = ";")
            rand=random.randint(1, total(filename))
            bot.send_message(message.chat.id, 'Я думаю ему понравится это -')
            for row in reader: 
                if count==rand:
                    url_button = types.InlineKeyboardButton(text="Перейти за товаром", url=f"{row['url']}")
                    keyboardd.add(url_button)
                    bot.send_photo(message.chat.id, (row["imeg"]))                
                    bot.send_message(message.chat.id, f'Цена: {row["price"]}', reply_markup=keyboardd)
                count=count+1
                
# RUN
bot.polling(none_stop=True)