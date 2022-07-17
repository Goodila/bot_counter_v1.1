import telebot
import json
token = "5259442386:AAGZjTZP-O_2ajDvx9gY35nFDV_6wX-OEPo"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def bot_message_handler(message):
    bot.send_message(message.chat.id, str(message.chat.id) + " тесттовое сообщение при START!!!!")


@bot.message_handler(commands=["zaebat_peska"])
def bot_message_handler(message):
    for i in range(20):
        bot.send_message(361570583, "  ЗАЕБЕМ ПЕСКА  "*10)


@bot.message_handler(commands=["count"])
def bot_message_handler(message):
    dict1 = json.load(open("dict_counter.txt", "r"))

    #dict1 = json.load(open("dict_counter.txt", "r"))
    res = []
    result = ""
    D = dict1.copy()
    lst_v = list(D[str(message.chat.id)].values())

    for i in range(7):
        res.append(lst_v.index(max(lst_v)))
        result += f"{i+1}. {list(D[str(message.chat.id)].items())[lst_v.index(max(lst_v))]}\n"
        lst_v[lst_v.index(max(lst_v))] = 0
    result += f'\n всего уникальных слов было использовано - {len(dict1[str(message.chat.id)])}'

    bot.send_message(message.chat.id, f"самые часто используемые слова в вашей беседе это:\n {result}")


@bot.message_handler(func=lambda message: message)
def bot_message_handler(message):
    lst = message.text.split(' ')
    dict1 = json.load(open("dict_counter.txt", "r"))

    for i in lst:
        if i.strip('.,?!-_') not in ['а','и','но','в','это', 'если','без','с','как','за','до','я','ты','мы', 'все','всё','лол', 'на', 'не', 'к', '','Путин','путин','к','что','чтобы','у','нас']:
            try:
                if i.strip('.,?!-_') not in dict1[str(message.chat.id)]:
                    dict1[str(message.chat.id)][i.strip('.,?!-_')] = 1
                    json.dump(dict1, open("dict_counter.txt", "w"), indent=4, ensure_ascii=False)
                else:
                    dict1[str(message.chat.id)][i.strip('.,?!-_')] += 1
                    json.dump(dict1, open("dict_counter.txt", "w"), indent=4, ensure_ascii=False)
            except KeyError:
                dict1[str(message.chat.id)] = {}
                dict1[str(message.chat.id)][i.strip('.,?!-_')] = 1
                json.dump(dict1, open("dict_counter.txt", "w"), indent=4, ensure_ascii=False)


@bot.message_handler(func=lambda message: message.text in ["ТЕСТ"])
def bot_message_handler(message):
    print('принял сообщение в группе')
    bot.send_message(message.from_user.id, " тесттовое сообщение при ТЕСТЕ")
    bot.send_message(message.chat.id, " тесттовое сообщение при ТЕСТЕ!!!!")

bot.infinity_polling()
