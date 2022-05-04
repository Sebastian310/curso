import pyautogui as robot
import time

Cmder=(56,806)
academico=(47,40)
academico2=(381,353)
academico3=(349,729)
miniaca=(1744,15)
headvisual=(1014,20)
dragtovisual=(1919,490)
afterdrag=(326,572)
wait=2

def open(position,clic=2):
    robot.moveTo(position)
    robot.click(clic)

robot.alert("¡Estoy Tostado, revisar Código CLick!", "Mensaje Acualizado desde ultomo codgo")

#Open Cmder
open(Cmder)

robot.hotkey("Ctrl+Space")
robot.typewrite("Cd D:\ACADEMICO\BIG_DATA\Python\Python_intermedio\curso")
time.sleep(wait)
robot.typewrite("code")
robot.hotkey("enter")


