from aiogram.filters import Command, CommandStart
from aiogram.types import Message, FSInputFile, CallbackQuery
from aiogram import Router, F, types
from keybords.kb import menu, language
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from routers.handler import router, Form

from db import read_data

start_photo = FSInputFile("app/images/image1.jpg")
auth_user_menu = FSInputFile("app/images/auth_user.jpg")


@router.message(CommandStart())
async def command_st(message: Message, state: FSMContext):
    await state.clear()
    # запрос данных пользователя из БД
    user_data_db = await read_data((message.from_user.id,))

    text_en_st = "🌿GreenBit welcomes you👋!\nChoose language!"
    # Если пользоваьель новый -> установка языка в FSM
    if user_data_db == []:
        await message.answer_photo(
            photo=start_photo,
            caption=text_en_st,
            reply_markup=language(lang="en", size=2),
        )
    # если пользователь зареганый
    else:
        # заносим все данные в FSM
        await state.update_data(
            {
                "user_id": user_data_db[0][0],
                "auth_status": 1,
                "user_language": user_data_db[0][6],
            }
        )
        await state.set_state(Form.user_id)
        await state.set_state(Form.auth_status)
        await state.set_state(Form.user_language)
        await command_menu(message, state)


@router.message(Command("menu"))
async def command_menu(message: Message, state: FSMContext):
    text_en_st = "🌿GreenBit welcomes you👋!"
    text_ru_st = "🌿GreenBit приветствует вас👋!"
    # подгружаем данные из FSM
    user_data = await state.get_data()
    user_language = user_data.get("user_language")
    user_auth = user_data.get("auth_status")
    # запрос данных пользователя из БД
    user_data_db = await read_data((message.from_user.id,))
    # если пользователь новый
    if user_auth is None and user_data_db == []:
        if user_language == "en":
            await message.answer_photo(
                photo=start_photo,
                caption=text_en_st,
                reply_markup=menu(lang="en_user_new", size=2),
            )
        else:
            await message.answer_photo(
                photo=start_photo,
                caption=text_ru_st,
                reply_markup=menu(lang="ru_user_new", size=2),
            )
    # если уже зарегистрированный
    elif user_auth == 1 or user_data_db[0][0] != []:
        if user_language == "en" or user_data_db[0][6] == "en":
            await message.answer_photo(
                photo=auth_user_menu,
                caption=text_en_st,
                reply_markup=menu(lang="en_user_auth", size=2),
            )
        else:
            await message.answer_photo(
                photo=auth_user_menu,
                caption=text_ru_st,
                reply_markup=menu(lang="ru_user_auth", size=2),
            )


@router.message(Command("hellp"))
async def command_help(message: Message):
    await message.answer(text="Help Menu\n-Admin link\nhttps://t.me/petran_dev")
