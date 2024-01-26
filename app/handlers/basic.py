from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.types import Message
from filtres.chat_type import ChatTypeFilter
from keyboards.kb import get_builder, buy

db_user = "tets_1"

router = Router()
router.message.filter(ChatTypeFilter(chat_type=["private"]))


@router.message(Command("start"))
async def my_answer(message: Message):
    await message.answer(
        "🌿GreenBit приветствует вас👋. Что вы хотите сделат?",
        reply_markup=get_builder(),
    )
    us_id = message.from_user.id
    us_name = message.from_user.first_name
    user_link = message.from_user.username
    await db_user(user_id=us_id, user_name=us_name, user_link=user_link)


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
async def who_2(callback: types.CallbackQuery):
    await callback.message.answer(
        "Для покупки нашего токена, вы можете нажать на кнопку <b>Купить</b>, которая переведет вас на сайт для покупки👨‍",
        parse_mode="HTML",
        reply_markup=buy(),
    )
