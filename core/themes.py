"""
🎨 Advanced UI Themes Module
Beautiful embed themes for premium experience
"""

import discord
from enum import Enum

class Theme(Enum):
    """UI Themes"""
    DARK = "dark"
    LIGHT = "light"
    NEON = "neon"
    OCEAN = "ocean"
    SUNSET = "sunset"
    FOREST = "forest"
    CYBERPUNK = "cyberpunk"
    GALAXY = "galaxy"

class ThemeManager:
    """Manages UI themes"""
    
    THEME_COLORS = {
        Theme.DARK: {"primary": 0x2C2F33, "accent": 0x7289DA},
        Theme.LIGHT: {"primary": 0xFFFFFF, "accent": 0x7289DA},
        Theme.NEON: {"primary": 0x0D0221, "accent": 0xFF006E},
        Theme.OCEAN: {"primary": 0x001F3F, "accent": 0x7FDBCA},
        Theme.SUNSET: {"primary": 0xFF6B35, "accent": 0xFDB833},
        Theme.FOREST: {"primary": 0x1B4332, "accent": 0x52B788},
        Theme.CYBERPUNK: {"primary": 0x000000, "accent": 0x00FF00},
        Theme.GALAXY: {"primary": 0x0A0E27, "accent": 0x9D4EDD},
    }
    
    @staticmethod
    def create_embed(title="", description="", theme=Theme.DARK):
        """Create themed embed"""
        colors = ThemeManager.THEME_COLORS[theme]
        return discord.Embed(
            title=title,
            description=description,
            color=colors["primary"]
        )
