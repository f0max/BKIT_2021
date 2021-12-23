#!/usr/bin/python3

import telebot as tb
from bs4 import BeautifulSoup as BS
import requests

TOKEN = "YOUR:own_private_secure-Bot_token"
URL = "https://coinmarketcap.com/currencies/"
HELLO = "Let's start"
HELP = "Just choose the crypto you wanna to see the price of"

bot = tb.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands='start')
def send_welcome(message):
    markup = tb.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itmbtn1 = tb.types.KeyboardButton('₿')
    itmbtn2 = tb.types.KeyboardButton('Ξ')
    itmbtn3 = tb.types.KeyboardButton('BNB')
    markup.add(itmbtn1, itmbtn2, itmbtn3)
    bot.send_message(message.chat.id, HELLO, reply_markup=markup)

@bot.message_handler(commands='help')
def send_help(message):
    bot.send_message(message.chat.id, HELP)

def ParseCryptoValue(crypto):
    r = requests.get(URL + crypto)
    soup = BS(r.content, "lxml")
    crypto_value = soup.find("div", class_="priceValue").text
    return crypto_value

@bot.message_handler(content_types='text')
def text(message):
    if message.text == '₿':
        bot.send_message(message.chat.id, ParseCryptoValue("bitcoin"))
    elif message.text == 'Ξ':
        bot.send_message(message.chat.id, ParseCryptoValue("ethereum"))
    elif message.text == 'BNB':
        bot.send_message(message.chat.id, ParseCryptoValue("binance-coin"))

bot.infinity_polling()
