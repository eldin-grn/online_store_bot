from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.database.requests import get_categories, get_products

main_keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Catalog')],
    [KeyboardButton(text='Contacts')]
], resize_keyboard=True, input_field_placeholder='Choose from below')


async def categories_b():
    categories_keyboard = InlineKeyboardBuilder()
    categories = await get_categories()

    for category in categories:
        categories_keyboard.add(InlineKeyboardButton(
            text=category.name,
            callback_data=f'category={category.id}'
        ))
    return categories_keyboard.adjust(2).as_markup()


async def products_b(category_id):
    products_keyboard = InlineKeyboardBuilder()
    products = await get_products(category_id)

    for product in products:
        products_keyboard.add(InlineKeyboardButton(
            text=product.name,
            callback_data=f'product={product.id}'
        ))
    return products_keyboard.adjust(2).as_markup()
