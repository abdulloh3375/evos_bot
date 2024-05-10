from aiogram import Bot, Dispatcher, types
import asyncio
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram import F
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton 



bot = Bot(token="6903892269:AAFQ7HTBS3B2HcOgu0902CefPOAf7sgOA9g")
dp = Dispatcher()






"""    ********************************************************
        Botni ishga tushiramiz
       ********************************************************
"""
@dp.message(Command("start"))
async def start_bot(message: Message):
    await message.answer("Quydagilardan birini tanlang!", reply_markup=reply_buttons())



"""    ********************************************************
        Bot ishga tushganidan keyingi multi panel
       ********************************************************
"""
def reply_buttons():
    buttons = [
        [KeyboardButton(text="Menyu")],
        [KeyboardButton(text="Mening buyurtmalarim")],
        [KeyboardButton(text="Fikir bildirish"), KeyboardButton(text="Sozlamalar")]
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)



"""    ********************************************************
        Menyu knopka bosilgandan kegin qaytariladigan javob
       ********************************************************
"""
@dp.message(F.text=="Menyu")
async def button_menu(message: Message):
    await message.answer(text="Geolakatsiyani yuboring yoki yetkazib berish manzilini tanlag", reply_markup=menu_button())



"""    ********************************************************
        Menyu knopka bosilganidan kegingi mulyi panel
       ********************************************************
"""
def menu_button():
    button_menu = [
        [KeyboardButton(text="Mening manzilim")],
        [KeyboardButton(text="Geolakatsiya jo'natish"), KeyboardButton(text="Ortga")]
    ]
    return ReplyKeyboardMarkup(keyboard=button_menu, resize_keyboard=True)



"""    ********************************************************
        Buyrtmalrni tekshirish knopkasi 
       ********************************************************
"""
@dp.message(F.text=="Mening buyurtmalarim")
async def button_ordes(message: Message):
    await message.answer(text="Siz hech narsa buyurtma bermadingiz")



"""    ********************************************************
        Fikir bildirish
       ********************************************************
"""
@dp.message(F.text=="Fikir bildirish")
async def comment(message: Message):
    await message.answer(text="Siz bilan bosg'lanishimiz uchun telefon raqamingizni qoldiring", reply_markup=comment_button())



"""    ********************************************************
        Tel rqam fikir bildirish uchun
       ********************************************************
"""
def comment_button():
    button = [
        [KeyboardButton(text="Mening telefon raqamim", request_contact=True)],
        [KeyboardButton(text="Ortga")]
    ]
    return ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)



"""    ********************************************************
        Mening manzilimni jo'natosh
       ********************************************************
"""
@dp.message(F.text=="Mening manzilim")
async def location(message: Message):
    await bot.send_location(chat_id=message.chat.id, latitude=41.2876351, longitude=69.2273964)
    await message.answer(text="Bo'limni tanlang", reply_markup=location_button())



"""    ********************************************************
        Manzil jo'natilganidan kegin taomlar menusi 
       ********************************************************
"""
def location_button():
    button =[
        [KeyboardButton(text="Lavash"), KeyboardButton(text="Sendvich")],
        [KeyboardButton(text="Shaurma"), KeyboardButton(text="Burger")],
        [KeyboardButton(text="Sub"), KeyboardButton(text="Kartoshka")],
        [KeyboardButton(text="Hod dog"), KeyboardButton(text="Sneklar")],
        [KeyboardButton(text="Salat, garnir, non"), KeyboardButton(text="Souslar")],
        [KeyboardButton(text="Setlar"), KeyboardButton(text="Desertlar")],
        [KeyboardButton(text="Issiq ichimliklar"), KeyboardButton(text="Sovuq ichimliklar")],
        [KeyboardButton(text="Combo")],
        [KeyboardButton(text="Savat"), KeyboardButton(text="Ortga")]
    ]
    return ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)



"""    ********************************************************
        Geolcatsiya tanlash
       ********************************************************
"""
@dp.message(F.text=="Geolakatsiya jo'natish")
async def choose_location(message: Message):
    await bot.send_location(chat_id=message.chat.id, latitude=41.2876351, longitude=69.2273964)
    await message.answer(text="Geolokatsiyani tasdiqlang", reply_markup=choose_loc_button())



"""    ********************************************************
        Geolcatsiyani tasdiqlash knopkasi
       ********************************************************
"""
def choose_loc_button():
    button = [
        [KeyboardButton(text="Ha, tasdiqlayman"), KeyboardButton(text="Qayta tanlash")] 
    ]
    return ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)



"""    ********************************************************
        Geolcatsiya tasdiqlanganda taomlar menusini chiqarish
       ********************************************************
"""
@dp.message(F.text=="Ha, tasdiqlayman")
async def confirm(message: Message):
    await message.answer(text="Bo'limni tanlang", reply_markup=location_button())



"""    ********************************************************
        Lavash
       ********************************************************
"""
@dp.message(F.text=="Lavash")
async def lavash_(message: Message):
    await bot.send_photo(chat_id=message.chat.id, photo="https://yandex.ru/images/search?p=1&text=lavash+fon&pos=1&rpt=simage&img_url=https%3A%2F%2Fpodacha-blud.com%2Fuploads%2Fposts%2F2022-06%2F1654221139_38-podacha-blud-com-p-fud-foto-shaurmi-foto-38.jpg&from=tabbar&lr=10335")
    await message.answer(text="Lavash turini tanlang", reply_markup=lavash_button())



def lavash_button():
    button = [
        [KeyboardButton(text="Tovuq go'shtidan lavash"),KeyboardButton(text="Mol go'shtidan lavash")],
        [KeyboardButton(text="Tovuq go'shtidan qalampirli lavash"),KeyboardButton(text="Mol go'shtidan qalampirli lavash")],
        [KeyboardButton(text="Tovuq go'shtidan pishloqli lavash"),KeyboardButton(text="Mol go'shtiadan pishloqli lavash")],
        [KeyboardButton(text="Fitter")],
        [KeyboardButton(text="Ortga")]

    ]
    return ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)



@dp.message(F.text=="Tovuq go'shtidan lavash")
async def lavash_tovuq_gosht(message: Message):
    await bot.send_photo(chat_id=message.chat.id, photo="https://yandex.ru/images/search?p=1&text=lavash+fon&pos=29&rpt=simage&img_url=https%3A%2F%2Featstreet.imgix.net%2Fproduct_photos%2F1b1d487dffd7db590ad01db6c4d82c1c7d1da&from=tabbar&lr=10335", reply_markup=lavash_tovuq_gosht_button())
    # await message.answer(text="Big lavash yoki mini lavash", reply_markup=inline_lavash_tovuq_gosht()) 
    


def lavash_tovuq_gosht_button():
    button = [
        [KeyboardButton(text="Savat")],[KeyboardButton(text="Ortga")]
    ]    
    return ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)



# def inline_lavash_tovuq_gosht():
#     buttons = InlineKeyboardBuilder()
#     big_gosht_lavash = InlineKeyboardButton(text="30 000")
#     mini_gosht_lavash = InlineKeyboardButton(text="25 000")
#     buttons.add(big_gosht_lavash)
#     buttons.add(mini_gosht_lavash)
#     return buttons.as_markup()



@dp.message(F.text=="Tovuq go'shtidan qalampirli lavash")
async def lavash_tovuq_gosht_qalampir(message: Message):
    await bot.send_photo(chat_id=message.chat.id, photo="https://yandex.ru/images/search?p=1&text=lavash+fon&pos=29&rpt=simage&img_url=https%3A%2F%2Featstreet.imgix.net%2Fproduct_photos%2F1b1d487dffd7db590ad01db6c4d82c1c7d1da&from=tabbar&lr=10335", reply_markup=lavash_tovuq_gosht_qalampir_button())
    # await message.answer(text="Big lavash yoki mini lavash", reply_markup=inline_lavash_tovuq_gosht()) 
    


def lavash_tovuq_gosht_qalampir_button():
    button = [
        [KeyboardButton(text="Savat")],[KeyboardButton(text="Ortga")]
    ]    
    return ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)



@dp.message(F.text=="Tovuq go'shtidan pishloqli lavash")
async def lavash_tovuq_gosht_pishloq(message: Message):
    await bot.send_photo(chat_id=message.chat.id, photo="https://yandex.ru/images/search?p=1&text=lavash+fon&pos=29&rpt=simage&img_url=https%3A%2F%2Featstreet.imgix.net%2Fproduct_photos%2F1b1d487dffd7db590ad01db6c4d82c1c7d1da&from=tabbar&lr=10335", reply_markup=lavash_tovuq_gosht_pishloq_button())
    # await message.answer(text="Big lavash yoki mini lavash", reply_markup=inline_lavash_tovuq_gosht()) 
    


def lavash_tovuq_gosht_pishloq_button():
    button = [
        [KeyboardButton(text="Savat")],[KeyboardButton(text="Ortga")]
    ]    
    return ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)




@dp.message(F.text=="Mol go'shtidan lavash")
async def lavash_mol_gosht(message: Message):
    await bot.send_photo(chat_id=message.chat.id, photo="https://yandex.ru/images/search?p=1&text=lavash+fon&pos=29&rpt=simage&img_url=https%3A%2F%2Featstreet.imgix.net%2Fproduct_photos%2F1b1d487dffd7db590ad01db6c4d82c1c7d1da&from=tabbar&lr=10335", reply_markup=lavash_mol_gosht_button())
    # await message.answer(text="Big lavash yoki mini lavash", reply_markup=inline_lavash_tovuq_gosht()) 
    


def lavash_mol_gosht_button():
    button = [
        [KeyboardButton(text="Savat")],[KeyboardButton(text="Ortga")]
    ]    
    return ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)




@dp.message(F.text=="Mol go'shtidan qalampirli lavash")
async def lavash_mol_gosht_qalampir(message: Message):
    await bot.send_photo(chat_id=message.chat.id, photo="https://yandex.ru/images/search?p=1&text=lavash+fon&pos=29&rpt=simage&img_url=https%3A%2F%2Featstreet.imgix.net%2Fproduct_photos%2F1b1d487dffd7db590ad01db6c4d82c1c7d1da&from=tabbar&lr=10335", reply_markup=lavash_mol_gosht_qalampir_button())
    # await message.answer(text="Big lavash yoki mini lavash", reply_markup=inline_lavash_tovuq_gosht()) 
    


def lavash_mol_gosht_qalampir_button():
    button = [
        [KeyboardButton(text="Savat")],[KeyboardButton(text="Ortga")]
    ]    
    return ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)




@dp.message(F.text=="Mol go'shtidan pishloqli lavash")
async def lavash_mol_gosht_pishloq(message: Message):
    await bot.send_photo(chat_id=message.chat.id, photo="https://yandex.ru/images/search?p=1&text=lavash+fon&pos=29&rpt=simage&img_url=https%3A%2F%2Featstreet.imgix.net%2Fproduct_photos%2F1b1d487dffd7db590ad01db6c4d82c1c7d1da&from=tabbar&lr=10335", reply_markup=lavash_mol_gosht_pishloq_button())
    # await message.answer(text="Big lavash yoki mini lavash", reply_markup=inline_lavash_tovuq_gosht()) 
    


def lavash_mol_gosht_pishloq_button():
    button = [
        [KeyboardButton(text="Savat")],[KeyboardButton(text="Ortga")]
    ]    
    return ReplyKeyboardMarkup(keyboard=button, resize_keyboard=True)











async def main():
    print("bot ishladi")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())