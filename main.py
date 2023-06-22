
from botaria import hold_key, focus_terraria, select_slot, left_click, check_spawn, time, scan_qrcode, pyautogui 
from botaria import *

def farm_setup():
    select_slot(1)
    left_click()
    time.sleep(1)
    
    if scan_qrcode() != QR_FARM:
        print(scan_qrcode())
        print("QR code not found, exiting...")
        exit()
    hold_key('r')
        

def do_layer(side, harvest=True):
    
    #side == 0 right
    #side == 1 left
    pyautogui.mouseDown()
    pyautogui.keyDown( 'a' if side else 'd')
    time.sleep(5)
    pyautogui.mouseUp()
    pyautogui.keyUp('a' if side else 'd')
    
        
    
    

focus_terraria()
time.sleep(1)
farm_setup()
reset_cursor()


for i in range(1):
    do_layer(i%2)
    
    # with pyautogui.hold(r):
    #     pyautogui.sleep(2)

    
    
    
    