"""
⚙️ Admin & Moderation Features
"""

import discord
from discord.ext import commands
import logging
import config

logger = logging.getLogger('ShlokMusic.Admin')

class Admin(commands.Cog, name="Admin"):
    """⚙️ Server management and moderation"""
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.hybrid_command(name="admin-settings", description="Admin settings")
    @commands.has_permissions(manage_guild=True)
    async def admin_settings(self, ctx: commands.Context):
        """Admin settings"""
        embed = discord.Embed(
            title="⚙️ Admin Settings",
            description="🔜 Coming soon!",
            color=config.BOT_COLOR
        )
        await ctx.send(embed=embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Admin(bot))
    logger.info("✅ Admin cog loaded")
