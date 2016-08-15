from __future__ import print_function
from telegram.ext import Updater

import random
updater = Updater(token = 'TOKEN')
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

if_im_happy = [
 'lame',
 'happiness is for losers',
 'happiness is a lie',
 'liar',
 'ok good'
]


if_im_sad = [
 'why?',
 'what happened?',
 'who punched you?',
 'dont be sad',
 'stop crying'
]

if_im_angry = [
  'calm down hulk'
  'why?'
]

if_im_tired = [
  'me too',
  'drink coffee',
  'poor baby',
  'stop being lazy'
]

if_im_bored = [
  'shall i tell you a fun fact?'
  'okay'
]

if_im_annoyed = [
  'oh dear',
  'hmm ok'
]

i_dont_understand = [
  'what are you talking about?',
  'huh?',
  'what?'
]

verbs = [
	'do it',
	'sit'
]

def happy(bot, update, array = if_im_happy):
 string =  random.choice(array)
 bot.sendMessage(chat_id = update.message.chat_id, text = string)

def sad(bot, update, array = if_im_sad):
 string =  random.choice(array)
 bot.sendMessage(chat_id = update.message.chat_id, text = string)

def angry(bot, update, array = if_im_angry):
 string =  random.choice(array)
 bot.sendMessage(chat_id = update.message.chat_id, text = string)

def tired(bot, update, array = if_im_tired):
 string =  random.choice(array)
 bot.sendMessage(chat_id = update.message.chat_id, text = string)

def bored(bot, update, array = if_im_bored):
 string =  random.choice(array)
 bot.sendMessage(chat_id = update.message.chat_id, text = string)

def annoyed(bot, update, array = if_im_annoyed):
 string =  random.choice(array)
 bot.sendMessage(chat_id = update.message.chat_id, text = string) 

def anything(bot, update):
 if 'why' in update.message.text:
  bot.sendMessage(chat_id = update.message.chat_id, text = "because I said so")
 elif 'do it' in update.message.text:
  bot.sendMessage(chat_id = update.message.chat_id, text = "dont tell me what to do")
 elif 'go on' in update.message.text:
  bot.sendMessage(chat_id = update.message.chat_id, text = "no")
 elif 'thanks' in update.message.text:
  bot.sendMessage(chat_id = update.message.chat_id, text = "ur not welcome")
 elif 'okay' in update.message.text:
  bot.sendMessage(chat_id = update.message.chat_id, text = "maybe okay will be our always ;)")
 elif 'reemma' in update.message.text:
  bot.sendMessage(chat_id = update.message.chat_id, text = "hello")    
 else:
  bot.sendMessage(chat_id = update.message.chat_id, text = random.choice(i_dont_understand))  
  
from telegram.ext import CommandHandler, MessageHandler, Filters

happy_handler = CommandHandler('happy', happy)
sad_handler = CommandHandler('sad', sad)
angry_handler = CommandHandler('angry', angry)
tired_handler = CommandHandler('tired', tired)
bored_handler = CommandHandler('bored', bored)
annoyed_handler = CommandHandler('annoyed', annoyed)
anything_handler = MessageHandler([Filters.text], anything)

dispatcher.add_handler(happy_handler)
dispatcher.add_handler(sad_handler)
dispatcher.add_handler(angry_handler)
dispatcher.add_handler(tired_handler)
dispatcher.add_handler(bored_handler)
dispatcher.add_handler(annoyed_handler)
dispatcher.add_handler(anything_handler)

updater.start_polling()	