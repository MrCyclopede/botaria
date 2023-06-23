from botaria import (
    hold_key,
    focus_terraria,
    select_slot,
    left_click,
    check_spawn,
    time,
    scan_qrcode,
    pyautogui,
    cursor_move,
    reset_cursor,
    QR_FARM,
)
from botaria import *
import pyautogui


FARM_LAYERS = 8

def is_farm_aligned():
    return scan_qrcode() == QR_FARM


def farm_setup():
    select_slot(1)
    left_click()
    time.sleep(1)

    if not is_farm_aligned():
        print(scan_qrcode())
        print("QR code not found, exiting...")
        exit()
    hold_key("r")


def move_layer(side, harvest=True):
    # side == 0 right
    # side == 1 left

    pyautogui.keyDown("a" if side else "d")
    time.sleep(1)

    time.sleep(14)

    pyautogui.keyUp("a" if side else "d")
    hold_key("s")


def move_layers():
    for i in range(FARM_LAYERS):
        move_layer(i % 2)


def harvest():
    reset_cursor()
    cursor_move("down", 1)
    select_slot(2)
    pyautogui.mouseDown()

    move_layers()
    pyautogui.mouseUp()
    hold_key("r")


def init_replant():
    
    def get_seeds():
        reset_cursor()
        cursor_move("up", 1)
        cursor_move("left", 2)
        right_click()
        
        
        

        for i in range(FARM_LAYERS):
            chest_cursor_reset()
            cursor_move("right", i, mode="chest")
            right_click(2.4)
            inventory_cursor_reset()
            cursor_move('right', 2 + i, mode='inventory')
            left_click()
            
        hold_key('tab')
       
        

    
    select_slot(1)
    left_click()
    if not is_farm_aligned():
        print(f"QR code not found, found {scan_qrcode()} exiting...")
        exit()
    time.sleep(2)
    

    get_seeds()
    



def replant():
    init_replant()

    reset_cursor()
    cursor_move("down")
    
    for i in range(FARM_LAYERS):
        select_slot(i + 3 % 10)
        pyautogui.mouseDown()
        move_layer(i % 2)
        pyautogui.mouseUp()        
        


focus_terraria()
time.sleep(1)
farm_setup()
reset_cursor()
# harvest()
replant()

farm_setup()

