from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_builder():
    bi = InlineKeyboardBuilder()
    bi.add(types.InlineKeyboardButton(text="👥Кто вы", callback_data="who you"))
    bi.add(types.InlineKeyboardButton(text="💵Как купить", callback_data="how buy"))
    bi.add(
        types.InlineKeyboardButton(
            text="🖥Наш сай", url="https://trump-token.company.site"
        )
    )
    bi.add(types.InlineKeyboardButton(text="➡️Меню", callback_data="menu"))
    bi.adjust(2)
    return bi.as_markup()


def buld_new():
    new = InlineKeyboardBuilder()
    new.add(types.InlineKeyboardButton(text="New", callback_data="new"))
    new.adjust(1)
    return new.as_markup()


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
