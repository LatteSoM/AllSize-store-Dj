# import telegram_send
#
#
# async def send_order():
#     await telegram_send.send(messages=['успех'])
import requests


def saaaaaad(message):
    tok = '6334529129:AAH5JseCYY8l4eEIPUilwTA3BjPDtmo6zAc'
    u_id = '420309682'
    u_idkol = '1450087163'
    url_t = f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={u_idkol}&parse_mode=MarkDown&text={message}'
    url = f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={u_id}&parse_mode=MarkDown&text={message}'
    requests.get(url_t)
    requests.get(url)



# from telegram import Update
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
#
#
# # Обработчик команды /start
# def start(update: Update, context: CallbackContext) -> None:
#     update.message.reply_text("Привет, я бот который будет отправлять тебе заказы которые пользователи сделали на твоем сайте. Введи свой логин:")
#
#
# # Обработчик текстовых сообщений
# def text_message(update: Update, context: CallbackContext) -> None:
#     if 'login' not in context.user_data:  # Если логин еще не введен
#         context.user_data['login'] = update.message.text  # Сохраняем логин
#         update.message.reply_text("Теперь введи свой пароль:")
#     elif 'password' not in context.user_data:  # Если пароль еще не введен
#         context.user_data['password'] = update.message.text  # Сохраняем пароль
#         update.message.reply_text("Регистрация успешна! Теперь ты можешь получать заказы.")
#
#
# def main() -> None:
#     # Создаем объект Updater и передаем ему токен вашего бота
#     updater = Updater("YOUR_BOT_TOKEN")
#
#     # Получаем объект диспетчера из updater
#     dispatcher = updater.dispatcher
#
#     # Добавляем обработчики команды /start и текстовых сообщений
#     dispatcher.add_handler(CommandHandler("start", start))
#     dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, text_message))
#
#     # Запускаем бота
#     updater.start_polling()
#     updater.idle()
#
#
# if __name__ == '__main__':
#     main()