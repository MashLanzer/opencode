# discord-bot.py
# OpenCode Discord Bot - Messaging + Voice Integration

import os
import asyncio
import logging
from datetime import datetime
from typing import Optional

import discord
from discord import app_commands
from discord.ext import commands

import requests

# ============= CONFIGURATION =============
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# OBSIDIAN
OBSIDIAN_URL = "http://127.0.0.1:27123"
OBSIDIAN_API_KEY = os.getenv("OBSIDIAN_API_KEY", "dadde3d8184f6aae78239eb4570ac4430b55532fcf5afb77fd081f70c7e0c459")

# OMI
OMI_API_KEY = os.getenv("OMI_API_KEY", "omi_dev_f109295456f5a35b2226ddadc206b4dc")
OMI_API_URL = "https://api-omi.me/v1/dev"

# ============= LOGGING =============
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ============= BOT SETUP =============
intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)
tree = app_commands.CommandTree(bot)

voice_clients = {}

# ============= OBSIDIAN HELPERS =============
def get_obsidian_note(path: str) -> Optional[str]:
    headers = {"Authorization": f"Bearer {OBSIDIAN_API_KEY}"}
    try:
        response = requests.get(f"{OBSIDIAN_URL}/vault/{path}", headers=headers, timeout=10)
        if response.status_code == 200:
            return response.text
    except Exception as e:
        logger.error(f"Error: {e}")
    return None

def search_obsidian(query: str) -> list:
    headers = {"Authorization": f"Bearer {OBSIDIAN_API_KEY}"}
    try:
        response = requests.get(f"{OBSIDIAN_URL}/vault/", headers=headers, timeout=10)
        if response.status_code == 200:
            files = response.json().get("files", [])
            return [f for f in files if query.lower() in f.lower()]
    except:
        pass
    return []

def get_omi_memories(limit: int = 10) -> list:
    headers = {"Authorization": f"Bearer {OMI_API_KEY}"}
    try:
        response = requests.get(f"{OMI_API_URL}/user/memories?limit={limit}", headers=headers, timeout=10)
        if response.status_code == 200:
            return response.json()
    except:
        pass
    return []

# ============= MESSAGE BUILDERS =============
async def build_daily_brief() -> str:
    msg = "📅 *OpenCode Daily Brief*\n\n"
    tasks = get_obsidian_note("Notas/tareas/pendientes.md")
    if tasks:
        msg += "*Tareas:*\n"
        for line in tasks.split("\n")[:10]:
            if "- [ ]" in line:
                msg += f"• {line.replace('- [ ]', '').strip()}\n"
    return msg

# ============= SLASH COMMANDS =============
@tree.command(name="start", description="Info del bot")
async def start_cmd(i): await i.response.send_message("🤖 OpenCode Bot - /brief /tasks /search /join /leave")

@tree.command(name="brief", description="Daily Brief")
async def brief_cmd(i):
    await i.response.defer()
    await i.followup.send(await build_daily_brief())

@tree.command(name="tasks", description="Tareas")
async def tasks_cmd(i):
    tasks = get_obsidian_note("Notas/tareas/pendientes.md")
    msg = "📋 *Tareas*\n\n" + (tasks[:500] if tasks else "_Sin tareas_")
    await i.response.send_message(msg, ephemeral=True)

@tree.command(name="search", description="Buscar")
async def search_cmd(i, query: str):
    obs = search_obsidian(query)
    msg = f"*Resultados:*\n" + "\n".join(obs[:5]) if obs else "_Sin resultados_"
    await i.response.send_message(msg)

@tree.command(name="join", description="Unirse a voice")
async def join_cmd(i):
    if not i.user.voice:
        await i.response.send_message("❌ No estás en voice", ephemeral=True)
        return
    vc = await i.user.voice.channel.connect()
    voice_clients[i.guild.id] = vc
    await i.response.send_message(f"✅ En {i.user.voice.channel.name}")

@tree.command(name="leave", description="Salir de voice")
async def leave_cmd(i):
    gid = i.guild.id
    if gid in voice_clients:
        await voice_clients[gid].disconnect()
        del voice_clients[gid]
        await i.response.send_message("✅ Salí")
    else:
        await i.response.send_message("❌ No estoy en voice", ephemeral=True)

# ============= EVENTS =============
@bot.event
async def on_ready():
    logger.info(f"Bot: {bot.user}")
    await tree.sync()
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="/start"))

# ============= MAIN =============
def main():
    if not DISCORD_TOKEN:
        print("⚠️ Set DISCORD_TOKEN env var")
        return
    bot.run(DISCORD_TOKEN, log_handler=None)

if __name__ == "__main__":
    main()