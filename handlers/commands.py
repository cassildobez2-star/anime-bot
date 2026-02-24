from telegram import Update
from telegram.ext import ContextTypes
from core.queue_manager import DOWNLOAD_QUEUE


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Bot online!\nUse:\n/anime <link>"
    )


async def anime(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args:
        await update.message.reply_text("Envie um link.")
        return

    url = context.args[0]

    await DOWNLOAD_QUEUE.put({
        "chat_id": update.effective_chat.id,
        "url": url,
        "filename": "episodio.mp4"
    })

    await update.message.reply_text("✅ Adicionado à fila.")


async def fila(update: Update, context: ContextTypes.DEFAULT_TYPE):

    size = DOWNLOAD_QUEUE.qsize()
    await update.message.reply_text(f"📦 {size} capítulo(s) na fila.")
