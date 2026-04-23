# telegram-bot.py
# OpenCode Telegram Bot - Daily Brief and Task Management

import os
import asyncio
import logging
from datetime import datetime

# Telegram Bot
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# OpenCode imports
import requests

# ============= CONFIGURATION =============
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN", "7953249856:AAGLm38BnrqtFjgSCO952wAglmtEjyzAWcs")
CHAT_ID = os.getenv("CHAT_ID", "5667291055")

# OBSIDIAN
OBSIDIAN_URL = "http://127.0.0.1:27123"
OBSIDIAN_API_KEY = "dadde3d8184f6aae78239eb4570ac4430b55532fcf5afb77fd081f70c7e0c459"

# OMI
OMI_API_KEY = "omi_dev_f109295456f5a35b2226ddadc206b4dc"
OMI_API_URL = "https://api.omi.me/v1/dev"

# ============= LOGGING =============
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ============= OBSIDIAN HELPERS =============
def get_obsidian_note(path: str) -> str:
    """Get note from Obsidian"""
    headers = {"Authorization": f"Bearer {OBSIDIAN_API_KEY}"}
    try:
        response = requests.get(
            f"{OBSIDIAN_URL}/vault/{path}",
            headers=headers,
            timeout=10
        )
        if response.status_code == 200:
            return response.text
        return None
    except Exception as e:
        logger.error(f"Error fetching note: {e}")
        return None

def search_obsidian(query: str) -> list:
    """Search in Obsidian vault"""
    # Simple search - returns list of filenames
    headers = {"Authorization": f"Bearer {OBSIDIAN_API_KEY}"}
    try:
        response = requests.get(
            f"{OBSIDIAN_URL}/vault/",
            headers=headers,
            timeout=10
        )
        if response.status_code == 200:
            files = response.json().get("files", [])
            # Filter by query
            return [f for f in files if query.lower() in f.lower()]
        return []
    except Exception as e:
        logger.error(f"Error searching: {e}")
        return []

# ============= OMI HELPERS =============
def get_omi_memories(limit: int = 10) -> list:
    """Get memories from OMI"""
    headers = {"Authorization": f"Bearer {OMI_API_KEY}"}
    try:
        response = requests.get(
            f"{OMI_API_URL}/user/memories?limit={limit}",
            headers=headers,
            timeout=10
        )
        if response.status_code == 200:
            return response.json()
        return []
    except Exception as e:
        logger.error(f"Error fetching OMI: {e}")
        return []

# ============= MESSAGE BUILDERS =============
async def build_daily_brief() -> str:
    """Build daily brief message"""
    msg = "📅 *OpenCode Daily Brief* \n\n"
    
    # Get pending tasks
    tasks_note = get_obsidian_note("Notas/tareas/pendientes.md")
    if tasks_note:
        msg += "*Tareas Pendientes:*\n"
        # Extract task lines
        lines = tasks_note.split("\n")
        for line in lines[:10]:  # First 10
            if "- [ ]" in line:
                task = line.replace("- [ ]", "").strip()
                if task:
                    msg += f"• {task}\n"
    else:
        msg += "_No hay tareas pendientes_\n"
    
    msg += "\n"
    
    # Get recent conversations
    msg += "*Sesión Reciente:*\n"
    conv_note = get_obsidian_note("Notas/conversaciones.md")
    if conv_note:
        # Get last few lines
        lines = conv_note.split("\n")
        for line in lines[-5:]:
            if line.strip():
                msg += f"• {line.strip()[:50]}\n"
    else:
        msg += "_Sin conversaciones_\n"
    
    msg += "\n"
    msg += "Usa /tasks para ver todas las tareas"
    
    return msg

async def build_tasks_message() -> str:
    """Build tasks list message"""
    msg = "📋 *Tareas Pendientes* \n\n"
    
    tasks_note = get_obsidian_note("Notas/tareas/pendientes.md")
    if tasks_note:
        lines = tasks_note.split("\n")
        count = 0
        for line in lines:
            if "- [ ]" in line:
                count += 1
                task = line.replace("- [ ]", "").strip()
                msg += f"{count}. {task}\n"
        
        if count == 0:
            msg += "¡No hay tareas pendientes! 🎉"
    else:
        msg += "No hay nota de tareas"
    
    return msg

async def build_alerts_message() -> str:
    """Build alerts message"""
    msg = "⚠️ *Alertas del Sistema* \n\n"
    
    # Check alerts
    alerts_note = get_obsidian_note("Notas/alertas.md")
    if alerts_note:
        msg += alerts_note[:500]  # First 500 chars
    else:
        msg += "_No hay alertas activas_"
    
    return msg

# ============= COMMAND HANDLERS =============
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /start"""
    await update.message.reply_text(
        "🤖 *OpenCode Bot*\n\n"
        "Tu asistente de IA con memoria persistente.\n\n"
        "Comandos disponibles:\n"
        "• /brief - Daily Brief\n"
        "• /tasks - Tareas pendientes\n"
        "• /search [texto] - Buscar\n"
        "• /alerts - Ver alertas\n"
        "• /help - Ayuda",
        parse_mode="Markdown"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /help"""
    await start_command(update, context)

async def brief_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /brief"""
    await update.message.reply_text("⏳ Generando Brief...")
    msg = await build_daily_brief()
    await update.message.reply_text(msg, parse_mode="Markdown")

async def tasks_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /tasks"""
    await update.message.reply_text("⏳ Cargando tareas...")
    msg = await build_tasks_message()
    await update.message.reply_text(msg, parse_mode="Markdown")

async def alerts_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /alerts"""
    msg = await build_alerts_message()
    await update.message.reply_text(msg, parse_mode="Markdown")

async def search_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle /search"""
    query = " ".join(context.args)
    if not query:
        await update.message.reply_text("Usa /search [texto]")
        return
    
    await update.message.reply_text(f"🔍 Buscando '{query}'...")
    
    # Search both systems
    obsidian_results = search_obsidian(query)
    omi_results = get_omi_memories(limit=5)
    
    msg = f"*Resultados para '{query}':*\n\n"
    
    # Obsidian
    msg += "*OBSIDIAN:*\n"
    if obsidian_results:
        for r in obsidian_results[:5]:
            msg += f"• {r}\n"
    else:
        msg += "_Sin resultados_\n"
    
    msg += "\n*OMI:*\n"
    if omi_results:
        for r in omi_results[:3]:
            content = r.get("content", "")[:50]
            msg += f"• {content}...\n"
    else:
        msg += "_Sin resultados_\n"
    
    await update.message.reply_text(msg, parse_mode="Markdown")

# ============= MESSAGE HANDLER =============
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle any other message"""
    await update.message.reply_text(
        "Usa /brief, /tasks, /search o /alerts"
    )

# ============= DAILY BRIEF SCHEDULER =============
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes, JobQueue, HTTPServer, BaseRequestHandler
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer

# ============= MAIN =============
def main():
    """Start the bot"""
    logger.info("Starting OpenCode Telegram Bot...")
    
    app = (
        ApplicationBuilder()
        .token(TELEGRAM_TOKEN)
        .build()
    )
    
    # Add command handlers
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("brief", brief_command))
    app.add_handler(CommandHandler("tasks", tasks_command))
    app.add_handler(CommandHandler("alerts", alerts_command))
    app.add_handler(CommandHandler("search", search_command))
    
    # Message handler
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # Start polling
    logger.info("Bot started. Press Ctrl+C to stop.")
    app.run_polling()

if __name__ == "__main__":
    main()