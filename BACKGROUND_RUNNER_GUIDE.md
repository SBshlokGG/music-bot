# 🎵 Shlok Music Bot - 24/7 Background Runner Guide

## The Problem
Your bot was only running when VS Code was open. When you closed VS Code, the bot process ended.

## The Solution
I've created **bot_manager.sh** - a background process manager that keeps your bot running even when VS Code is closed.

---

## Quick Start (Easiest Method)

### 1. Start the bot in background:
```bash
bash bot_manager.sh start
```

**That's it!** The bot is now running in the background. You can close VS Code and the bot will keep running.

---

## Managing Your Bot

### Check if bot is running:
```bash
bash bot_manager.sh status
```

### View logs (last 50 lines):
```bash
bash bot_manager.sh logs
```

### Watch logs in real-time:
```bash
tail -f data/logs/bot.log
```

### Stop the bot:
```bash
bash bot_manager.sh stop
```

### Restart the bot:
```bash
bash bot_manager.sh restart
```

---

## How It Works

1. **bot_manager.sh** - Main control script (use this!)
2. **background_runner.py** - Python runner that detaches from terminal
3. **run.py** - Your bot launcher

The manager script:
- Starts the bot in background using `nohup`
- Saves the bot's process ID (PID)
- Logs all output to `data/logs/bot.log`
- Lets you check status, restart, stop, etc.

---

## Monitoring Your Bot

### View last 50 lines of logs:
```bash
tail -50 data/logs/bot.log
```

### Follow logs in real-time (recommended):
```bash
tail -f data/logs/bot.log
```

### Exit real-time logs:
Press `Ctrl + C`

---

## Troubleshooting

### "Bot is already running"
- Check status: `bash bot_manager.sh status`
- Stop it first: `bash bot_manager.sh stop`
- Then start fresh: `bash bot_manager.sh start`

### Bot not responding
- Check logs: `bash bot_manager.sh logs`
- Restart: `bash bot_manager.sh restart`

### Need to force stop (if stuck):
```bash
bash bot_manager.sh stop
```
Or directly:
```bash
kill -9 $(cat data/logs/bot.pid)
```

---

## Next Steps

1. **Close VS Code**
2. **Start bot**: `bash bot_manager.sh start`
3. **Check status**: `bash bot_manager.sh status`
4. **Close terminal** - bot keeps running!
5. **Monitor anytime**: `bash bot_manager.sh logs` or `tail -f data/logs/bot.log`

---

## Auto-Start on Mac Restart (Optional)

If you want the bot to start automatically when your Mac reboots:

```bash
# Create a LaunchAgent
mkdir -p ~/Library/LaunchAgents
cat > ~/Library/LaunchAgents/com.shlok.music-bot.plist << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>com.shlok.music-bot</string>
    <key>ProgramArguments</key>
    <array>
        <string>bash</string>
        <string>/Users/ishwarbhingaradiya/Desktop/Shlok/bot_manager.sh</string>
        <string>start</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
</dict>
</plist>
EOF

# Load it:
launchctl load ~/Library/LaunchAgents/com.shlok.music-bot.plist
```

---

## Summary

✅ Bot runs 24/7 in background  
✅ VS Code can be closed  
✅ Easy to start/stop/monitor  
✅ Logs saved for debugging  
✅ Auto-restart on crashes (via run.py)  

**Start your bot now:**
```bash
bash bot_manager.sh start
```
