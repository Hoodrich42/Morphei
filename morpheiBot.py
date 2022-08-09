import telebot
from telebot import types

bot = telebot.TeleBot('5478094534:AAG0pt58EM9kPElrA_svYxUXVBj4pDArFPU')

@bot.message_handler(commands=['start'])
def start(message):
	mess = f'Привет, {message.from_user.first_name}&#128075;'
	bot.send_message(message.chat.id, mess, parse_mode='html')
	mess = f'Я Морфей, Древнегреческий Бог сновидений&#9889;\n\nДо меня дошли вести, что миллионы людей на земле страдают из-за плохого сна. Я спустился к вам сюда, чтобы улучшить ваш сон, и сделать его более качественным.'
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
	notgood = types.KeyboardButton('Я тебя давно ждал!')
	good = types.KeyboardButton('Спасибо, но у меня все хорошо со сном')
	markup.add(notgood, good)
	bot.send_message(message.chat.id, mess, reply_markup=markup, parse_mode='html')

@bot.message_handler(content_types=['text'])
def func(message):
	#remove = types.ReplyKeyboardRemove()
	keyboard_level_0 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
	sovet = types.KeyboardButton('Дай мне один из советов для улучшения сна')
	praktikum = types.KeyboardButton('Хорошо, уговорил! Давай начнем 14-дневный практикум')
	neponravitca = types.KeyboardButton('А что если практикум не понравится?')
	keyboard_level_0.add(sovet, praktikum, neponravitca)
	if(message.text == "Я тебя давно ждал!"):
	    bot.send_message(message.chat.id, text='Прекрасно! У меня для тебя есть 14-дневный практикум сна, после которого улучшаться следующие показатели:\n\n- Эмоциональное состояние\n- Отношения с друзьями\n- Здоровье\n- Внутренняя энергия для достижения целей\n- Качество жизни', reply_markup=keyboard_level_0, parse_mode='html')
	    bot.send_message(message.chat.id, text='В данном практикуме не будет банальных советов о том, что нужно спать по 8 часов. Важно не дольше спать, важно спать качественнее. Я расскажу тебе как это сделать.')
	if(message.text == "Спасибо, но у меня все хорошо со сном"):   
	    bot.send_message(message.chat.id, text='Я очень рад за тебя!\n\nСон кажется чем-то настолько элементарным, что мало кто обращает на него внимание.\n\nСон может помочь или помешать сбросить вес, замедлить старение, предотвратить рак и добиться высоких результатов в работе.', reply_markup=keyboard_level_0, parse_mode='html')
	    bot.send_message(message.chat.id, text="В данном практикуме не будет банальных советов о том, что нужно спать по 8 часов. Важно не дольше спать, важно спать качественнее. Я расскажу тебе как это сделать.", parse_mode='html')
	else:
	    bot.send_message(message.chat.id, text="Прости, я тебя не понял", reply_markup=remove, parse_mode='html')

bot.polling(none_stop=True)	
