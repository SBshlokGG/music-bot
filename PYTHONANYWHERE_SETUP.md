# 🎵 Shlok Music Bot - PythonAnywhere Setup Guide

**Complete FREE hosting with 24/7 uptime + UptimeRobot monitoring**

---

## **Step 1: Create PythonAnywhere Account**

1. Go to https://www.pythonanywhere.com
2. Click **"Sign up"**
3. Create free account (no credit card needed)
4. Verify email

---

## **Step 2: Upload Your Bot Code**

### Option A: Upload via Web Interface (Easiest)

1. Log in to PythonAnywhere
2. Click **"Files"** tab
3. Create folder: `/home/yourusername/shlok_bot/`
4. Upload all your files:
   - `bot.py`
   - `config.py`
   - `requirements.txt`
   - `cogs/` (entire folder)
   - `core/` (entire folder)
   - `utils/` (entire folder)
   - `data/` (entire folder)

### Option B: Upload via GitHub (Better)

1. Click **"Files"**
2. Click **"Open Bash Console"**
3. Run:
```bash
git clone https://github.com/yourusername/your-repo.git ~/shlok_bot
cd ~/shlok_bot
```

---

## **Step 3: Install Requirements**

1. Click **"Bash Console"** (or use existing)
2. Run:
```bash
cd ~/shlok_bot
pip install --user -r requirements.txt
```

This installs all dependencies: discord.py, yt-dlp, aiohttp, etc.

---

## **Step 4: Create Web App (for HTTP Endpoint)**

PythonAnywhere needs a web app for UptimeRobot to ping.

1. Click **"Web"** tab
2. Click **"Add a new web app"**
3. Choose:
   - Domain: `yourusername.pythonanywhere.com` (auto)
   - Framework: **Flask**
   - Python: **3.10** or higher
4. PythonAnywhere creates: `/home/yourusername/mysite/flask_app.py`

---

## **Step 5: Replace Flask App Code**

Go to **"Web"** → **"Code"** → Click on `/home/yourusername/mysite/flask_app.py`

Replace entire content with:

```python
"""
PythonAnywhere Web Wrapper for Shlok Music Bot
Provides HTTP endpoint for UptimeRobot monitoring
"""

from flask import Flask, jsonify
from datetime import datetime
import subprocess
import threading
import os
import sys

app = Flask(__name__)

# Global flag to track if bot is running
bot_process = None
bot_started = False

def start_discord_bot():
    """Start the Discord bot in background"""
    global bot_process, bot_started
    
    try:
        # Change to bot directory
        os.chdir('/home/yourusername/shlok_bot')
        
        # Start bot process
        bot_process = subprocess.Popen(
            [sys.executable, 'bot.py'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        bot_started = True
        print("✅ Discord bot started successfully")
        
    except Exception as e:
        print(f"❌ Failed to start bot: {e}")
        bot_started = False

# Start bot when Flask app loads
threading.Thread(target=start_discord_bot, daemon=True).start()

# ═══════════════════════════════════════════════════════════════
# 🌐 HTTP ENDPOINTS
# ═══════════════════════════════════════════════════════════════

@app.route('/health')
def health():
    """Health check endpoint for UptimeRobot"""
    return jsonify({
        'status': 'online',
        'bot': 'Shlok Music',
        'timestamp': datetime.now().isoformat(),
        'uptime': 'Always on PythonAnywhere'
    }), 200

@app.route('/ping')
def ping():
    """Ping endpoint"""
    return jsonify({'status': 'pong'}), 200

@app.route('/')
def home():
    """Home page"""
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>🎵 Shlok Music Bot</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }
            .container {
                text-align: center;
                padding: 40px;
                background: rgba(0,0,0,0.3);
                border-radius: 20px;
                max-width: 600px;
            }
            h1 { font-size: 3em; margin-bottom: 10px; }
            p { font-size: 1.2em; opacity: 0.9; margin: 10px 0; }
            .status {
                background: #2ecc71;
                padding: 10px 30px;
                border-radius: 50px;
                display: inline-block;
                margin-top: 20px;
                font-weight: bold;
            }
            .info {
                background: rgba(255,255,255,0.1);
                padding: 20px;
                border-radius: 10px;
                margin-top: 20px;
                font-size: 0.9em;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎵 Shlok Music Bot</h1>
            <p>High-Quality Discord Music Streaming</p>
            <div class="status">✅ Online</div>
            <div class="info">
                <p><strong>Hosted on:</strong> PythonAnywhere</p>
                <p><strong>Monitored by:</strong> UptimeRobot</p>
                <p><strong>Status:</strong> 24/7 Always On</p>
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
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run()
```

**⚠️ IMPORTANT:** Replace `yourusername` with your actual PythonAnywhere username!

---

## **Step 6: Install Flask (if not already installed)**

In Bash Console:
```bash
pip install --user flask
```

---

## **Step 7: Reload Web App**

1. Go to **"Web"** tab
2. Scroll down to your web app
3. Click **"Reload"** button (green button)
4. Wait 10 seconds

---

## **Step 8: Verify It's Working**

1. Go to your URL: `https://yourusername.pythonanywhere.com`
2. You should see the bot status page ✅
3. Test health endpoint: `https://yourusername.pythonanywhere.com/health`
4. Should return JSON with status

---

## **Step 9: Add to UptimeRobot**

1. Go to https://uptimerobot.com
2. Sign up (free)
3. Click **"Add New Monitor"**
4. Fill in:
   ```
   Monitor Type:       HTTP(s)
   Friendly Name:      Shlok Music Bot
   URL:                https://yourusername.pythonanywhere.com/health
   Monitoring Interval: 5 minutes
   Alert Contacts:     (optional - your email)
   ```
5. Click **"Create Monitor"**

---

## **Step 10: Check If Bot is Running**

### Check Web Server Logs:
1. Go to **"Web"** tab
2. Click on **"Error Log"** - should be empty
3. Click on **"Server Log"** - should show requests

### Check Discord Bot Logs:
1. Go to **"Files"**
2. Navigate to `shlok_bot/data/logs/`
3. View recent log files

---

## **Step 11: Monitor Everything**

**UptimeRobot Dashboard:**
- Shows bot status ✅ UP or ❌ DOWN
- Shows response times
- Sends alerts if down

**PythonAnywhere Dashboard:**
- Monitor CPU usage
- Monitor memory
- View logs
- Reload if needed

---

## **Troubleshooting**

### **"Bot URL shows DOWN in UptimeRobot"**
1. Check URL is correct: `https://yourusername.pythonanywhere.com/health`
2. Check web app is reloaded
3. Check web app error log for issues
4. Wait 5 minutes for UptimeRobot to retry

### **"Discord bot not responding but web server is online"**
1. Check Discord bot logs: `shlok_bot/data/logs/`
2. Check token in config.py is correct
3. Check bot has Discord intents enabled
4. Restart bot: Stop background task and reload web app

### **"Running out of CPU/memory"**
1. PythonAnywhere free tier: 100 CPU seconds/day
2. If exceeded, wait until next day (quota resets)
3. Or upgrade to paid plan for unlimited

### **"File upload failed"**
1. Use Bash Console instead: `git clone` your repo
2. Or split uploads into smaller batches

---

## **Important: Keep Web App Running**

Your web app must stay **"Running"** for monitoring to work.

✅ **Running** = web server is on = UptimeRobot can ping it  
❌ **Stopped** = web server is off = UptimeRobot sees it as DOWN

To keep it running:
- Keep at least 1 web app active
- Free tier: Web apps go to sleep after 3 months inactivity
- UptimeRobot pinging every 5 min keeps it active

---

## **Quick Reference**

```bash
# Bash Console commands
cd ~/shlok_bot
pip install --user discord.py yt-dlp aiohttp
python bot.py                    # Test bot locally
cat data/logs/bot.log           # View bot logs
```

**Web App:**
- **Files:** `/home/yourusername/mysite/flask_app.py`
- **URL:** `https://yourusername.pythonanywhere.com`
- **Health Check:** `https://yourusername.pythonanywhere.com/health`

---

## **Final Checklist**

- [ ] PythonAnywhere account created
- [ ] Bot files uploaded
- [ ] Requirements installed
- [ ] Web app created (Flask)
- [ ] Flask app code replaced
- [ ] Web app reloaded
- [ ] Home page loads at `https://yourusername.pythonanywhere.com`
- [ ] Health endpoint works at `/health`
- [ ] UptimeRobot monitor created
- [ ] UptimeRobot shows **✅ UP**

---

## **You're Done! 🎉**

Your bot is now:
- ✅ **24/7 Online** on PythonAnywhere
- ✅ **Monitored** by UptimeRobot
- ✅ **Free** (no credit card)
- ✅ **Always Running** (no PC needed)

Enjoy! 🎵

