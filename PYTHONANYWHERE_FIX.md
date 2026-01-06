# 🔧 Fix: Discord Bot Not Online Despite Flask App Running

## The Problem
- ✅ Flask app is running on PythonAnywhere 
- ❌ Discord bot is NOT online in Discord

## Why This Happens
The Flask app tries to start the Discord bot in a background thread, but:
1. PythonAnywhere kills background processes when the web app reloads
2. Discord.py's async event loop doesn't work well in Flask threads
3. The bot process isn't being properly managed

## ✅ Solution: Use PythonAnywhere Always-On Task

### Step 1: Verify Bot Code is Uploaded
SSH/Bash into PythonAnywhere and check:
```bash
ls -la ~/shlok_bot/
# Should show: bot.py, config.py, cogs/, core/, utils/, requirements.txt, etc.
```

### Step 2: Create Simple Bot Wrapper
Create `/home/shlokb125/shlok_bot/run_bot.py`:
```python
#!/usr/bin/env python3
"""
Simple bot runner - use this for PythonAnywhere always-on task
"""

import subprocess
import sys
import os

if __name__ == '__main__':
    os.chdir('/home/shlokb125/shlok_bot')
    
    # Run bot indefinitely
    while True:
        try:
            print("🚀 Starting Discord bot...")
            result = subprocess.run([sys.executable, 'bot.py'], check=False)
            print(f"⚠️ Bot exited with code {result.returncode}, restarting...")
        except Exception as e:
            print(f"❌ Error: {e}")
```

### Step 3: Set Up Always-On Task
1. Go to **PythonAnywhere** → **Web** tab
2. Look for **"Always-on task"** or **"Scheduled tasks"**
3. Click **"Add a new always-on task"**
4. Set command to:
```
/usr/bin/python3.10 /home/shlokb125/shlok_bot/run_bot.py
```

### Step 4: Keep Flask App for Health Checks
The Flask app should just serve health checks, NOT try to start the bot:

Replace `/home/shlokb125/mysite/flask_app.py` with:
```python
from flask import Flask, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({'status': 'online', 'bot': 'Shlok Music'}), 200

@app.route('/health')
def health():
    return jsonify({'status': 'online', 'timestamp': datetime.now().isoformat()}), 200

@app.route('/ping')
def ping():
    return jsonify({'status': 'pong'}), 200
```

### Step 5: Check Bot Logs
In **Bash Console**:
```bash
tail -f ~/shlok_bot/data/logs/bot_*.log
```

## Expected Result
- ✅ Flask app responds to `/health` 
- ✅ Discord bot shows online in Discord
- ✅ Both run independently

## Alternative: Direct Bot Approach
If "Always-on task" isn't available on free plan, try:

1. **Use cron job** (if available):
```bash
*/5 * * * * cd ~/shlok_bot && python3.10 -c "import subprocess; subprocess.Popen(['/usr/bin/python3.10', 'bot.py'])"
```

2. **Use nohup via Bash Console**:
```bash
cd ~/shlok_bot
nohup python3.10 bot.py > data/logs/bot.log 2>&1 &
```

## Checklist
- [ ] Bot code uploaded to `~/shlok_bot/`
- [ ] `requirements.txt` dependencies installed
- [ ] Flask app deployed and responding
- [ ] Always-on task created OR bot started manually
- [ ] Check `/health` endpoint returns 200
- [ ] Check bot appears online in Discord
- [ ] Set up UptimeRobot to ping `/health` every 5 min
