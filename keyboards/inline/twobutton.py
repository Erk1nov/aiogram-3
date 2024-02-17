from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

menyu = InlineKeyboardMarkup(
  inline_keyboard=[
    [InlineKeyboardButton(text="Menyu", callback_data="menyu")]
  ]
)