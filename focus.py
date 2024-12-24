import win32api
import win32gui
import win32con
import time



if __name__ == "__main__":
    hwnd = win32gui.FindWindow(None, '魔兽世界')
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x38, 0)
    time.sleep(0.05)
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x38, 0)
