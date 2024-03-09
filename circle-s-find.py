from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import math

# Функция для обработки команды /start
def start(update, context):
    update.message.reply_text('Привет! Я бот для вычисления площади круга. Просто отправь мне радиус круга.')

# Функция для обработки текстовых сообщений с радиусом круга
def calculate_area(update, context):
    try:
        radius = float(update.message.text)

        if radius > 0:
            area = math.pi * radius**2
            update.message.reply_text(f'Площадь круга с радиусом {radius} равна {area:.2f}')
        else:
            update.message.reply_text('Ошибка: Радиус должен быть положительным числом.')
    except ValueError:
        update.message.reply_text('Ошибка: Пожалуйста, введите число в качестве радиуса.')

def main():
    # Создаем объект Updater и передаем в него токен вашего бота
    updater = Updater("YOUR_TELEGRAM_BOT_TOKEN", use_context=True)

    # Получаем диспетчер для регистрации обработчиков
    dp = updater.dispatcher

    # Регистрируем обработчик команды /start
    dp.add_handler(CommandHandler("start", start))

    # Регистрируем обработчик для текстовых сообщений
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, calculate_area))

    # Запускаем бота
    updater.start_polling()

    # Останавливаем бота при нажатии Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()
