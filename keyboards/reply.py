from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Информация о нашей компании')
        ],
        [
            KeyboardButton(text='Инвестиционный портфель'),
            KeyboardButton(text='Заработок на партнерах')
        ],
        [

            KeyboardButton(text='Мои активы'),
            KeyboardButton(text='Внутренняя статистика')
        ]],
    resize_keyboard=True
)
update_sum = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text='Пополнить', callback_data='update'),
        InlineKeyboardButton(text='Реинвестировать', callback_data='reinvest')
    ], [InlineKeyboardButton(text='Калькулятор', callback_data='calk'),
        InlineKeyboardButton(text='Вывод средств', callback_data='withdrawal')]
]
)

back_to_inv = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Назад', callback_data='back_to_inv')]])
