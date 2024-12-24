import numpy as np
import pyaudio
import win32api
import win32gui
import win32con
import time
audio = pyaudio.PyAudio()

def sound_listener():
    hwnd = win32gui.FindWindow(None, '魔兽世界')
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK,
                    )
    flag = 0
    timeStep = 0
    max = 500
    min = 200
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x38, 0)
    time.sleep(0.05)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0x38, 0)
    while True:
        data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
        if np.abs(data).mean() < min:
            timeStep += 1
        if np.abs(data).mean() > max or timeStep > 800:  # 设置声音阈值
            if flag == 0:
                print("钓到鱼了！", np.abs(data).mean())
                time.sleep(1)
                win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x39, 0)
                time.sleep(0.05)
                win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0x39, 0)
                time.sleep(1)
                # pyautogui.press('space')
                # time.sleep(1)
                # img = pyautogui.screenshot(region=[0, 0, 300, 150])
                # img = cv2.cvtColor(np.asarray(img), cv2.COLOR_BGRA2BGR)
                # pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
                # cv2.imshow('image', img)
                # cv2.waitKey(0)
                #
                # fish = pytesseract.image_to_string(img, lang='chi_sim')
                # print(fish)
                # if 'B' in fish:
                #     print("检测到wa标记,钓到锤头鲨了，自动补充buff")
                #     pyautogui.press('0')
                win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x38, 0)
                time.sleep(0.05)
                win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0x38, 0)
                flag = 10
                timeStep = 0
            if timeStep > 800:
                print("很长时间没有上钩了！")
                time.sleep(1)
                win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x39, 0)
                time.sleep(0.05)
                win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0x39, 0)
                time.sleep(2)
                # pyautogui.press('space')
                # time.sleep(1)
                win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, 0x38, 0)
                time.sleep(0.05)
                win32api.PostMessage(hwnd, win32con.WM_KEYUP, 0x38, 0)
                flag = 5
                timeStep = 0
            if flag != 0:
                flag = flag - 1


if __name__ == "__main__":
   sound_listener()

