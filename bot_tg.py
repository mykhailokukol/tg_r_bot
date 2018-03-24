chet = u"Понедельник:\n1. Право (Лекция)\n2. Право\n\nВторник:\n1.\n2. БД (Лаб) (Малахов)\n3. ЭМПИ (Лаб) (Егошина)\n\nСреда:\n1. \n2. БЖД (Лаб)\n3. ТИМ (Лаб) (Шнайдер)\n4. PWEBД (Лаб) (Северин)\n\nЧетверг:\n1. ПМ (Лаб) (Ларин)\n2. ТИМ (Лекция) (Шнайдер)\n3. \n4. Физ-ра\n\nПятница:\n1.\n2. \n3. БД (Малахов)"
nechet = u"Понедельник:\n1. Право (Лекция)\n\nВторник:\n1.\n2. БД (Лаб) (Малахов)\n3. ЭМПИ (Лаб) (Егошина)\n4. ЭМПИ (Лекция) (Егошина)\n\nСреда:\n1. ПМ (Лаб)\n2. БЖД (Лекция)\n3. ТИМ (Лаб) (Шнайдер)\n4. PWEBД (Лаб) (Северин)\n\nЧетверг:\n1. ПМ (Лаб) (Ларин)\n2. ТИМ (Лекция) (Шнайдер)\n3. ПМ (Лекция) (Ларин)\n4. Физ-ра\n\nПятница:\n1.\n2. \n3. БД (Малахов)\n4. PWEBД (Лекция) (Северин)"

n_monday = u'Понедельник:\n1. Право (Лекция)'
n_tuesday = u'Вторник:\n1.\n2. БД (Лаб) (Малахов)\n3. ЭМПИ (Лаб) (Егошина)\n4. ЭМПИ (Лекция) (Егошина)'
n_wednesday = u'Среда:\n1. ПМ (Лаб)\n2. БЖД (Лекция)\n3. ТИМ (Лаб) (Шнайдер)\n4. PWEBД (Лаб) (Северин)'
n_thursday = u'Четверг:\n1. ПМ (Лаб) (Ларин)\n2. ТИМ (Лекция) (Шнайдер)\n3. ПМ (Лекция) (Ларин)\n4. Физ-ра'
n_friday = u'Пятница:\n1.\n2. \n3. БД (Малахов)\n4. PWEBД (Лекция) (Северин)'
c_monday = u'Понедельник:\n1. Право (Лекция)\n2. Право'
c_tuesday = u'Вторник:\n1.\n2. БД (Лаб) (Малахов)\n3. ЭМПИ (Лаб) (Егошина)'
c_wednesday = u'Среда:\n1. \n2. БЖД (Лаб)\n3. ТИМ (Лаб) (Шнайдер)\n4. PWEBД (Лаб) (Северин)'
c_thursday = u'Четверг:\n1. ПМ (Лаб) (Ларин)\n2. ТИМ (Лекция) (Шнайдер)\n3. \n4. Физ-ра'
c_friday = u'Пятница:\n1.\n2. \n3. БД (Малахов)'

import telebot as tb
import datetime

token = "468712981:AAFHuD1rOuW31VYZOZx_qwXNgydpn3_DgFo"

date = datetime.datetime.now()

def get_week():	
	week = date.isocalendar()[1]
	return int(week)

def get_next_week():
	return (get_week() + 1)

def get_next_day():
	day = date.isocalendar()[2]
	if day != 6:
		return day
	else:
		return 0

def get_current_day():
	day = date.weekday()
	return day

bot = tb.TeleBot(token)

@bot.message_handler(commands=['this_week', 'next_week', 'tomorrow', 'today', 'traffic'])
def send_msg(msg):
	if msg.text == '/this_week' or msg.text == '/this_week@pi_raspisanie_bot':
		if (get_week() % 2 == 0):
			bot.send_message(msg.chat.id, chet)
		elif (get_week() % 2 == 1):
			bot.send_message(msg.chat.id, nechet)
		else:
			bot.send_message(msg.chat.id, "Week == 0")

	elif msg.text == '/next_week' or msg.text == '/next_week@pi_raspisanie_bot':
		if (get_next_week() % 2 == 0):
			bot.send_message(msg.chat.id, chet)
		elif (get_next_week() % 2 == 1):
			bot.send_message(msg.chat.id, nechet)
		else:
			bot.send_message(msg.chat.id, "Week == 0")

	elif msg.text == '/tomorrow' or msg.text == '/tomorrow@pi_raspisanie_bot':
		if (get_week() % 2 == 0):	
			if get_next_day() == 0:
				bot.send_message(msg.chat.id, n_monday)
			elif get_next_day() == 1:
				bot.send_message(msg.chat.id, c_tuesday)
			elif get_next_day() == 2:
				bot.send_message(msg.chat.id, c_wednesday)
			elif get_next_day() == 3:
				bot.send_message(msg.chat.id, c_thursday)
			elif get_next_day() == 4:
				bot.send_message(msg.chat.id, c_friday)
			else:
				bot.send_message(msg.chat.id, 'Завтра выходной.')
		elif (get_week() % 2 == 1):
			if get_next_day() == 0:
				bot.send_message(msg.chat.id, c_monday)
			elif get_next_day() == 1:
				bot.send_message(msg.chat.id, n_tuesday)
			elif get_next_day() == 2:
				bot.send_message(msg.chat.id, n_wednesday)
			elif get_next_day() == 3:
				bot.send_message(msg.chat.id, n_thursday)
			elif get_next_day() == 4:
				bot.send_message(msg.chat.id, n_friday)
			else:
				bot.send_message(msg.chat.id, 'Завтра выходной.')

	elif msg.text == '/today' or msg.text == '/today@pi_raspisanie_bot':
		if (get_week() % 2 == 0):	
			if get_current_day() == 0:
				bot.send_message(msg.chat.id, c_monday)
			elif get_current_day() == 1:
				bot.send_message(msg.chat.id, c_tuesday)
			elif get_current_day() == 2:
				bot.send_message(msg.chat.id, c_wednesday)
			elif get_current_day() == 3:
				bot.send_message(msg.chat.id, c_thursday)
			elif get_current_day() == 4:
				bot.send_message(msg.chat.id, c_friday)
			else:
				bot.send_message(msg.chat.id, 'Сегодня выходной.')
		elif (get_week() % 2 == 1):
			if get_current_day() == 0:
				bot.send_message(msg.chat.id, n_monday)
			elif get_current_day() == 1:
				bot.send_message(msg.chat.id, n_tuesday)
			elif get_current_day() == 2:
				bot.send_message(msg.chat.id, n_wednesday)
			elif get_current_day() == 3:
				bot.send_message(msg.chat.id, n_thursday)
			elif get_current_day() == 4:
				bot.send_message(msg.chat.id, n_friday)
			else:
				bot.send_message(msg.chat.id, 'Сегодня выходной.')

	elif msg.text == '/traffic' or msg.text == '/traffic@pi_raspisanie_bot':
		bot.send_message(msg.chat.id, 'https://youtu.be/s83yL0mQ7mc')

if __name__ == "__main__":
		bot.polling(none_stop = True)