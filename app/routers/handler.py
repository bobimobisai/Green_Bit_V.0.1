from aiogram import types, Router, F

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from keybords.kb import language, settings

from db import create_data, update_data, delete_data

who_by_img = types.FSInputFile("app/images/who_by.jpg")
settings_img = types.FSInputFile("app/images/settings.jpg")

router = Router()


class Form(StatesGroup):
    user_id = State()
    auth_status = State()
    user_language = State()


# колбек смены языка для не зареганных
@router.callback_query(F.data == "en")
async def lang_en(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(
        text="English language selected💚\nGo in Menu -> /menu",
    )
    await state.update_data(user_language="en")
    await state.set_state(Form.user_language)


@router.callback_query(F.data == "ru")
async def lang_ru(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(
        text="Русский язык выбран💚!\nПерейти в  Menu -> /menu",
    )
    await state.update_data(user_language="ru")
    await state.set_state(Form.user_language)


# колбек смены языка для зареганных
@router.callback_query(F.data == "en_db")
async def lang_en_db(callback: types.CallbackQuery, state: FSMContext):
    try:
        await state.update_data(user_language="en")
        await state.set_state(Form.user_language)
        await update_data(
            column="user_language",
            data="'en'",
            args=(callback.from_user.id,),
        )
    except Exception as e:
        await callback.message.answer(
            text="Ooooh fuck...\nSomething's broken bup beep...\nTry later.",
        )
        print(e)
    else:
        await callback.message.answer(
            text="English language selected💚\nGo in Menu -> /menu",
        )


@router.callback_query(F.data == "ru_db")
async def lang_ru_db(callback: types.CallbackQuery, state: FSMContext):
    try:
        await state.update_data(user_language="ru")
        await state.set_state(Form.user_language)
        await update_data(
            column="user_language",
            data="'ru'",
            args=(callback.from_user.id,),
        )
    except Exception as e:
        await callback.message.answer(
            text="Что то блять сломалось:(\nПопробуйте позже",
        )
        print(e)
    else:
        await callback.message.answer(
            text="Русский язык выбран💚!\nПерейти в  Menu -> /menu",
        )


# колбек для кто вы
@router.callback_query(F.data == "who_you")
async def menu_new_who(callback: types.CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    user_language = user_data.get("user_language")
    try:
        if user_language == "en":
            text_1 = "We are a crypto company <b>GreenBit</b> that aims to support environmentally disruptive lifestyles"
            text_2 = "💁‍Members can earn <b>GreenBit</b> for making environmentally responsible decisions and doing their part to protect the environment."
        elif user_language == "ru":
            text_1 = "Мы - крипто-компания <b>GreenBit</b>, которая направлена на поддержку экологически устойчивого образа жизни"
            text_2 = "💁‍Участники могут зарабатывать <b>GreenBit</b> за принятие экологически ответственных решений и внесение своего вклада в охрану окружающей среды."
    finally:
        await callback.message.answer(
            text=text_1,
            parse_mode="HTML",
        )
        await callback.message.answer(
            text=text_2,
            parse_mode="HTML",
        )


# колбек для того как купить
@router.callback_query(F.data == "how_buy")
async def menu_new_how_buy(callback: types.CallbackQuery, state: FSMContext):
    user_data = await state.get_data()
    user_language = user_data.get("user_language")
    try:
        if user_language == "en":
            text_1 = "To purchase our token, you can click on the <b>Buy</b> button, which will take you to the site for purchase👨‍"
        elif user_language == "ru":
            text_1 = "Для покупки нашего токена, вы можете нажать на кнопку <b>Купить</b>, которая переведет вас на сайт для покупки👨‍"
    finally:
        await callback.message.answer_photo(
            caption=text_1,
            parse_mode="HTML",
            photo=who_by_img,
        )


# смена языка
@router.callback_query(F.data == "s_w")
async def menu_new_s_w(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(
        text="Change language", reply_markup=language(lang="en", size=2)
    )


@router.callback_query(F.data == "s_w_db")
async def menu_new_s_w_db(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(
        text="Change language", reply_markup=language(lang="en_db", size=2)
    )


# регистрация в БД и FSM
@router.callback_query(F.data == "join")
async def join_new_user(callback: types.CallbackQuery, state: FSMContext):
    text_en = "Now you are with us💚! Check out the functionality by going to the Menu! -> /menu"
    text_ru = "Теперь вы с нами💚! Оцените функционал перейдя в Меню! -> /menu"

    user_data = await state.get_data()
    user_language = user_data.get("user_language")

    try:
        # при записи user_id обязательно скобки () и запятая (user_id,) в конце!!!
        user_id = (callback.from_user.id,)
        await create_data(
            data=user_id,
        )
    except Exception as e:
        await callback.message.answer(text="Error :(\nPlease, tyr again")
        print(f"ERROR:{e}")
    else:
        if user_language == "en":
            await callback.message.answer(text=text_en)
        else:
            await callback.message.answer(text=text_ru)
    await update_data(
        column="user_language",
        # при записи языка ползователя обязательно экранировать данные в '' даже если это строка
        data=f"'{user_language}'",
        args=user_id,
    )
    await state.update_data({"auth_status": 1})
    await state.set_state(Form.auth_status)


# Базовой меню верифицированного пользователя
@router.callback_query(F.data == "get_rate")
async def menu_auth_rate(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(text="GRB=100000000$")


@router.callback_query(F.data == "buy_tk")
async def menu_auth_buy_tk(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(text="You  buy 1GRB!")


@router.callback_query(F.data == "walet")
async def menu_auth_walet(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(text="GRWallet\nGRB - 1.0 GRB(100000000BUSD)")


@router.callback_query(F.data == "swap")
async def menu_auth_swap(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(text="Swap!")


@router.callback_query(F.data == "setigs")
async def menu_auth_setigs(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer_photo(
        caption="Settigs",
        photo=settings_img,
        reply_markup=settings(lang="en_set", size=2),
    )


@router.callback_query(F.data == "sub")
async def menu_auth_sub(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer(text="sub!")


@router.callback_query(F.data == "del")
async def dell_account(callback: types.CallbackQuery, state: FSMContext):
    try:
        await delete_data(args=(callback.from_user.id,))
        await state.clear()
    except Exception as e:
        await callback.message.answer(text="Fuck....")
        print(e)
    else:
        await callback.message.answer(text="Account has been deleted.")


@router.callback_query(F.data == "pro")
async def menu_auth_pro(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer_sticker(
        sticker="CAACAgIAAxkBATbJA2W6kH81InpZ96tNjxttywPSGB35AALsGQACi9-5SJcxVjPNzsPdNAQ"
    )
