"""
🎵 Shlok Music Bot - Configuration
Advanced Discord Music Bot with Premium Features
"""

import os
from dataclasses import dataclass, field
from typing import Dict, List, Optional

# ═══════════════════════════════════════════════════════════════
# 🔑 BOT CREDENTIALS
# ═══════════════════════════════════════════════════════════════

# Use environment variables for secrets (never hardcode in production!)
BOT_TOKEN = os.getenv('BOT_TOKEN', '')
APPLICATION_ID = os.getenv('APPLICATION_ID', '1097878151713017896')
PUBLIC_KEY = os.getenv('PUBLIC_KEY', '')

# ═══════════════════════════════════════════════════════════════
# 🎨 BOT APPEARANCE
# ═══════════════════════════════════════════════════════════════

BOT_NAME = "Shlok Music"
BOT_PREFIXES = ['s!', '$', '!']  # Multiple prefixes
BOT_PREFIX = "s!"  # Primary prefix for display
BOT_COLOR = 0x7289DA  # Discord Blurple
BOT_COLOR_SUCCESS = 0x2ECC71  # Green
BOT_COLOR_ERROR = 0xE74C3C  # Red
BOT_COLOR_WARNING = 0xF39C12  # Orange
BOT_COLOR_INFO = 0x3498DB  # Blue

# ═══════════════════════════════════════════════════════════════
# 🎵 MUSIC SETTINGS
# ═══════════════════════════════════════════════════════════════

@dataclass
class MusicSettings:
    """Music player configuration"""
    default_volume: int = 100
    max_volume: int = 150
    min_volume: int = 0
    
    max_queue_size: int = 500
    max_song_duration: int = 7200  # 2 hours in seconds
    
    auto_disconnect_time: int = 300  # 5 minutes of inactivity
    stay_connected_24_7: bool = True  # 24/7 mode enabled
    
    default_search_limit: int = 5
    max_playlist_size: int = 100
    
    # Audio quality - OPTIMIZED FOR PREMIUM SOUND
    audio_bitrate: int = 320  # kbps - Maximum quality
    audio_sample_rate: int = 48000  # Hz
    enable_advanced_filters: bool = True
    enable_dynamic_normalization: bool = True
    enable_bass_enhancement: bool = True
    enable_recommendations: bool = True
    enable_auto_dj: bool = True
    
    # Advanced Features
    enable_user_profiles: bool = True
    enable_playlists: bool = True
    enable_achievements: bool = True
    enable_leaderboards: bool = True
    enable_themes: bool = True
    
    # Buffer settings for smooth playback
    buffer_size: int = 32768
    reconnect_attempts: int = 5
    
    # Premium features
    premium_bitrate: int = 320
    enable_offline_sync: bool = False
    enable_spatial_audio: bool = False
    
MUSIC = MusicSettings()

# ═══════════════════════════════════════════════════════════════
# 🎛️ AUDIO EFFECTS PRESETS
# ═══════════════════════════════════════════════════════════════

AUDIO_EFFECTS = {
    "none": {},
    "bass_boost": {
        "equalizer": [(0, 0.25), (1, 0.20), (2, 0.15), (3, 0.10)],
        "description": "🔊 Enhanced bass frequencies"
    },
    "nightcore": {
        "timescale": {"speed": 1.25, "pitch": 1.25, "rate": 1.0},
        "description": "⚡ Faster tempo with higher pitch"
    },
    "vaporwave": {
        "timescale": {"speed": 0.8, "pitch": 0.85, "rate": 1.0},
        "description": "🌊 Slowed and reverbed aesthetic"
    },
    "8d": {
        "rotation": {"rotation_hz": 0.2},
        "description": "🎧 360° rotating audio effect"
    },
    "karaoke": {
        "karaoke": {"level": 1.0, "mono_level": 1.0, "filter_band": 220, "filter_width": 100},
        "description": "🎤 Removes vocals from the track"
    },
    "tremolo": {
        "tremolo": {"frequency": 4.0, "depth": 0.6},
        "description": "〰️ Wavering volume effect"
    },
    "vibrato": {
        "vibrato": {"frequency": 4.0, "depth": 0.6},
        "description": "🎵 Wavering pitch effect"
    },
    "soft": {
        "lowpass": {"smoothing": 20.0},
        "description": "🌙 Soft and mellow sound"
    },
    "chipmunk": {
        "timescale": {"speed": 1.0, "pitch": 1.5, "rate": 1.0},
        "description": "🐿️ High pitched voice"
    },
    "deep": {
        "timescale": {"speed": 1.0, "pitch": 0.7, "rate": 1.0},
        "description": "👹 Deep voice effect"
    },
    "clarity": {
        "equalizer": [(0, -0.3), (1, 0.0), (2, 0.3), (3, 0.2), (4, 0.1), (5, -0.2)],
        "description": "🎤 Clear speech-like sound with enhanced midrange"
    },
    "crystalclear": {
        "equalizer": [(0, -0.2), (1, 0.1), (2, 0.4), (3, 0.3), (4, 0.2), (5, 0.1), (6, -0.1)],
        "description": "💎 Ultra-clear professional audio quality"
    },
    "studio": {
        "equalizer": [(0, 0.0), (1, 0.1), (2, 0.2), (3, 0.15), (4, 0.1), (5, 0.0), (6, -0.1)],
        "description": "🎙️ Studio-grade balanced sound"
    },
    "hiphop": {
        "equalizer": [(0, 0.3), (1, 0.1), (2, -0.1), (3, 0.0), (4, 0.0), (5, 0.2)],
        "description": "🎤 Enhanced bass and presence for hip-hop"
    },
    "pop": {
        "equalizer": [(0, 0.1), (1, 0.15), (2, 0.2), (3, 0.15), (4, 0.1), (5, -0.05)],
        "description": "🎵 Optimized for pop music with clear vocals"
    },
    "electronic": {
        "equalizer": [(0, 0.2), (1, 0.1), (2, -0.1), (3, 0.0), (4, 0.3), (5, 0.2)],
        "description": "⚡ Enhanced highs and lows for electronic music"
    },
    "rock": {
        "equalizer": [(0, 0.2), (1, 0.0), (2, -0.1), (3, 0.1), (4, 0.3), (5, 0.1)],
        "description": "🎸 Powerful bass and crisp guitars"
    },
    "cinema": {
        "equalizer": [(0, 0.1), (1, 0.05), (2, 0.15), (3, 0.2), (4, 0.15), (5, 0.1), (6, 0.0)],
        "reverb": {"room_size": 0.6, "damping": 0.5, "wet_level": 0.3, "dry_level": 1.0, "width": 1.0},
        "description": "🎬 Cinematic sound with room reverb"
    },
    "halls": {
        "reverb": {"room_size": 0.9, "damping": 0.3, "wet_level": 0.5, "dry_level": 1.0, "width": 1.0},
        "description": "🏛️ Concert hall acoustics"
    },
    "phonetic": {
        "equalizer": [(0, -0.4), (1, 0.2), (2, 0.4), (3, 0.25), (4, 0.1), (5, -0.3)],
        "description": "📢 Optimized for speech clarity"
    },
}

# ═══════════════════════════════════════════════════════════════
# 🎮 REACTION CONTROLS
# ═══════════════════════════════════════════════════════════════

REACTION_CONTROLS = {
    "⏯️": "pause_resume",      # Pause/Resume
    "⏭️": "skip",              # Skip
    "⏹️": "stop",              # Stop
    "🔀": "shuffle",           # Shuffle
    "🔁": "loop_queue",        # Loop queue
    "🔂": "loop_track",        # Loop track
    "🔉": "volume_down",       # Volume down
    "🔊": "volume_up",         # Volume up
    "❤️": "favorite",          # Add to favorites
    "📋": "show_queue",        # Show queue
    "🎵": "lyrics",            # Show lyrics
    "⏮️": "previous",          # Previous track
}

# Reaction emojis in order (for adding to messages)
CONTROL_EMOJIS = ["⏮️", "⏯️", "⏭️", "⏹️", "🔀", "🔁", "🔂", "🔉", "🔊", "❤️", "📋", "🎵"]

# ═══════════════════════════════════════════════════════════════
# 📊 PROGRESS BAR SETTINGS
# ═══════════════════════════════════════════════════════════════

PROGRESS_BAR = {
    "length": 20,
    "filled": "▰",
    "empty": "▱",
    "start_filled": "▰",
    "end_filled": "▰",
    "start_empty": "▱",
    "end_empty": "▱",
}

# ═══════════════════════════════════════════════════════════════
# 🔧 YTDL OPTIONS (Optimized for performance)
# ═══════════════════════════════════════════════════════════════

YTDL_OPTIONS = {
    'format': 'bestaudio[ext=webm]/bestaudio[ext=m4a]/bestaudio/best',
    'extractaudio': True,
    'audioformat': 'bestaudio',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': False,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'ytsearch',
    'source_address': '0.0.0.0',
    'force_generic_extractor': False,
    'cachedir': False,
    'extract_flat': 'in_playlist',
    'socket_timeout': 30,  # Increased from 10
    'retries': 10,  # Increased from 5
    'fragment_retries': 10,  # Increased from 5
    'skip_unavailable_fragments': True,
    'youtube_include_dash_manifest': True,  # Better quality selection
    'http_headers': {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    },
}

FFMPEG_OPTIONS = {
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5 -nostdin -rtbufsize 150M',
    'options': '-vn -b:a 320k -bufsize 16k -af "aresample=48000,atempo=1.0,equalizer=f=125:g=2:q=0.9,equalizer=f=250:g=1:q=0.9,equalizer=f=4000:g=3:q=0.9"'
}

# ═══════════════════════════════════════════════════════════════
# 📝 EMBED TEMPLATES
# ═══════════════════════════════════════════════════════════════

EMBED_ICONS = {
    "music": "🎵",
    "play": "▶️",
    "pause": "⏸️",
    "stop": "⏹️",
    "skip": "⏭️",
    "queue": "📋",
    "volume": "🔊",
    "loop": "🔁",
    "shuffle": "🔀",
    "error": "❌",
    "success": "✅",
    "warning": "⚠️",
    "info": "ℹ️",
    "search": "🔍",
    "loading": "⏳",
    "heart": "❤️",
    "star": "⭐",
    "fire": "🔥",
    "sparkle": "✨",
    "headphones": "🎧",
    "microphone": "🎤",
    "notes": "🎶",
    "cd": "💿",
    "radio": "📻",
}

# ═══════════════════════════════════════════════════════════════
# ⚙️ PERMISSIONS & ROLES
# ═══════════════════════════════════════════════════════════════

DJ_ROLE_NAME = "DJ"
ADMIN_COMMANDS = ["forceskip", "forceplay", "clear", "disconnect", "settings"]

# ═══════════════════════════════════════════════════════════════
# 🎵 LAVALINK NODES (Professional Audio Streaming)
# ═══════════════════════════════════════════════════════════════

LAVALINK_NODES = [
    {
        "uri": "http://node.lewdhutao.my.eu.org:80",
        "password": "youshallnotpass",
        "identifier": "MAIN"
    },
]

# ═══════════════════════════════════════════════════════════════
# 📊 SPOTIFY INTEGRATION (Optional)
# ═══════════════════════════════════════════════════════════════

SPOTIFY_CLIENT_ID = ""  # Add your Spotify client ID
SPOTIFY_CLIENT_SECRET = ""  # Add your Spotify client secret

# ═══════════════════════════════════════════════════════════════
# 🌐 API ENDPOINTS
# ═══════════════════════════════════════════════════════════════

LYRICS_API = "https://api.lyrics.ovh/v1"
GENIUS_API_TOKEN = ""  # Optional: Add Genius API token for better lyrics

# ═══════════════════════════════════════════════════════════════
# 📁 PATHS
# ═══════════════════════════════════════════════════════════════

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")
CACHE_DIR = os.path.join(DATA_DIR, "cache")
PLAYLISTS_DIR = os.path.join(DATA_DIR, "playlists")
LOGS_DIR = os.path.join(DATA_DIR, "logs")

# Create directories if they don't exist
for directory in [DATA_DIR, CACHE_DIR, PLAYLISTS_DIR, LOGS_DIR]:
    os.makedirs(directory, exist_ok=True)

# ═══════════════════════════════════════════════════════════════
# 🔄 STATUS ROTATION
# ═══════════════════════════════════════════════════════════════

BOT_ACTIVITIES = [
    {"type": "listening", "name": "!help | Music 24/7"},
    {"type": "watching", "name": "{guilds} servers"},
    {"type": "listening", "name": "{users} users"},
    {"type": "playing", "name": "🎵 High Quality Music"},
    {"type": "Monitoring", "name": "shlok.kesug.com"},
    {"type": "competing", "name": "music streaming"},
]

# Activity rotation interval (seconds)
ACTIVITY_ROTATION_INTERVAL = 30
