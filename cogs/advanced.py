"""
🚀 Advanced Features Cog
Premium audio settings, equalizer presets, and AI features
"""

import logging
import discord
from discord import app_commands
from discord.ext import commands

import config

logger = logging.getLogger('ShlokMusic.Advanced')

class Advanced(commands.Cog, name="Advanced"):
    """🚀 Advanced audio and bot features"""
    
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    def get_player(self, ctx):
        """Get or create music player for the guild"""
        return self.bot.get_player(ctx.guild.id)
    
    # ═══════════════════════════════════════════════════════════
    # 🎛️ AUDIO PRESET COMMANDS
    # ═══════════════════════════════════════════════════════════
    
    @commands.hybrid_group(name="preset", aliases=["eq"], description="Audio equalizer presets")
    async def preset(self, ctx: commands.Context):
        """Audio preset commands"""
        if ctx.invoked_subcommand is None:
            player = self.get_player(ctx)
            
            embed = discord.Embed(
                title="🎛️ Audio Presets",
                description="Premium sound profiles for different music genres and use cases",
                color=config.BOT_COLOR
            )
            
            presets = {
                "📢 Clarity": "`clarity` - Speech optimized\n`phonetic` - Maximum speech clarity\n`studio` - Professional sound",
                "🎵 Music": "`pop` - Pop & vocals\n`hiphop` - Rap & hip-hop\n`rock` - Rock & guitars\n`electronic` - EDM & synth",
                "🎬 Special": "`cinema` - Cinematic effect\n`halls` - Concert acoustics\n`crystalclear` - Ultra HD quality",
            }
            
            for category, items in presets.items():
                embed.add_field(name=category, value=items, inline=True)
            
            embed.add_field(
                name="Usage",
                value="`!preset <name>` - Apply a preset\n`!preset reset` - Return to default",
                inline=False
            )
            embed.set_footer(text=f"Current: {player.current_effect}")
            
            await ctx.send(embed=embed)
    
    @preset.command(name="list", description="List all audio presets")
    async def preset_list(self, ctx: commands.Context):
        """List all presets"""
        embed = discord.Embed(
            title="🎛️ All Audio Presets",
            color=config.BOT_COLOR
        )
        
        for name, data in config.AUDIO_EFFECTS.items():
            if name != "none":
                desc = data.get("description", "")
                embed.add_field(name=name.upper(), value=desc, inline=False)
        
        await ctx.send(embed=embed)
    
    @preset.command(name="apply", description="Apply an audio preset")
    @app_commands.describe(name="Preset name")
    async def preset_apply(self, ctx: commands.Context, name: str):
        """Apply a preset"""
        player = self.get_player(ctx)
        name = name.lower()
        
        if name not in config.AUDIO_EFFECTS:
            embed = discord.Embed(
                title="❌ Unknown Preset",
                description=f"Preset `{name}` not found. Use `!preset list`",
                color=config.BOT_COLOR_ERROR
            )
            await ctx.send(embed=embed, delete_after=10)
            return
        
        player.current_effect = name
        
        embed = discord.Embed(
            title="✅ Preset Applied",
            description=f"Audio preset changed to: **{name.upper()}**",
            color=config.BOT_COLOR_SUCCESS
        )
        
        effect_data = config.AUDIO_EFFECTS[name]
        if desc := effect_data.get("description"):
            embed.add_field(name="Description", value=desc, inline=False)
        
        await ctx.send(embed=embed)
    
    @preset.command(name="reset", description="Reset to default preset")
    async def preset_reset(self, ctx: commands.Context):
        """Reset preset"""
        player = self.get_player(ctx)
        player.current_effect = "crystalclear"
        
        embed = discord.Embed(
            title="🔄 Preset Reset",
            description="Audio preset reset to **CrystalClear**",
            color=config.BOT_COLOR_SUCCESS
        )
        await ctx.send(embed=embed)
    
    # ═══════════════════════════════════════════════════════════
    # 🎚️ AUDIO QUALITY SETTINGS
    # ═══════════════════════════════════════════════════════════
    
    @commands.hybrid_group(name="quality", aliases=["bitrate"], description="Audio quality settings")
    async def quality(self, ctx: commands.Context):
        """Audio quality commands"""
        if ctx.invoked_subcommand is None:
            player = self.get_player(ctx)
            
            embed = discord.Embed(
                title="🎚️ Audio Quality Settings",
                color=config.BOT_COLOR
            )
            
            quality_info = {
                "high": "🔊 320kbps - Crystal clear\n48kHz sample rate\nAdvanced filters enabled",
                "normal": "🔉 256kbps - Balanced\n44.1kHz sample rate\nStandard filters",
                "low": "🔕 128kbps - Lightweight\n44.1kHz sample rate\nBasic playback"
            }
            
            for mode, info in quality_info.items():
                emoji = "✅" if player.quality_mode == mode else "○"
                embed.add_field(name=f"{emoji} {mode.upper()}", value=info, inline=True)
            
            embed.add_field(
                name="Commands",
                value="`!quality high` - Maximum quality\n`!quality normal` - Balanced\n`!quality low` - Lightweight",
                inline=False
            )
            
            await ctx.send(embed=embed)
    
    @quality.command(name="high", description="Set quality to high (320kbps)")
    async def quality_high(self, ctx: commands.Context):
        """Set high quality"""
        player = self.get_player(ctx)
        player.quality_mode = "high"
        
        embed = discord.Embed(
            title="✅ Quality Set to HIGH",
            description="📊 320kbps • 48kHz\nAdvanced filters enabled\nMaximum audio clarity",
            color=config.BOT_COLOR_SUCCESS
        )
        await ctx.send(embed=embed)
    
    @quality.command(name="normal", description="Set quality to normal (256kbps)")
    async def quality_normal(self, ctx: commands.Context):
        """Set normal quality"""
        player = self.get_player(ctx)
        player.quality_mode = "normal"
        
        embed = discord.Embed(
            title="✅ Quality Set to NORMAL",
            description="📊 256kbps • 44.1kHz\nBalanced performance and quality",
            color=config.BOT_COLOR_SUCCESS
        )
        await ctx.send(embed=embed)
    
    @quality.command(name="low", description="Set quality to low (128kbps)")
    async def quality_low(self, ctx: commands.Context):
        """Set low quality"""
        player = self.get_player(ctx)
        player.quality_mode = "low"
        
        embed = discord.Embed(
            title="✅ Quality Set to LOW",
            description="📊 128kbps • 44.1kHz\nLightweight but lower quality",
            color=config.BOT_COLOR_SUCCESS
        )
        await ctx.send(embed=embed)
    
    # ═══════════════════════════════════════════════════════════
    # 🤖 AUTO-DJ FEATURE
    # ═══════════════════════════════════════════════════════════
    
    @commands.hybrid_command(name="autodj", aliases=["ai"], description="Toggle auto DJ mode")
    async def autodj(self, ctx: commands.Context):
        """Toggle auto DJ"""
        player = self.get_player(ctx)
        player.auto_dj_enabled = not player.auto_dj_enabled
        
        status = "enabled" if player.auto_dj_enabled else "disabled"
        emoji = "🤖" if player.auto_dj_enabled else "🔇"
        
        embed = discord.Embed(
            title=f"{emoji} Auto DJ {status.upper()}",
            description="Bot will automatically queue similar songs when queue is empty",
            color=config.BOT_COLOR_SUCCESS
        )
        
        await ctx.send(embed=embed)
    
    # ═══════════════════════════════════════════════════════════
    # 📊 AUDIO STATS
    # ═══════════════════════════════════════════════════════════
    
    @commands.hybrid_command(name="audiostats", description="Show audio statistics")
    async def audiostats(self, ctx: commands.Context):
        """Show audio statistics"""
        player = self.get_player(ctx)
        
        embed = discord.Embed(
            title="📊 Audio Statistics",
            color=config.BOT_COLOR
        )
        
        embed.add_field(name="🎛️ Current Preset", value=player.current_effect.upper(), inline=True)
        embed.add_field(name="🎚️ Quality Mode", value=player.quality_mode.upper(), inline=True)
        embed.add_field(name="🔊 Volume", value=f"{int(player.volume * 100)}%", inline=True)
        
        embed.add_field(name="🤖 Auto DJ", value="✅ Enabled" if player.auto_dj_enabled else "❌ Disabled", inline=True)
        embed.add_field(name="📢 Normalization", value="✅ Enabled" if player.normalizer_enabled else "❌ Disabled", inline=True)
        embed.add_field(name="🎵 Bitrate", value="320kbps" if player.quality_mode == "high" else "256kbps" if player.quality_mode == "normal" else "128kbps", inline=True)
        
        if player.current_track:
            embed.add_field(name="▶️ Now Playing", value=f"[{player.current_track.title}]({player.current_track.url})", inline=False)
        
        embed.add_field(name="📋 Queue Size", value=f"{len(player.queue)} tracks", inline=True)
        embed.add_field(name="🕐 History", value=f"{len(player.history)} tracks", inline=True)
        
        await ctx.send(embed=embed)


async def setup(bot: commands.Bot) -> None:
    """Load the cog"""
    await bot.add_cog(Advanced(bot))
    logger.info("✅ Advanced cog loaded")
