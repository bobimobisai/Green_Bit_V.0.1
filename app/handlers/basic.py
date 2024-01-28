from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile
from filtres.chat_type import ChatTypeFilter
from keyboards.kb import get_builder, buy, menu, buld_new
from db import read_data, create_data


router = Router()
router.message.filter(ChatTypeFilter(chat_type=["private"]))
start_photo = FSInputFile("app/images/image1.jpg")


@router.message(Command("start"))
async def my_answer(message: Message):
    """
    автоматически определяется язык, нужно адаптировать кноки...
    нужно сделать либо автоматическое либо фиксированное
    определение языка, и провести тесты
    """
    get_id = await read_data(args=(message.from_user.id,))
    if get_id == []:
        await message.answer_photo(
            photo=start_photo,
            caption=f"🌿GreenBit приветствует вас👋\n. Вы у нас впервые, хотите присоединиться?\n Нажмите ⬇🆕\n Ваш язык - {message.from_user.language_code}",
            reply_markup=buld_new(),
        )
    elif message.from_user.id == get_id[0][0]:
        await message.answer_photo(
            photo=start_photo,
            caption="🌿GreenBit снова рад вас видеть👋!",
            reply_markup=get_builder(),
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
