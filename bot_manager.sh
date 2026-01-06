#!/bin/bash

# ╔══════════════════════════════════════════════════════════════╗
# ║     🎵 Shlok Music Bot - Background Manager Script 🎵         ║
# ╚══════════════════════════════════════════════════════════════╝

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LOG_FILE="$SCRIPT_DIR/data/logs/bot.log"
PID_FILE="$SCRIPT_DIR/data/logs/bot.pid"

echo -e "${PURPLE}╔══════════════════════════════════════════════════════════════╗${NC}"
echo -e "${PURPLE}║        🎵  S H L O K   M U S I C   B O T  🎵               ║${NC}"
echo -e "${PURPLE}║         Background Manager & Process Control               ║${NC}"
echo -e "${PURPLE}╚══════════════════════════════════════════════════════════════╝${NC}"
echo ""

# Function to start bot
start_bot() {
    echo -e "${CYAN}Starting bot in background...${NC}"
    mkdir -p "$SCRIPT_DIR/data/logs" "$SCRIPT_DIR/data/cache" "$SCRIPT_DIR/data/playlists"
    
    if [ -f "$PID_FILE" ]; then
        PID=$(cat "$PID_FILE")
        if kill -0 "$PID" 2>/dev/null; then
            echo -e "${RED}❌ Bot is already running (PID: $PID)${NC}"
            echo -e "${YELLOW}   To stop: bash bot_manager.sh stop${NC}"
            return 1
        fi
    fi
    
    # Start in background with nohup
    nohup python3 "$SCRIPT_DIR/run.py" >> "$LOG_FILE" 2>&1 &
    NEW_PID=$!
    
    echo $NEW_PID > "$PID_FILE"
    sleep 1
    
    if kill -0 $NEW_PID 2>/dev/null; then
        echo -e "${GREEN}✅ Bot started successfully!${NC}"
        echo -e "${CYAN}   PID: $NEW_PID${NC}"
        echo -e "${CYAN}   Logs: $LOG_FILE${NC}"
        echo -e "${CYAN}   View logs: tail -f \"$LOG_FILE\"${NC}"
        return 0
    else
        echo -e "${RED}❌ Failed to start bot${NC}"
        cat "$LOG_FILE" | tail -20
        return 1
    fi
}

# Function to stop bot
stop_bot() {
    if [ ! -f "$PID_FILE" ]; then
        echo -e "${YELLOW}⚠️  No running bot found${NC}"
        return 1
    fi
    
    PID=$(cat "$PID_FILE")
    
    if ! kill -0 "$PID" 2>/dev/null; then
        echo -e "${YELLOW}⚠️  Bot is not running (stale PID file)${NC}"
        rm -f "$PID_FILE"
        return 1
    fi
    
    echo -e "${CYAN}Stopping bot (PID: $PID)...${NC}"
    kill -TERM "$PID"
    
    # Wait for graceful shutdown
    for i in {1..10}; do
        if ! kill -0 "$PID" 2>/dev/null; then
            echo -e "${GREEN}✅ Bot stopped successfully${NC}"
            rm -f "$PID_FILE"
            return 0
        fi
        sleep 0.5
    done
    
    # Force kill if needed
    echo -e "${YELLOW}Forcing shutdown...${NC}"
    kill -9 "$PID"
    rm -f "$PID_FILE"
    echo -e "${GREEN}✅ Bot force-stopped${NC}"
    return 0
}

# Function to check status
check_status() {
    if [ ! -f "$PID_FILE" ]; then
        echo -e "${RED}❌ Bot is not running${NC}"
        return 1
    fi
    
    PID=$(cat "$PID_FILE")
    
    if kill -0 "$PID" 2>/dev/null; then
        echo -e "${GREEN}✅ Bot is running${NC}"
        echo -e "${CYAN}   PID: $PID${NC}"
        echo -e "${CYAN}   Memory: $(ps -o rss= -p $PID | awk '{printf "%.1f MB", $1/1024}')${NC}"
        echo -e "${CYAN}   CPU: $(ps -o %cpu= -p $PID)%${NC}"
        return 0
    else
        echo -e "${RED}❌ Bot is not running (stale PID file)${NC}"
        rm -f "$PID_FILE"
        return 1
    fi
}

# Function to view logs
view_logs() {
    if [ ! -f "$LOG_FILE" ]; then
        echo -e "${YELLOW}⚠️  No logs found${NC}"
        return 1
    fi
    
    echo -e "${CYAN}=== BOT LOGS (last 50 lines) ===${NC}"
    tail -50 "$LOG_FILE"
    echo ""
    echo -e "${CYAN}To follow logs in real-time: tail -f \"$LOG_FILE\"${NC}"
}

# Function to restart bot
restart_bot() {
    echo -e "${CYAN}Restarting bot...${NC}"
    stop_bot
    sleep 2
    start_bot
}

# Main menu
case "${1:-menu}" in
    start)
        start_bot
        ;;
    stop)
        stop_bot
        ;;
    restart)
        restart_bot
        ;;
    status)
        check_status
        ;;
    logs)
        view_logs
        ;;
    *)
        echo -e "${BLUE}Usage:${NC}"
        echo -e "  bash bot_manager.sh ${GREEN}start${NC}     - Start bot in background"
        echo -e "  bash bot_manager.sh ${GREEN}stop${NC}      - Stop the running bot"
        echo -e "  bash bot_manager.sh ${GREEN}restart${NC}   - Restart the bot"
        echo -e "  bash bot_manager.sh ${GREEN}status${NC}    - Check if bot is running"
        echo -e "  bash bot_manager.sh ${GREEN}logs${NC}      - View bot logs"
        echo ""
        echo -e "${BLUE}Quick Start:${NC}"
        echo -e "  ${GREEN}bash bot_manager.sh start${NC}     # Start bot in background"
        echo -e "  ${GREEN}tail -f $LOG_FILE${NC} # Watch logs"
        echo ""
        check_status
        ;;
esac
