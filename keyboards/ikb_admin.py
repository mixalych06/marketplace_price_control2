from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def gen_markup_category_tariff():
    """Меню после нажатия тарифы для админа"""
    return InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text=f'Активные', callback_data=f'tariff_active:1'),
                          InlineKeyboardButton(text=f'Не активные', callback_data=f'tariff_active:0')],
                         [InlineKeyboardButton(text=f'Добавить тариф', callback_data=f'add_tariff')]])


async def gen_markup_cancel_fsm():
    """создаёт кнопуе отмены FSM"""
    return InlineKeyboardMarkup(
        inline_keyboard=[[InlineKeyboardButton(text=f'Отмена', callback_data=f'cancelFSM')]])


async def gen_markup_menu_tariff(tariff_id, active_index=1):
    """Клавиатура для тарифа. active_index=1 (активные тарифы), active_index=0 (не активные тарифы)
    передаёт в callback id тарифа и номер операции (1-включить, 0-выключить, 2-удалить)"""
    if active_index == 1:
        return InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text=f'Отключить', callback_data=f'tar_action:{tariff_id}:0'),
                              InlineKeyboardButton(text=f'Удалить', callback_data=f'tar_action:{tariff_id}:2')]])
    elif active_index == 0:
        return InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text=f'Включить', callback_data=f'tar_action:{tariff_id}:1'),
                              InlineKeyboardButton(text=f'Удалить', callback_data=f'tar_action:{tariff_id}:2')]])


async def gen_markup_ok_pay(user_id):
    """Создаёт инлайн кнопки"""
    return InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=f'Пополнить баланс', callback_data=f'ok_pay:{user_id}')],
        [InlineKeyboardButton(text=f'Отмена оплаты', callback_data=f'no_pay:{user_id}')]])
