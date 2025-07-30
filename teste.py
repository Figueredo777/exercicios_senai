import pyautogui as p
from time import sleep


# p.mouseInfo()



p.press('win')
sleep(1)
p.write('Chrome')
p.press('enter')
p.moveTo(954,582, duration=1)
p.click()
sleep(1)
p.write('www.youtube.com', interval=0.5)
p.press('enter')
sleep(1)
p.moveTo(832,115,duration=1)
p.click()
p.write('Tutorial Python Pyautogui', interval=0.5)
p.press('enter')