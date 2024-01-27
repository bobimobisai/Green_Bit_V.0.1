from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from app.filtres.chat_type import ChatTypeFilter
from app.keyboards.kb import get_builder, buy, menu

db_user = "tets_1"

router = Router()
router.message.filter(ChatTypeFilter(chat_type=["private"]))
start_photo = FSInputFile("images/image1.jpg")



@router.message(Command("start"))
async def my_answer(message: Message):
    await message.answer_photo(photo=start_photo,
        caption="🌿GreenBit приветствует вас👋. Что будем делать?",
        reply_markup=get_builder(),
    )
    #us_id = message.from_user.id
    #us_name = message.from_user.first_name
    #user_link = message.from_user.username
    #await db_user(user_id=us_id, user_name=us_name, user_link=user_link)


@router.callback_query(F.data == "who you")
async def who(callback: types.CallbackQuery):
    await callback.message.answer(
        "Мы - крипто-компания <b>GreenBit</b>, которая направлена на поддержку экологически устойчивого образа жизни💚",
        parse_mode="HTML",
    )
    await callback.message.answer(
        "💁‍Участники могут зарабатывать <b>GreenBit</b> за принятие экологически ответственных решений и внесение своего вклада в охрану окружающей среды.",
        parse_mode="HTML",
    )


@router.callback_query(F.data == "how buy")
async def how(callback: types.CallbackQuery):
    await callback.message.answer(
        "Для покупки нашего токена, вы можете нажать на кнопку <b>Купить</b>, которая переведет вас на сайт для покупки👨‍",
        parse_mode="HTML",
        reply_markup=buy(),
    )

@router.callback_query(F.data == "menu")
async def menu_answ(callback: types.CallbackQuery):
    await callback.message.answer(
        "Добро пожаловать в меню!🟢",
        reply_markup=menu()
    )

@router.callback_query(F.data == "trade")
async def kurs_otvet(callback: types.CallbackQuery):
    await callback.answer(
        "Скоро тут появиться курс валюты!💚",
    )

@router.callback_query(F.data == "back")
async def back_to(callback: types.CallbackQuery):
    await callback.message.answer("Для возвращения в главное меню, нажмите /start 🔆")