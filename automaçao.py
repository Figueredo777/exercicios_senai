import pyautogui as p
from time import sleep

# p.mouseInfo()

p.press("win")
sleep(1)
p.write("Chrome", interval= 0.2)
p.press("Enter")
p.moveTo(196,59, duration=1 )
p.click()
sleep(1)
p.write("https://www.instagram.com", interval= 0.2)
p.press("Enter")
p.moveTo(1247,360, duration=1)
p.click()
sleep(1)
p.write("gu_figueredo_", interval= 0.2)
p.moveTo(1233,405, duration=1)
p.click()
sleep(1)
p.write("FIGUEREDO2008", interval= 0.2)
p.moveTo(1178,442, duration=1)
p.click()
sleep(1)
p.moveTo(1148,395, duration=3)
sleep(1)
p.click()

