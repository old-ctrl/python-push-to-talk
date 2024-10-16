import ctypes, keyboard, time

def toggle_mic(mute):
    APPCOMMAND_MICROPHONE_VOLUME_MUTE = 0x180000
    WM_APPCOMMAND = 0x319
    hwnd = ctypes.windll.user32.GetForegroundWindow()
    ctypes.windll.user32.SendMessageW(hwnd, WM_APPCOMMAND, 0, APPCOMMAND_MICROPHONE_VOLUME_MUTE)
    print("Microphone", "muted." if mute else "unmuted.")

def push_to_talk():
    mic_is_muted = True
    toggle_mic(True)
    while True:
        if keyboard.is_pressed('j') and mic_is_muted:
            toggle_mic(False)
            mic_is_muted = False
        elif not keyboard.is_pressed('j') and not mic_is_muted:
            toggle_mic(True)
            mic_is_muted = True
        time.sleep(0.1)

if __name__ == "__main__":
    push_to_talk()
# lol ez
