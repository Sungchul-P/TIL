import subprocess
import pyautogui
import time

# kakao = subprocess.Popen(['python', 'pyautogui_basic_1.py'])
kakao = subprocess.Popen(['C:\\Program Files (x86)\\Kakao\\KakaoTalk\\KakaoTalk.exe'])
time.sleep(3)

# 계정 정보를 따로 저장해 두고 import 해서 사용한다.
from myid import ID, PW

pyautogui.typewrite(ID)
pyautogui.press('tab')
pyautogui.typewrite(PW)
pyautogui.press('enter')