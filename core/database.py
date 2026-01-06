"""
💎 Premium Bot Database Module
Advanced database system for user profiles and statistics
"""

import sqlite3
import logging

logger = logging.getLogger('ShlokMusic.Database')

class BotDatabase:
    """Advanced database manager"""
    
    def __init__(self, db_path: str = "data/shlok_premium.db"):
        self.db_path = db_path
        self.init_db()
    
    def init_db(self):
        """Initialize database"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # User Profiles
            cursor.execute("""CREATE TABLE IF NOT EXISTS user_profiles (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                songs_played INTEGER DEFAULT 0,
                total_listen_time INTEGER DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )""")
            
            # User Preferences
            cursor.execute("""CREATE TABLE IF NOT EXISTS user_preferences (
                user_id INTEGER PRIMARY KEY,
                audio_preset TEXT DEFAULT 'crystalclear',
                quality_mode TEXT DEFAULT 'high',
                volume_level INTEGER DEFAULT 100,
                auto_dj BOOLEAN DEFAULT 1
            )""")
            
            conn.commit()
            conn.close()
            logger.info("✅ Database initialized")
        except Exception as e:
            logger.error(f"❌ Database error: {e}")


# Global database instance
db = BotDatabase()
