from telebot import types
import telebot
DLineCalc_bot = telebot.TeleBot('TELEGRAMBOT_TOKEN')


num = ''
null = ''
answer = ''
first_msg = None
keyboard = types.InlineKeyboardMarkup(row_width=4)
button_eraser = types.InlineKeyboardButton(text='⬅️', callback_data='erase')
button_cancel = types.InlineKeyboardButton(text='↩️', callback_data='cancel')
button_none = types.InlineKeyboardButton(text='🌸', callback_data='none')
button_comma = types.InlineKeyboardButton(text='⏺️', callback_data='comma')
button_equals = types.InlineKeyboardButton(text='🟰', callback_data='equals')
button_num1 = types.InlineKeyboardButton(text='1⃣', callback_data='num_1')
button_num2 = types.InlineKeyboardButton(text='2⃣', callback_data='num_2')
button_num3 = types.InlineKeyboardButton(text='3⃣', callback_data='num_3')
button_plus = types.InlineKeyboardButton(text='➕', callback_data='plus')
button_num4 = types.InlineKeyboardButton(text='4⃣', callback_data='num_4')
button_num5 = types.InlineKeyboardButton(text='5⃣', callback_data='num_5')
button_num6 = types.InlineKeyboardButton(text='6⃣', callback_data='num_6')
button_minus = types.InlineKeyboardButton(text='➖', callback_data='minus')
button_num7 = types.InlineKeyboardButton(text='7⃣', callback_data='num_7')
button_num8 = types.InlineKeyboardButton(text='8⃣', callback_data='num_8')
button_num9 = types.InlineKeyboardButton(text='9⃣', callback_data='num_9')
button_multiply = types.InlineKeyboardButton(text='✖️', callback_data='multiply')
button_num0 = types.InlineKeyboardButton(text='0⃣', callback_data='num_0')
button_division = types.InlineKeyboardButton(text='➗', callback_data='division')
keyboard.row(button_cancel, button_division, button_multiply, button_eraser)
keyboard.row(button_num7, button_num8, button_num9, button_minus)
keyboard.row(button_num4, button_num5, button_num6, button_plus)
keyboard.row(button_num1, button_num2, button_num3, button_none)
keyboard.row(button_none, button_num0, button_comma, button_equals)


@DLineCalc_bot.message_handler(commands=['start'])  # noqa: E302
def start(message):
    global first_msg
    key = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    key.add(types.InlineKeyboardButton(text="Калькулятор", callback_data='calc'))
    msg = (f"Привет, <b>{message.from_user.first_name}</b>!\nЯ Бот-калькулятор\n"
           f"Я умею складывать, вычитать, умножать и делить. :)")
    first_msg = DLineCalc_bot.send_message(message.chat.id, msg, parse_mode='html', reply_markup=key)
    return first_msg


@DLineCalc_bot.message_handler(content_types=['text'])
def calc(message):
    if message.text == "Калькулятор":
        DLineCalc_bot.send_message(message.from_user.id, "0", reply_markup=keyboard)


@DLineCalc_bot.callback_query_handler(func=lambda call: True)
def callback(call):
    global null, num
    if call.message:
        if call.data == 'none':
            DLineCalc_bot.answer_callback_query(call.id)
        if call.data == 'cancel':
            num = ''
            DLineCalc_bot.answer_callback_query(call.id)
        if call.data == 'comma':
            num += '.'
            DLineCalc_bot.answer_callback_query(call.id)
        if call.data == 'num_1':
            num += '1'
            DLineCalc_bot.answer_callback_query(call.id)
        elif call.data == 'num_2':
            num += '2'
            DLineCalc_bot.answer_callback_query(call.id)
        elif call.data == 'num_3':
            num += '3'
            DLineCalc_bot.answer_callback_query(call.id)
        elif call.data == 'num_4':
            num += '4'
            DLineCalc_bot.answer_callback_query(call.id)
        elif call.data == 'num_5':
            num += '5'
            DLineCalc_bot.answer_callback_query(call.id)
        elif call.data == 'num_6':
            num += '6'
            DLineCalc_bot.answer_callback_query(call.id)
        elif call.data == 'num_7':
            num += '7'
            DLineCalc_bot.answer_callback_query(call.id)
        elif call.data == 'num_8':
            num += '8'
            DLineCalc_bot.answer_callback_query(call.id)
        elif call.data == 'num_9':
            num += '9'
            DLineCalc_bot.answer_callback_query(call.id)
        elif call.data == 'num_0':
            num += '0'
            DLineCalc_bot.answer_callback_query(call.id)
        elif call.data == 'plus':
            num += str("+")
            DLineCalc_bot.answer_callback_query(call.id)
        elif call.data == 'minus':
            num += str("-")
            DLineCalc_bot.answer_callback_query(call.id)
        elif call.data == 'multiply':
            num += str("*")
            DLineCalc_bot.answer_callback_query(call.id)
        elif call.data == 'division':
            num += str("/")
            DLineCalc_bot.answer_callback_query(call.id)
        elif call.data == 'equals':
            if num == '':
                num = '0'
                DLineCalc_bot.answer_callback_query(call.id)
            else:
                num = eval(num)
                DLineCalc_bot.answer_callback_query(call.id)
        elif call.data == 'erase':
            if num != '':
                num = num[:len(num)-1]
                DLineCalc_bot.answer_callback_query(call.id)
        if num != null:
            if num == '':
                DLineCalc_bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='0',
                                                reply_markup=keyboard)
            else:
                DLineCalc_bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text=num,
                                                reply_markup=keyboard)
            DLineCalc_bot.answer_callback_query(call.id)
            null = num


DLineCalc_bot.infinity_polling()
