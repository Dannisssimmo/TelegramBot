from aiogram import types, Router, F
from aiogram.filters import CommandStart
from keyboards import reply

from main_func import data

user_private_router = Router()


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer(data.start_message, reply_markup=reply.start_kb)


@user_private_router.message(F.text == 'Инвестиционный портфель')
async def mes(message: types.Message):
    await message.answer(data.inform_about_inv, reply_markup=reply.update_sum)


@user_private_router.message(F.text == 'Заработок на партнерах')
async def mes(message: types.Message):
    await message.answer(data.partners)


@user_private_router.message(F.text == 'Мои активы')
async def mes(message: types.Message):
    await message.answer(data.my_balance)


@user_private_router.message(F.text == 'Внутренняя статистика')
async def mes(message: types.Message):
    await message.answer(data.statistics)


@user_private_router.message(F.text == 'Информация о нашей компании')
async def mes(message: types.Message):
    await message.answer(data.about_us)


@user_private_router.callback_query(F.data == "update")
async def mes(query: types.CallbackQuery):
    await query.message.edit_text(text=data.about_update, reply_markup=reply.back_to_inv)


@user_private_router.callback_query(F.data == 'back_to_inv')
async def mes(query: types.CallbackQuery):
    await query.message.edit_text(text=data.inform_about_inv, reply_markup=reply.update_sum)


@user_private_router.callback_query(F.data == 'reinvest')
async def mes(query: types.CallbackQuery):
    await query.message.edit_text(text=data.zagl, reply_markup=reply.back_to_inv)


@user_private_router.callback_query(F.data == 'calk')
async def calk(query: types.CallbackQuery):
    await query.message.edit_text(text=data.zagl, reply_markup=reply.back_to_inv)


@user_private_router.callback_query(F.data == 'withdrawal')
async def mes(query: types.CallbackQuery):
    await query.message.edit_text(text=data.zagl, reply_markup=reply.back_to_inv)


@user_private_router.message(F.photo)
async def mes(message: types.Message):
    await message.answer(
        text='Мы получили ваш скриншон, он отправлен на проверку администратору, в скором времени мы уведомим вас о '
             'результате работы')
    await message.copy_to(chat_id=data.my_id, caption=f'@{message.from_user.username}')

