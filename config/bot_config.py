from dotenv import dotenv_values

BOT_TOKEN = dotenv_values('.env')['BOT_TOKEN']

DEFAULT_COMMANDS = (
    ('start', 'Регистрация'),
    ('help', 'Доступные команды'),
    ('menu', 'Основное меню')
)