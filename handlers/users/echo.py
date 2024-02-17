from aiogram import Router, types, F

router = Router()


@router.callback_query(F.data == "menyu")
async def start_user(callback: types.CallbackQuery):
    await callback.message.answer("soz")
