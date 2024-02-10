from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart

import app.keyboards as kb
from app.database.requests import get_product

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Welcome to ShopSheep!',
                         reply_markup=kb.main_keyboard)


@router.message(F.text == 'Catalog')
async def catalog(message: Message):
    await message.answer('Select an option from catalog',
                         reply_markup=await kb.categories_b())


@router.callback_query(F.data.startswith('category_'))
async def category_selected(callback: CallbackQuery):
    category_id = callback.data.split('_', 1)
    await callback.message.answer(
        f'Products by selected category:',
        reply_markup=await kb.products_b(category_id)
    )
    await callback.answer('Selected')


@router.callback_query(F.data.startswith('product_'))
async def category_selected(callback: CallbackQuery):
    product_id = callback.data.split('_', 1)
    product = await get_product(product_id=product_id)
    await callback.message.answer(
        f'<b>{product.name}</b>\n\n{product.description}\n\nPrice: {product.price}',
    )
    await callback.answer('Selected')
