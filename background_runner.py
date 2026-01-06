#!/usr/bin/env python3
"""
🎵 Shlok Music Bot - Background Runner
This script runs the bot in the background and detaches from terminal
"""

import subprocess
import sys
import os
import time
import signal

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def run_in_background():
    """Run the bot in background using nohup"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Create logs directory if it doesn't exist
    logs_dir = os.path.join(script_dir, 'data', 'logs')
    os.makedirs(logs_dir, exist_ok=True)
    
    log_file = os.path.join(logs_dir, 'bot.log')
    pid_file = os.path.join(logs_dir, 'bot.pid')
    
    # Check if bot is already running
    if os.path.exists(pid_file):
        try:
            with open(pid_file, 'r') as f:
                old_pid = int(f.read().strip())
            
            # Try to check if process is still running
            os.kill(old_pid, 0)
            print(f"❌ Bot is already running (PID: {old_pid})")
            print(f"   To stop it, run: kill {old_pid}")
            return
        except (ProcessLookupError, ValueError, FileNotFoundError):
            # Process is not running, continue
            pass
    
    # Start the bot in background
    print("🚀 Starting Shlok Music Bot in background...")
    print(f"📝 Logs will be saved to: {log_file}")
    
    try:
        # Start process in background
        process = subprocess.Popen(
            [sys.executable, 'run.py'],
            cwd=script_dir,
            stdout=open(log_file, 'a'),
            stderr=subprocess.STDOUT,
            preexec_fn=os.setpgrp if sys.platform != 'win32' else None,
            start_new_session=True if sys.platform != 'win32' else False
        )
        
        # Save PID
        with open(pid_file, 'w') as f:
            f.write(str(process.pid))
        
        print(f"✅ Bot started successfully!")
        print(f"   PID: {process.pid}")
        print(f"   To view logs: tail -f {log_file}")
        print(f"   To stop bot: kill {process.pid}")
        
        return process.pid
        
    except Exception as e:
        print(f"❌ Failed to start bot: {e}")
        sys.exit(1)


def stop_bot():
    """Stop the running bot"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    pid_file = os.path.join(script_dir, 'data', 'logs', 'bot.pid')
    
    if not os.path.exists(pid_file):
        print("⚠️  No running bot found")
        return
    
    try:
        with open(pid_file, 'r') as f:
            pid = int(f.read().strip())
        
        print(f"Stopping bot (PID: {pid})...")
        os.kill(pid, signal.SIGTERM)
        
        # Wait a bit for graceful shutdown
        for i in range(5):
            try:
                os.kill(pid, 0)
                time.sleep(0.5)
            except ProcessLookupError:
                print("✅ Bot stopped successfully")
                os.remove(pid_file)
                return
        
        # Force kill if needed
        os.kill(pid, signal.SIGKILL)
        print("✅ Bot force-stopped")
        os.remove(pid_file)
        
    except Exception as e:
        print(f"❌ Error stopping bot: {e}")


def check_status():
    """Check if bot is running"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    pid_file = os.path.join(script_dir, 'data', 'logs', 'bot.pid')
    
    if not os.path.exists(pid_file):
        print("⚠️  Bot is not running")
        return False
    
    try:
        with open(pid_file, 'r') as f:
            pid = int(f.read().strip())
        
        os.kill(pid, 0)
        print(f"✅ Bot is running (PID: {pid})")
        return True
    except (ProcessLookupError, ValueError):
        print("⚠️  Bot is not running (stale PID file)")
        try:
            os.remove(pid_file)
        except:
            pass
        return False


if __name__ == "__main__":
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        if command == "stop":
            stop_bot()
        elif command == "status":
            check_status()
        else:
            print(f"Unknown command: {command}")
            print("Usage: python background_runner.py [start|stop|status]")
    else:
        run_in_background()
