# pip install pyautogui==0.9.39

import pyautogui

# 활성화 시킬 창의 좌표 클릭
pyautogui.click(346, 24)

# 활성화 된 상태의 전체 스크린샷이 필요하다.
# pyautogui.click(346, 24); pyautogui.screenshot('test.png')

# 전체 화면에서 클릭할 부분의 이미지를 부분 저장한다.
x, y = pyautogui.locateCenterOnScreen('1.png')
pyautogui.click(x, y)

x, y = pyautogui.locateCenterOnScreen('+.png')
pyautogui.click(x, y)

x, y = pyautogui.locateCenterOnScreen('3.png')
pyautogui.click(x, y)
pyautogui.press('enter')