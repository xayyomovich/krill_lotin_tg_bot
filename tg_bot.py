'Video,  https://python.sariq.dev/amaliyot/27-cyr2lat-bot'
'GitHub,  https://github.com/kodchi'
'GitHub,  https://github.com/eternnoir/pyTelegramBotAPI'

from transliterate import to_cyrillic,to_latin
import telebot
bot = telebot.TeleBot("6707824393:AAH-9_0Kv4X4THGAKlvIygiihcuLbTJ8xF4", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start'])
def send_welcome(message):
     javob = 'Assalomu alaykum, xush omaded shodruz xotin:)'
     javob += '\nUshbu bot lotin alifbosidagi matnlarni krillga, krill alifbosidagi matnlarni esa lotin alifbosiga o\'giradi'
     javob += '\nMatn kiriting: '
     bot.reply_to(message,javob)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
     msg = message.text
     if msg.isascii():
          javob = to_cyrillic(msg)
     else:
          javob = to_latin(msg)

     bot.reply_to(message, javob)

bot.infinity_polling()




# maxsus = ['Faridun','Mehrangiz','Shoxrux','Shohrux']
# for uylan in maxsus:
#      if uylan == message:
#           print('Uylannnnn, Qachon uylanasan')


# matn = input('Matn kiriting: ')
# if matn.isascii():
#      print(to_cyrillic(matn))
# else:
#      print(to_latin(matn))
