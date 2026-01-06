# 🎵 Shlok Music Bot - UptimeRobot Keep-Alive Setup Guide

## What is UptimeRobot?

UptimeRobot is a **FREE** uptime monitoring service that periodically sends HTTP requests to your bot's web server. This keeps your bot "alive" by:
1. Detecting if it's down
2. Sending regular pings to keep it running
3. Alerting you if there are issues

## Two Methods to Use UptimeRobot

### Method 1: Local Machine with ngrok (Easiest for Testing)
Your bot runs locally, and ngrok creates a public URL that UptimeRobot can access.

### Method 2: Cloud Hosting (Recommended for 24/7)
Deploy your bot to a free/paid cloud service with a public IP.

---

## Method 1: Local Machine + ngrok (Quick Setup)

### Step 1: Install ngrok
```bash
# macOS with Homebrew
brew install ngrok

# Or download from: https://ngrok.com/download
```

### Step 2: Get ngrok API Key
1. Go to https://ngrok.com
2. Sign up (free)
3. Get your auth token from dashboard
4. Run: `ngrok config add-authtoken YOUR_TOKEN_HERE`

### Step 3: Start your bot
```bash
bash bot_manager.sh start
```

### Step 4: Expose bot with ngrok (in a new terminal)
```bash
# Forward port 5000 (where your bot's web server runs)
ngrok http 5000
```

You'll see output like:
```
Forwarding                    https://abc123def456.ngrok.io -> http://localhost:8080
```

**Copy that URL** - you'll need it for UptimeRobot.

### Step 5: Set up UptimeRobot
1. Go to https://uptimerobot.com
2. Sign up (free)
3. Click "Add New Monitor"
4. Select **HTTP(s)**
5. Fill in:
   - **Friendly Name**: `Shlok Music Bot`
   - **URL**: `https://abc123def456.ngrok.io/` (your ngrok URL)
   - **Monitoring Interval**: `5 minutes` (or less)
6. Click "Create Monitor"

Done! UptimeRobot will now ping your bot every 5 minutes to keep it alive.

---

## Method 2: Cloud Hosting (Recommended 24/7)

### Option A: Replit (Easiest, Free)

1. **Go to** https://replit.com
2. **Import from GitHub** or upload your project
3. **Create .replit file**:
```
run = "bash start.sh"
```

4. **Keep Replit tab open** (or use Replit's Always On feature - $7/month)
5. **Get your Replit URL** from the "Run" window
6. **Add to UptimeRobot** (see Step 5 above)

### Option B: Railway (Free tier, simple)

1. **Go to** https://railway.app
2. **Connect GitHub** or upload files
3. **Add Python plugin** and set startup command: `bash start.sh`
4. **Deploy**
5. **Get public URL** from Railway dashboard
6. **Add to UptimeRobot**

### Option C: Heroku (Free tier ending, but still available)

1. Go to https://heroku.com
2. Create account and add credit card
3. Create new app
4. Deploy your code
5. Get public URL
6. Add to UptimeRobot

---

## UptimeRobot Setup (All Methods)

### Create a Monitor:

1. **Log in** to https://uptimerobot.com
2. **Click** "Add New Monitor"
3. **Select Monitor Type**: `HTTP(s)`
4. **Fill in**:
   ```
   Friendly Name:      Shlok Music Bot
   URL:                https://your-url-here/
   Monitoring Interval: 5 minutes
   Alert Contacts:     (optional - email yourself)
   ```
5. **Create Monitor**

### That's it!
UptimeRobot will now ping your bot every 5 minutes, keeping it alive and monitoring uptime.

---

## Status Checks

### View UptimeRobot Dashboard:
- See if bot is online ✅
- View uptime percentage
- Get alerts if bot goes down
- View response times

### View Your Bot Logs:
```bash
tail -f data/logs/bot.log
```

### Check Bot Status Locally:
```bash
bash bot_manager.sh status
```

---

## Troubleshooting

### "Monitor shows DOWN"
1. Check bot is actually running: `bash bot_manager.sh status`
2. Check logs for errors: `bash bot_manager.sh logs`
3. For ngrok: Make sure ngrok is still running
4. For cloud: Check cloud service logs
5. Restart bot: `bash bot_manager.sh restart`

### ngrok URL keeps changing
- Use ngrok **Pro plan** ($5/month) for static URL
- Or use one of the cloud hosting options (URLs are permanent)

### Discord bot not responding even though uptime shows online
- UptimeRobot only monitors the HTTP server (port 8080)
- Discord connection is separate
- Check bot logs: `bash bot_manager.sh logs`

---

## Recommended Setup

**For 24/7 Uptime with Monitoring:**

1. **Choose one**:
   - ✅ Cloud hosting (Railway/Replit) - most reliable
   - ✅ Local + ngrok + keep ngrok running
   - ✅ Local with ngrok Pro ($5/month)

2. **Set up UptimeRobot** to monitor your URL

3. **Enable alerts** if bot goes down

4. **Check logs regularly** to ensure bot is running properly

---

## Quick Reference

```bash
# Start bot
bash bot_manager.sh start

# Start ngrok (separate terminal)
ngrok http 8080

# Check status
bash bot_manager.sh status

# View logs
bash bot_manager.sh logs

# Stop bot
bash bot_manager.sh stop
```

---

## What's Running Now

Your bot has:
- ✅ HTTP web server on port 8080 (for UptimeRobot)
- ✅ Discord bot connection
- ✅ Auto-restart on crashes
- ✅ Logging to `data/logs/bot.log`

Just add UptimeRobot monitoring and you're fully set up! 🚀
