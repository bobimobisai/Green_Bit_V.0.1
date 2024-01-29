from typing import List
from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from filtres.chat_type import ChatTypeFilter
from keyboards.kb import (
    get_builder_user,
    buy,
    menu,
    get_builder_auth_user,
    language,
    get_builder_auth_user_en,
    join_en,
)
from db import read_data, create_data, update_data


router = Router()
router.message.filter(ChatTypeFilter(chat_type=["private"]))
start_photo = FSInputFile("app/images/image1.jpg")


@router.message(Command("start"))
async def my_answer(message: Message):
    text_auth_ru = "🌿GreenBit снова рад вас видеть👋!"
    text_auth_en = "🌿GreenBit glad to see you again👋!"
    user_data = await read_data(args=(message.from_user.id,))
    if user_data == []:
        await message.answer_photo(
            photo=start_photo,
            caption="🌿GreenBit приветствует вас👋!\nВы у нас впервые, хотите присоединиться в телеграмм?\nНажмите Join✅\nSwith language 🔤",
            reply_markup=get_builder_user(),
        )
    elif message.from_user.id == user_data[0][0] and user_data[0][6] == "ru":
        await message.answer_photo(
            photo=start_photo,
            caption=text_auth_ru,
            reply_markup=get_builder_auth_user(),
        )
    elif message.from_user.id == user_data[0][0] and user_data[0][6] == "en":
        await message.answer_photo(
            photo=start_photo,
            caption=text_auth_en,
            reply_markup=get_builder_auth_user_en(),
        )
    elif message.from_user.id == user_data[0][0]:
        await message.answer_photo(
            photo=start_photo,
            caption=text_auth_en,
            reply_markup=get_builder_auth_user_en(),
        )


@router.callback_query(F.data == "who you")
async def who(callback: types.CallbackQuery):
    await callback.message.answer(
        text="Мы - крипто-компания <b>GreenBit</b>, которая направлена на поддержку экологически устойчивого образа жизни💚",
        parse_mode="HTML",
    )
    await callback.message.answer(
        tetx="💁‍Участники могут зарабатывать <b>GreenBit</b> за принятие экологически ответственных решений и внесение своего вклада в охрану окружающей среды.",
        parse_mode="HTML",
    )


@router.callback_query(F.data == "how buy")
async def how(callback: types.CallbackQuery):
    await callback.message.answer(
        text="Для покупки нашего токена, вы можете нажать на кнопку <b>Купить</b>, которая переведет вас на сайт для покупки👨‍",
        parse_mode="HTML",
        reply_markup=buy(),
    )


@router.callback_query(F.data == "menu")
async def menu_answ(callback: types.CallbackQuery):
    await callback.message.answer(text="Добро пожаловать в меню!🟢", reply_markup=menu())


@router.callback_query(F.data == "trade")
async def kurs_otvet(callback: types.CallbackQuery):
    await callback.answer(
        text="Скоро тут появиться курс валюты!💚",
    )


@router.callback_query(F.data == "back")
async def back_to(callback: types.CallbackQuery):
    await callback.message.answer(
        text="Для возвращения в главное меню, нажмите /start 🔆"
    )


@router.callback_query(F.data == "new")
async def set_new_user(callback: types.CallbackQuery):
    await create_data(data=(callback.from_user.id,))
    await callback.message.answer(text="Поздравляю! Теперь вы с нами! Нажмите /start")


@router.callback_query(F.data == "join_lang")
async def set_new_user_lang(callback: types.CallbackQuery):
    await create_data(data=(callback.from_user.id,))
    await update_data(
        column="user_language",
        data="'en'",
        args=(callback.from_user.id,),
    )
    await callback.message.answer(
        text="Congratulations! Now you are with us! Click /start"
    )


@router.callback_query(F.data == "sw")
async def sw_lang(callback: types.CallbackQuery):
    await callback.message.answer(text="Choose language!", reply_markup=language())


@router.callback_query(F.data == "en")
async def sw_en(callback: types.CallbackQuery):
    user_data = await read_data(args=(callback.from_user.id,))
    if user_data == []:
        await callback.message.answer(
            text="Please Join✅ to change language!", reply_markup=join_en()
        )
    else:
        await update_data(
            column="user_language",
            data="'en'",
            args=(callback.from_user.id,),
        )
        await callback.message.answer(
            text="Great, the language has been successfully changed to EN!\nClick /start"
        )


@router.callback_query(F.data == "ru")
async def sw_ru(callback: types.CallbackQuery):
    user_data = await read_data(args=(callback.from_user.id,))
    if user_data == []:
        await callback.message.answer(
            text="Пожалуйста присоединитесь -> Join✅, для смены Языка!",
            reply_markup=get_builder_user(),
        )
    await update_data(
        column="user_language",
        data="'ru'",
        args=(callback.from_user.id,),
    )
    await callback.message.answer(
        text="Отлично, язык успешно изменен на RU!\nНажмите /start"
    )
