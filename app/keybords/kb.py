from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import BotCommand

class Menu:
    def __init__(self, lang, size):
        self.lang = lang
        self.menu = InlineKeyboardBuilder()
        self.size = size

    def add_button(self, text, callback_data):
        self.menu.add(
            types.InlineKeyboardButton(text=text, callback_data=callback_data)
        )

    def add_url_button(self, text, url):
        self.menu.add(types.InlineKeyboardButton(text=text, url=url))

    def get_size(self):
        self.menu.adjust(self.size)

    def as_markup(self):
        return self.menu.as_markup()


class EnglishUserNewMenu(Menu):
    def __init__(self, size):
        super().__init__("en_user_new", size=size)
        self.add_button(text="👥Who you", callback_data="who_you")
        self.add_button(text="💵Buy coin tokens", callback_data="how_buy")
        self.add_url_button(text="🖥Our website", url="https://trump-token.company.site")
        self.add_button(text="Switch language", callback_data="s_w")
        self.add_button(text="Join✅", callback_data="join")
        self.get_size()


class RussianUserNewMenu(Menu):
    def __init__(self, size):
        super().__init__("ru_user_new", size=size)
        self.add_button(text="👥Кто вы", callback_data="who_you")
        self.add_button(text="💵Как купить", callback_data="how_buy")
        self.add_url_button(text="🖥Наш сайт", url="https://trump-token.company.site")
        self.add_button(text="Сменить язык", callback_data="s_w")
        self.add_button(text="Присоединиться✅", callback_data="join")
        self.get_size()


class EnglishUserAuthMenu(Menu):
    def __init__(self, size):
        super().__init__("en_user_auth", size=size)
        self.add_button(text="Token rate", callback_data="get_rate")
        self.add_button(text="Buy a token", callback_data="buy_tk")
        self.add_button(text="Wallet", callback_data="walet")
        self.add_button(text="Token swap", callback_data="swap")
        self.add_url_button(text="🖥Our website", url="https://trump-token.company.site")
        self.add_button(text="Settigs", callback_data="setigs")
        self.get_size()


class RussianUserAuthMenu(Menu):
    def __init__(self, size):
        super().__init__("ru_user_auth", size=size)
        self.add_button(text="Курс токена", callback_data="get_rate")
        self.add_button(text="Купить токен", callback_data="buy_tk")
        self.add_button(text="Кошелек", callback_data="walet")
        self.add_button(text="Обмен токенов", callback_data="swap")
        self.add_url_button(text="🖥Наш сайт", url="https://trump-token.company.site")
        self.add_button(text="Настройки", callback_data="setigs")
        self.get_size()


class Language(Menu):
    def __init__(self, size):
        super().__init__(lang="en", size=size)
        self.add_button(text="EN", callback_data="en")
        self.add_button(text="RU", callback_data="ru")


class Language_Auth(Menu):
    def __init__(self, size):
        super().__init__(lang="en_db", size=size)
        self.add_button(text="EN", callback_data="en_db")
        self.add_button(text="RU", callback_data="ru_db")


class Settigs(Menu):
    def __init__(self, size):
        super().__init__(lang="en_set", size=size)
        self.add_button(text="Subscribe", callback_data="sub")
        self.add_button(text="Change language", callback_data="s_w_db")
        self.add_button(text="Delete account...", callback_data="del")
        self.add_button(text="Pro version", callback_data="pro")
        self.get_size()


def language(lang: str, size: int):
    if lang == "en":
        menu_instance = Language(size=size)
    elif lang == "en_db":
        menu_instance = Language_Auth(size=size)
    else:
        menu_instance = Language(size=size)
    return menu_instance.as_markup()


def menu(lang: str = "en_user_new", size: int = 2):
    if lang == "en_user_new":
        menu_instance = EnglishUserNewMenu(size=size)

    elif lang == "ru_user_new":
        menu_instance = RussianUserNewMenu(size=size)

    elif lang == "en_user_auth":
        menu_instance = EnglishUserAuthMenu(size=size)

    elif lang == "ru_user_auth":
        menu_instance = RussianUserAuthMenu(size=size)

    return menu_instance.as_markup()


def settings(lang: str, size: int = 2):
    if lang == "en_set":
        menu_instance = Settigs(size)
    else:
        menu_instance = Settigs(size)

    return menu_instance.as_markup()
