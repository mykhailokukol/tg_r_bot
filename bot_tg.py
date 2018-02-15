chet = u"Понедельник:\n1. Право (Лекция)\n2. Право\n\nВторник:\n1.\n2. БД (Лаб) (Малахов)\n3. ЭМПИ (Лаб) (Егошина)\n\nСреда:\n1. \n2. БЖД (Лаб)\n3. ТИМ (Лаб) (Шнайдер)\n4. PWEBД (Лаб) (Северин)\n\nЧетверг:\n1. ПМ (Лаб) (Ларин)\n2. ТИМ (Лекция) (Шнайдер)\n3. \n4. Физ-ра\n\nПятница:\n1.\n2. \n3. БД (Малахов)"
nechet = u"Понедельник:\n1. Право (Лекция)\n\nВторник:\n1.\n2. БД (Лаб) (Малахов)\n3. ЭМПИ (Лаб) (Егошина)\n4. ЭМПИ (Лекция) (Егошина)\n\nСреда:\n1. \n2. БЖД (Лекция)\n3. ТИМ (Лаб) (Шнайдер)\n4. PWEBД (Лаб) (Северин)\n\nЧетверг:\n1. ПМ (Лаб) (Ларин)\n2. ТИМ (Лекция) (Шнайдер)\n3. ПМ (Лекция) (Ларин)\n4. Физ-ра\n\nПятница:\n1.\n2. \n3. БД (Малахов)\n4. PWEBД (Лекция) (Северин)"
import telebot as tb
import datetime

token = "468712981:AAFHuD1rOuW31VYZOZx_qwXNgydpn3_DgFo"

def get_week():
	date = datetime.datetime.now()
	week = date.isocalendar()[1]
	return int(week)

bot = tb.TeleBot(token)

@bot.message_handler(commands=['raspisanie'])
def send_msg(msg):
	if (get_week() % 2 == 0):
		bot.send_message(msg.chat.id, chet)
	elif (get_week() % 2 == 1):
		bot.send_message(msg.chat.id, nechet)
	else:
		bot.send_message(msg.chat.id, "Week == 0")	

if __name__ == "__main__":
		bot.polling(none_stop = True)