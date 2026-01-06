"""
PythonAnywhere Web Wrapper for Shlok Music Bot
Provides HTTP endpoint for UptimeRobot monitoring

INSTRUCTIONS:
1. Upload this file to: /home/yourusername/mysite/flask_app.py
2. Replace 'yourusername' with your actual PythonAnywhere username
3. Keep your bot.py and other files in: /home/yourusername/shlok_bot/
4. Reload web app when done
"""

from flask import Flask, jsonify
from datetime import datetime
import subprocess
import threading
import os
import sys
import time

app = Flask(__name__)

# Global variables to track bot status
bot_process = None
bot_started = False
bot_start_time = None
last_health_check = None

def start_discord_bot():
    """Start the Discord bot in background"""
    global bot_process, bot_started, bot_start_time
    
    try:
        # Change to bot directory
        os.chdir('/home/yourusername/shlok_bot')  # ⚠️ CHANGE 'yourusername'
        
        print("=" * 60)
        print("🚀 Starting Shlok Music Bot...")
        print("=" * 60)
        
        # Start bot process
        bot_process = subprocess.Popen(
            [sys.executable, 'bot.py'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            cwd='/home/yourusername/shlok_bot'  # ⚠️ CHANGE 'yourusername'
        )
        
        bot_started = True
        bot_start_time = datetime.now()
        print(f"✅ Discord bot process started (PID: {bot_process.pid})")
        
    except Exception as e:
        print(f"❌ Failed to start bot: {e}")
        bot_started = False

# Start bot when Flask app loads (in background thread)
print("🔧 Flask app initializing...")
start_thread = threading.Thread(target=start_discord_bot, daemon=True)
start_thread.start()

# ═══════════════════════════════════════════════════════════════
# 🌐 HTTP ENDPOINTS FOR UPTIMEROBOT
# ═══════════════════════════════════════════════════════════════

@app.route('/health')
def health():
    """
    Health check endpoint for UptimeRobot
    UptimeRobot pings this every 5 minutes to keep bot alive
    """
    global last_health_check
    last_health_check = datetime.now()
    
    uptime = "Starting..." if bot_start_time is None else str(datetime.now() - bot_start_time)
    
    return jsonify({
        'status': 'online',
        'bot': 'Shlok Music',
        'bot_running': bot_started,
        'timestamp': datetime.now().isoformat(),
        'uptime': uptime,
        'hosting': 'PythonAnywhere',
        'monitoring': 'UptimeRobot'
    }), 200

@app.route('/ping')
def ping():
    """Simple ping endpoint"""
    return jsonify({'status': 'pong', 'timestamp': datetime.now().isoformat()}), 200

@app.route('/status')
def status():
    """Detailed bot status"""
    return jsonify({
        'web_server': 'online',
        'discord_bot': 'online' if bot_started else 'offline',
        'bot_process_id': bot_process.pid if bot_process else None,
        'last_health_check': last_health_check.isoformat() if last_health_check else None,
        'uptime': str(datetime.now() - bot_start_time) if bot_start_time else 'Not started'
    }), 200

@app.route('/')
def home():
    """Home page with status information"""
    status_icon = '✅' if bot_started else '⚠️'
    
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>🎵 Shlok Music Bot - PythonAnywhere</title>
        <style>
            * {{ margin: 0; padding: 0; box-sizing: border-box; }}
            
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                padding: 20px;
            }}
            
            .container {{
                text-align: center;
                padding: 50px;
                background: rgba(0, 0, 0, 0.3);
                border-radius: 20px;
                max-width: 600px;
                backdrop-filter: blur(10px);
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
            }}
            
            h1 {{
                font-size: 3.5em;
                margin-bottom: 10px;
                text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
            }}
            
            .subtitle {{
                font-size: 1.3em;
                opacity: 0.9;
                margin-bottom: 30px;
            }}
            
            .status-badge {{
                background: #2ecc71;
                padding: 15px 40px;
                border-radius: 50px;
                display: inline-block;
                margin: 20px 0;
                font-weight: bold;
                font-size: 1.1em;
                box-shadow: 0 4px 15px rgba(46, 204, 113, 0.4);
            }}
            
            .info-box {{
                background: rgba(255, 255, 255, 0.1);
                padding: 25px;
                border-radius: 15px;
                margin-top: 30px;
                border-left: 4px solid #2ecc71;
            }}
            
            .info-item {{
                margin: 15px 0;
                font-size: 1em;
            }}
            
            .label {{
                font-weight: bold;
                opacity: 0.8;
            }}
            
            .value {{
                opacity: 0.9;
                margin-top: 5px;
            }}
            
            .endpoints {{
                background: rgba(255, 255, 255, 0.05);
                padding: 20px;
                border-radius: 10px;
                margin-top: 20px;
                text-align: left;
                font-size: 0.9em;
            }}
            
            .endpoint {{
                margin: 10px 0;
                padding: 10px;
                background: rgba(0, 0, 0, 0.2);
                border-radius: 5px;
                font-family: monospace;
            }}
            
            a {{
                color: #fff;
                text-decoration: none;
                border-bottom: 1px solid rgba(255, 255, 255, 0.3);
            }}
            
            a:hover {{
                border-bottom: 1px solid white;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎵 Shlok Music Bot</h1>
            <p class="subtitle">High-Quality Discord Music Streaming</p>
            
            <div class="status-badge">
                {status_icon} Status: {'Online' if bot_started else 'Initializing...'}
            </div>
            
            <div class="info-box">
                <div class="info-item">
                    <div class="label">🌐 Hosting</div>
                    <div class="value">PythonAnywhere (24/7)</div>
                </div>
                
                <div class="info-item">
                    <div class="label">📊 Monitoring</div>
                    <div class="value">UptimeRobot</div>
                </div>
                
                <div class="info-item">
                    <div class="label">🤖 Discord Bot</div>
                    <div class="value">{'Running' if bot_started else 'Starting...'}</div>
                </div>
                
                <div class="info-item">
                    <div class="label">⏰ Time</div>
                    <div class="value">{datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}</div>
                </div>
            </div>
            
            <div class="endpoints">
                <strong>API Endpoints:</strong>
                <div class="endpoint">📍 <a href="/health">/health</a> - UptimeRobot monitoring</div>
                <div class="endpoint">📍 <a href="/ping">/ping</a> - Simple ping test</div>
                <div class="endpoint">📍 <a href="/status">/status</a> - Detailed status JSON</div>
            </div>
        </div>
    </body>
    </html>
    """
    return html, 200

# ═══════════════════════════════════════════════════════════════
# ERROR HANDLERS
# ═══════════════════════════════════════════════════════════════

@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'error': 'Not found',
        'message': 'This endpoint does not exist'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        'error': 'Internal server error',
        'message': str(error)
    }), 500

# ═══════════════════════════════════════════════════════════════
# APP CONFIG
# ═══════════════════════════════════════════════════════════════

if __name__ == '__main__':
    app.run(debug=False)
