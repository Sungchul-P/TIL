# pip install pyautogui==0.9.39

import pyautogui

#####################################################################

# pos_x, pos_y = pyautogui.position() # 마우스의 현재 좌표 출력(튜플 형식)
# pyautogui.moveTo(pos_x, pos_y)
# pyautogui.moveTo(100, 200) # 절대 좌표(PC 해상도를 기준으로 계산된다.)
# pyautogui.click()
# pyautogui.moveRel(200, 100) # 현재 위치 기준 상대 좌표

#####################################################################

# pyautogui.moveTo(596, 175)
# pyautogui.click()
# pyautogui.typewrite('abcd') # 한글입력 안 됨. abcd 위치의 키보드를 입력할 뿐이다.
# pyautogui.press('enter')

#####################################################################

pyautogui.screenshot('result.png')