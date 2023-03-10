from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b2 = KeyboardButton('О нас')
b3 = KeyboardButton('Университеты')
b4 = KeyboardButton('Связаться с нами')

kb.insert(b2).insert(b3).add(b4)

kb_University =ReplyKeyboardMarkup(resize_keyboard=True)
bp1=KeyboardButton(text='Almaty')
bp2=KeyboardButton(text='Astana')
bp4=KeyboardButton(text='Shymkent')
bu26=KeyboardButton(text="Назад")
kb_University.add(bp1).insert(bp2).insert(bp4).add(bu26)

kb_Al=ReplyKeyboardMarkup(resize_keyboard=True)
bu1=KeyboardButton(text="Narxoz University")
bu2=KeyboardButton(text="Satbaev University")
bu3=KeyboardButton(text="Kaspian University")
bu4=KeyboardButton(text="Turan University")
bu5=KeyboardButton(text="Al-Farabi University")

bu21=KeyboardButton(text="Назад")
kb_Al.add(bu1,bu2,bu3,bu4,bu5,bu21)


kb_Sm=ReplyKeyboardMarkup(resize_keyboard=True)
bu7=KeyboardButton(text="Shakarim University")
bu8=KeyboardButton(text="AB University")
bu9=KeyboardButton(text="Semey Medical University")
bu22=KeyboardButton(text="Назад")
kb_Sm.add(bu7).insert(bu8).add(bu9).add(bu22)


kb_As=ReplyKeyboardMarkup(resize_keyboard=True)
bu10=KeyboardButton(text="IT University")
bu11=KeyboardButton(text="Seyfullin University")
bu12=KeyboardButton(text="Narikbaev University")
bu13=KeyboardButton(text="Eurasian University")
bu23=KeyboardButton(text="Назад")
kb_As.add(bu10,bu11,bu12,bu13,bu23)


kb_St=ReplyKeyboardMarkup(resize_keyboard=True)
bu14=KeyboardButton(text="Miras University")
bu15=KeyboardButton(text="SILKWAY University")
bu16=KeyboardButton(text="Auezov University")
bu17=KeyboardButton(text="Otyrar University")
bu24=KeyboardButton(text="Назад")
kb_St.add(bu14,bu15,bu16,bu17,bu24)


kb_Os=ReplyKeyboardMarkup(resize_keyboard=True)
bu18=KeyboardButton(text="Serikbaev University")
bu19=KeyboardButton(text="Amanzholov University")
bu20=KeyboardButton(text="Kaz-American University")
bu25=KeyboardButton(text="Назад")
kb_Os.add(bu14,bu15,bu16,bu25)

kb_Un=ReplyKeyboardMarkup(resize_keyboard=True)
bu45=KeyboardButton(text="Государственное управление")
bu46=KeyboardButton(text="Политические массовые коммуникации")
bu47=KeyboardButton(text="Международные отношения")
bu48=KeyboardButton(text="Статистика")
bu49=KeyboardButton(text="Социология")
bu50=KeyboardButton(text="Digital Management and Design")
bu51=KeyboardButton(text="Назад")
kb_Un.add(bu45,bu46,bu47,bu48,bu49,bu50,bu51)
kb_nar = InlineKeyboardMarkup(row_width=2)
urlButton = InlineKeyboardButton(text='Узнать больше', url='https://narxoz.edu.kz/')
kb_nar.add(urlButton)



kb_Stt=ReplyKeyboardMarkup(resize_keyboard=True)
bu52=KeyboardButton(text="Информационные системы")
bu53=KeyboardButton(text="Информационная безопасность")
bu54=KeyboardButton(text="Технология литейного производства")
bu55=KeyboardButton(text="Инженерная экология")
bu56=KeyboardButton(text="Биотехнология")
bu57=KeyboardButton(text="Дизайн")

bu58=KeyboardButton(text="Назад")
kb_Stt.add(bu52,bu53,bu54,bu55,bu56,bu57,bu58)
kb_satt = InlineKeyboardMarkup(row_width=2)
urlButton = InlineKeyboardButton(text='Узнать больше', url='https://satbayev.university/')
kb_satt.add(urlButton)


kb_Kas=ReplyKeyboardMarkup(resize_keyboard=True)
bu59=KeyboardButton(text="Школа Права «Әділет»!")
bu60=KeyboardButton(text="Школа экономики и управления")
bu61=KeyboardButton(text="Школа гуманитарных наук")
bu63=KeyboardButton(text="Биотехнология")
bu65=KeyboardButton(text="Назад")
kb_Kas.add(bu59,bu60,bu61,bu63,bu65)

bu90 = InlineKeyboardMarkup(row_width=2)
urlButton = InlineKeyboardButton(text='Узнать больше', url='https://cu.edu.kz/направление-подготовки/высшая-школа-экономики-и-управления/')
bu90.add(urlButton)

kb_Tur=ReplyKeyboardMarkup(resize_keyboard=True)
bu66=KeyboardButton(text="ЮРИСПРУДЕНЦИЯ")
bu67=KeyboardButton(text="МЕЖДУНАРОДНЫЕ ОТНОШЕНИЯ")
bu68=KeyboardButton(text="МЕЖДУНАРОДНОЕ ПРАВО")
bu69=KeyboardButton(text="РЕЖИССУРА")
bu70=KeyboardButton(text="ПРОДЮСИРОВАНИЕ КИНО И ТВ")
bu71=KeyboardButton(text="ПРОГРАММНАЯ ИНЖЕНЕРИЯ")
bu72=KeyboardButton(text="Назад")
kb_Tur.add(bu66,bu67,bu68,bu69,bu70,bu71,bu72)

kb_Turr = InlineKeyboardMarkup(row_width=2)
urlButton = InlineKeyboardButton(text='Узнать больше', url='https://turan.edu.kz/ru/bakalavriat/')
kb_Turr.add(urlButton)

kb_Alf=ReplyKeyboardMarkup(resize_keyboard=True)
bu66=KeyboardButton(text="Археология")
bu67=KeyboardButton(text="Международные отношения")
bu68=KeyboardButton(text="Биология")
bu69=KeyboardButton(text="Генетика")
bu70=KeyboardButton(text="Землеустройство")
bu71=KeyboardButton(text="Киберфизика")
bu72=KeyboardButton(text="Назад")
kb_Alf.add(bu66,bu67,bu68,bu69,bu70,bu71,bu72)

kb_Alff = InlineKeyboardMarkup(row_width=2)
urlButton = InlineKeyboardButton(text='Узнать больше', url='https://welcome.kaznu.kz/ru/education_programs/bachelor/')
kb_Alff.add(urlButton)


kb_Ait=ReplyKeyboardMarkup(resize_keyboard=True)
bu66=KeyboardButton(text="Computer Science")
bu67=KeyboardButton(text="Software Engineering")
bu68=KeyboardButton(text="Анализ больших данных")
bu69=KeyboardButton(text="Media Technologies")
bu70=KeyboardButton(text="Mathematical & Computational Science")
bu71=KeyboardButton(text="Cybersecurity")
bu72=KeyboardButton(text="Назад")
kb_Ait.add(bu66,bu67,bu68,bu69,bu70,bu71,bu72)

kb_Aitt = InlineKeyboardMarkup(row_width=2)
urlButton = InlineKeyboardButton(text='Узнать больше', url='https://astanait.edu.kz/programs/')
urlButton1 = InlineKeyboardButton(text='Контакты', url='https://astanait.edu.kz/contact/')
kb_Aitt.add(urlButton, urlButton1)

kb_Atu=ReplyKeyboardMarkup(resize_keyboard=True)
bu66=KeyboardButton(text="Растениеводство")
bu67=KeyboardButton(text="Животноводство")
bu68=KeyboardButton(text="Информационные технологии")
bu69=KeyboardButton(text="Архитектура")
bu70=KeyboardButton(text="Окружающая среда")
bu71=KeyboardButton(text="Агроинженерия")
bu72=KeyboardButton(text="Назад")
kb_Atu.add(bu66,bu67,bu68,bu69,bu70,bu71,bu72)

kb_Atuu = InlineKeyboardMarkup(row_width=2)
urlButton = InlineKeyboardButton(text='Узнать больше', url='https://www.kazatu.edu.kz/')
urlButton1 = InlineKeyboardButton(text='Контакты', url='https://www.kazatu.edu.kz/call-center')
kb_Atuu.add(urlButton, urlButton1)

kb_Guu=ReplyKeyboardMarkup(resize_keyboard=True)
bu101=KeyboardButton(text="Юриспруденция")
bu102=KeyboardButton(text="Туризм")
bu103=KeyboardButton(text="Гостеприимство")
bu104=KeyboardButton(text="Психология")
bu105=KeyboardButton(text="Журналистика")
bu106=KeyboardButton(text="Агроинженерия")
bu107=KeyboardButton(text="Назад")
kb_Guu.add(bu101,bu102,bu103,bu104,bu105,bu106,bu107)

kb_Guuu = InlineKeyboardMarkup(row_width=2)
urlButton12 = InlineKeyboardButton(text='Узнать больше', url='https://kazguu.kz/ru/')
kb_Guuu.add(urlButton12)

kb_Eu=ReplyKeyboardMarkup(resize_keyboard=True)
bu108=KeyboardButton(text="Юриспруденции")
bu109=KeyboardButton(text="Туризмм")
bu110=KeyboardButton(text="Гостеприимства")
bu111=KeyboardButton(text="Психологии")
bu112=KeyboardButton(text="Журналистики")
bu113=KeyboardButton(text="Агроинженерии")
bu114=KeyboardButton(text="Назад")
kb_Eu.add(bu108,bu109,bu110,bu111,bu112,bu113,bu114)

kb_Euu = InlineKeyboardMarkup(row_width=2)
urlButton13 = InlineKeyboardButton(text='Узнать больше', url='https://my.enu.kz/')
urlButton14 = InlineKeyboardButton(text='Контакт', url='https://my.enu.kz/page_dictonary.php?lng=kz')
kb_Euu.add(urlButton13, urlButton14)


kb_Mir=ReplyKeyboardMarkup(resize_keyboard=True)
bu120=KeyboardButton(text="Computer")
bu121=KeyboardButton(text="Software Engineer")
bu122=KeyboardButton(text="Анализ данных")
bu123=KeyboardButton(text="Media")
bu124=KeyboardButton(text="Mathematical Science")
bu125=KeyboardButton(text="IT")
bu126=KeyboardButton(text="Назад")
kb_Mir.add(bu120,bu121,bu122,bu123,bu124,bu125,bu126)

kb_Mirr = InlineKeyboardMarkup(row_width=2)
urlButton15 = InlineKeyboardButton(text='Узнать больше', url='https://miras.edu.kz/university/index.php/ru/')
kb_Mirr.add(urlButton15)

kb_Silk=ReplyKeyboardMarkup(resize_keyboard=True)
bu120=KeyboardButton(text="Музыкальное образование")
bu121=KeyboardButton(text="Основы права и экономики")
bu122=KeyboardButton(text="Педагогика и психология")
bu123=KeyboardButton(text="Переводческое дело")
bu124=KeyboardButton(text="Финансы")
bu125=KeyboardButton(text="Экономика")
bu126=KeyboardButton(text="Назад")
kb_Silk.add(bu120,bu121,bu122,bu123,bu124,bu125,bu126)

kb_Silkk = InlineKeyboardMarkup(row_width=2)
urlButton15 = InlineKeyboardButton(text='Узнать больше', url='https://univision.kz/univ/116-mezhdunarodnyy-universitet-silkway/')
kb_Silkk.add(urlButton15)

kb_Auez=ReplyKeyboardMarkup(resize_keyboard=True)
bu120=KeyboardButton(text="Хореография")
bu121=KeyboardButton(text="Политология")
bu122=KeyboardButton(text="Филология")
bu123=KeyboardButton(text="Психология")
bu124=KeyboardButton(text="Растениеводство")
bu125=KeyboardButton(text="Право")
bu126=KeyboardButton(text="Назад")
kb_Auez.add(bu120,bu121,bu122,bu123,bu124,bu125,bu126)

kb_Auezz = InlineKeyboardMarkup(row_width=2)
urlButton15 = InlineKeyboardButton(text='Узнать больше', url='https://priem.auezov.edu.kz/ru/')
kb_Auezz.add(urlButton15)

kb_Otr=ReplyKeyboardMarkup(resize_keyboard=True)
bu120=KeyboardButton(text="Хореографии")
bu121=KeyboardButton(text="Политологии")
bu122=KeyboardButton(text="Филологии")
bu123=KeyboardButton(text="Психологии")
bu124=KeyboardButton(text="Растениеводства")
bu125=KeyboardButton(text="Права")
bu126=KeyboardButton(text="Назад")
kb_Otr.add(bu120,bu121,bu122,bu123,bu124,bu125,bu126)

kb_Otrr = InlineKeyboardMarkup(row_width=2)
urlButton15 = InlineKeyboardButton(text='Узнать больше', url='https://univery.kz/universitet-otyrar-shymkent.html')
kb_Otrr.add(urlButton15)