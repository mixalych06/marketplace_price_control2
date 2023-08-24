from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from keyboards.kb_other import bt_my_stock



bt_number_users: KeyboardButton = KeyboardButton(text='Пользователи')
bt_getting_all: KeyboardButton = KeyboardButton(text='Выгрузка')
bt_add_admin: KeyboardButton = KeyboardButton(text='Добавить админа')
bt_add_blacklist: KeyboardButton = KeyboardButton(text='Добавить в ЧС')

kb_main_admin = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[bt_number_users, bt_getting_all],
                                                                    [bt_add_admin, bt_add_blacklist, bt_my_stock]])



