from telebot import types
import telebot
DLineCalc_bot = telebot.TeleBot('7776091392:AAE4_c9LL0kEeAadkNIpkMVNeopQ4yY4mZs')


first_msg = None


@DLineCalc_bot.message_handler(commands=['start'])  # noqa: E302
def start(message):
    global first_msg
    key = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    key.add(types.InlineKeyboardButton(text="Калькулятор", callback_data='calc'))
    msg = (f"Привет, <b>{message.from_user.first_name}</b>!\nЯ Бот-калькулятор\n"
           f"Я умею складывать, вычитать, умножать и делить. :)")
    first_msg = DLineCalc_bot.send_message(message.chat.id, msg, parse_mode='html', reply_markup=key)
    return first_msg

