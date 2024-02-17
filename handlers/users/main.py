from loader import db, Bot
from aiogram import Router, F, types

router = Router()


@router.callback_query(F.data == "menyu")
async def get_menyu(callback: types.CallbackQuery):
  await callback.message.answer("menyu yoq!")
