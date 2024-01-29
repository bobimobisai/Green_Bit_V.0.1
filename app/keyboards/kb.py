from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_builder_user():
    bi = InlineKeyboardBuilder()
    bi.add(types.InlineKeyboardButton(text="👥Кто вы", callback_data="who you"))
    bi.add(types.InlineKeyboardButton(text="💵Как купить", callback_data="how buy"))
    bi.add(
        types.InlineKeyboardButton(
            text="🖥Наш сай", url="https://trump-token.company.site"
        )
    )
    bi.add(types.InlineKeyboardButton(text="➡️Меню", callback_data="menu"))
    bi.add(types.InlineKeyboardButton(text="Swith language", callback_data="sw"))
    bi.add(types.InlineKeyboardButton(text="Join✅", callback_data="new"))
    bi.adjust(2)
    return bi.as_markup()


def get_builder_auth_user():
    bi = InlineKeyboardBuilder()
    bi.add(types.InlineKeyboardButton(text="👥Кто вы", callback_data="who you"))
    bi.add(types.InlineKeyboardButton(text="💵Как купить", callback_data="how buy"))
    bi.add(
        types.InlineKeyboardButton(
            text="🖥Наш сай", url="https://trump-token.company.site"
        )
    )
    bi.add(types.InlineKeyboardButton(text="➡️Меню", callback_data="menu"))
    bi.add(types.InlineKeyboardButton(text="Настройки", callback_data="setings"))
    bi.add(types.InlineKeyboardButton(text="Сменить язык", callback_data="sw"))
    bi.adjust(2)
    return bi.as_markup()


def get_builder_auth_user_en():
    bi = InlineKeyboardBuilder()
    bi.add(types.InlineKeyboardButton(text="👥Who you are?", callback_data="who you"))
    bi.add(types.InlineKeyboardButton(text="💵How to buy?", callback_data="how buy"))
    bi.add(
        types.InlineKeyboardButton(
            text="🖥Website", url="https://trump-token.company.site"
        )
    )
    bi.add(types.InlineKeyboardButton(text="Menu", callback_data="menu"))
    bi.add(types.InlineKeyboardButton(text="Settings", callback_data="settings"))
    bi.add(types.InlineKeyboardButton(text="Swith language", callback_data="sw"))
    bi.adjust(2)
    return bi.as_markup()


def buy():
    buy = InlineKeyboardBuilder()
    buy.add(
        types.InlineKeyboardButton(text="⚡️Купить", url="https://pancakeswap.finance/")
    )
    buy.adjust(1)
    return buy.as_markup()


def menu():
    menu = InlineKeyboardBuilder()
    menu.add(types.InlineKeyboardButton(text="📊Курс валют", callback_data="trade"))
    menu.add(types.InlineKeyboardButton(text="⬅️Назад", callback_data="back"))
    menu.adjust(4)
    return menu.as_markup()


def join_en():
    join = InlineKeyboardBuilder()
    join.add(types.InlineKeyboardButton(text="Join✅", callback_data="join_lang"))
    join.adjust()
    return join.as_markup()


def language():
    lang = InlineKeyboardBuilder()
    lang.add(types.InlineKeyboardButton(text="EN", callback_data="en"))
    lang.add(types.InlineKeyboardButton(text="RU", callback_data="ru"))
    lang.adjust(2)
    return lang.as_markup()
