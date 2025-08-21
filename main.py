from pyrogram import Client, filters
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Настройки
load_dotenv()
API_ID = os.getenv("API_ID")  # Получить на my.telegram.org
API_HASH = os.getenv("API_HASH")
SESSION_NAME = "topor_bot"
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # Получить на ai.google.dev

# Проверка наличия API ключей
if not API_ID or not API_HASH:
    print("Ошибка: API_ID или API_HASH не установлены в переменных окружения.")
    exit()

if not GEMINI_API_KEY:
    print("Ошибка: GEMINI_API_KEY не установлен в переменных окружения.")
    exit()

# Настройка Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# Создание клиента
app = Client(SESSION_NAME, api_id=int(API_ID), api_hash=API_HASH)

TOPOR_PROMPT = """Перекавыркивай любые сообщения в стиле агрессивных заголовков желтушных газет.\n\nФормат ответа:\n⚡️ЗАГОЛОВОК 1⚡️ЗАГОЛОВОК 2⚡️ЗАГОЛОВОК 3⚡️\n\nПравила:\n- Каждый текст между ⚡️ - отдельный самодостаточный заголовок\n- НЕ связывай заголовки в единое предложение\n- Каждый заголовок должен работать сам по себе\n- КАПС обязательно\n- Грубые выражения приветствуются\n- Делай из мухи слона\n- Как будто это сенсация века\n\nПримеры:\nОбновление вышло \n⚡️РАЗРАБЫ ВЫКАТИЛИ ГОВНОАПДЕЙТ⚡️АПДЕЙТ СЛОМАЛ В С Ё⚡️ДЕВЕЛОПЕРЫ ОБОСРАЛИСЬ⚡️\n\n- Сайт лагает\n⚡️СЕРВЕРАМ ПИЗДЕЦ⚡️СИСАДМИНЫ ПРОЕБАЛИСЬ ⚡️ САЙТ - В С Ё⚡️\n- Кстати xray умеет жрать yaml. И вроде даже toml.А ремна нет.\n⚡️ПАНЕЛЬ НЕ ПОДДЕРЖИВАЕТ ОБОССАНУЮ ФИШКУ КОТОРУЮ ЮЗАЮТ 1.5 ЗЕМЛЕКОПА ⚡️ЕБАНОЕ ДЕРЬМО ⚡️VPN - В С Ё ⚡️РАЗРАБЫ ОБЛЕНИЛИСЬ И НЕ ЗАВОЗЯТ НОВЫЕ ФИШКИ\n- В Европе хотят получить контроль над всеми переписками — весь Евросоюз на пороге тотального контроля граждан\nПолитики планируют обязать мессенджеры «просматривать» переписку пользователей, включая защищённые чаты — якобы для защиты детей от сомнительного контента\nНа деле же правительство будет получать прямой доступ к любой переписке и просматривать ее — шифрования просто не будет\nСразу пятнадцать членов-государств ЕС подержали введение контроля, всего три выступили против, девять пока не решили — итог ожидается 14 октября\n⚡️ ЕВРОПА -  В С Ё⚡️ КОНФИДЕНЦИАЛЬНОСТИ ПИЗДА ⚡️ВЛАСТИ ЗАХВАТЫВАЮТ МОЗГ ЛЮДЕЙ\n\nГлавное - каждый заголовок между молниями независим от остальных, как отдельные кричащие новости.А вот на что надо ответить в таком стиле:{message_text}"""

# Создаем кастомный фильтр для команды topor с / или \
def topor_filter(_, __, message):
    if not message.text:
        return False
    text = message.text.strip()
    return text.startswith('/topor') or text.startswith('\\topor')

topor_command_filter = filters.create(topor_filter)

@app.on_message(topor_command_filter & filters.me)
async def topor_handler(client, message):
    try:
        # Проверяем, есть ли реплай
        if not message.reply_to_message:
            await message.edit("❌ Нужно реплайнуть на сообщение!")
            return

        # Получаем текст сообщения, на которое реплайнули
        replied_message = message.reply_to_message
        text_to_process = replied_message.text or replied_message.caption or ""

        if not text_to_process:
            await message.edit("❌ В сообщении нет текста!")
            return

        # Показываем, что бот работает
        await message.edit("⚡️ Генерирую топорные заголовки...")

        # Формируем промпт
        prompt = TOPOR_PROMPT.format(message_text=text_to_process)

        # Обращаемся к Gemini
        response = model.generate_content(prompt)
        result = response.text.strip()

        # Отправляем результат
        await message.edit(result)

    except Exception as e:
        await message.edit(f"❌ Ошибка: {str(e)}")

@app.on_message(filters.command("start") & filters.me)
async def start_handler(client, message):
    await message.edit("🔥 **Топор-бот активирован!**\n\n"
                      "Команды:\n"
                      "• /topor или \\topor - реплайнуть на сообщение для генерации заголовков\n\n"
                      "Реплайнь на любое сообщение с командой /topor или \\topor и получи топорные заголовки!")

if __name__ == "__main__":
    print("🚀 Запуск Топор-бота...")
    app.run()
