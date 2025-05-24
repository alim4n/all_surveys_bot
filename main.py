from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "123456789"))

menu_keyboard = [
    ["1. شحن ألعاب"],
    ["2. شحن تطبيقات الدردشة"],
    ["3. اضافة رصيد"],
    ["4. الأسعار"],
    ["5. التواصل مع الدعم"]
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "مرحباً بك في بوت All surveys. اختر من القائمة:",
        reply_markup=ReplyKeyboardMarkup(menu_keyboard, resize_keyboard=True)
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text.startswith("1"):
        await update.message.reply_text("لشحن الألعاب، يرجى إرسال اسم اللعبة والمعرّف.")
    elif text.startswith("2"):
        await update.message.reply_text("لشحن تطبيقات الدردشة، يرجى إرسال نوع التطبيق والرقم.")
    elif text.startswith("3"):
        await update.message.reply_text("لإضافة رصيد، اختر الطريقة: [USDT، نقدي، سيريتل كاش].")
    elif text.startswith("4"):
        await update.message.reply_text("الأسعار الحالية:
- لعبة X: 5$
- تطبيق Y: 3$ ...")
    elif text.startswith("5"):
        await update.message.reply_text("أرسل رسالتك وسنقوم بالرد عليك في أقرب وقت.")
        await context.bot.send_message(chat_id=ADMIN_ID, text=f"رسالة دعم من {update.effective_user.username}:
{text}")
    elif update.effective_user.id == ADMIN_ID and text.startswith("/broadcast"):
        msg = text.replace("/broadcast ", "")
        await context.bot.send_message(chat_id=update.effective_chat.id, text="تم إرسال الرسالة بنجاح.")
    else:
        await update.message.reply_text("اختر أمراً من القائمة.")

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
