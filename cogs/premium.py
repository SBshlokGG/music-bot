"""
👑 Premium Features Cog
User profiles, playlists, library, achievements, leaderboards
"""

import discord
from discord import app_commands
from discord.ext import commands
import logging
import config

logger = logging.getLogger('ShlokMusic.Premium')

class Premium(commands.Cog, name="Premium"):
    """👑 Premium user profiles, playlists, and achievements"""
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @commands.hybrid_command(name="profile", aliases=["me"], description="View your profile")
    async def profile(self, ctx: commands.Context, user: discord.User = None):
        """View user profile"""
        target_user = user or ctx.author
        
        embed = discord.Embed(
            title=f"👤 {target_user.name}'s Profile",
            color=config.BOT_COLOR
        )
        
        embed.set_thumbnail(url=target_user.display_avatar.url)
        embed.add_field(name="📊 Stats", value="🔜 Premium features coming soon!", inline=False)
        
        await ctx.send(embed=embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Premium(bot))
    logger.info("✅ Premium cog loaded")
