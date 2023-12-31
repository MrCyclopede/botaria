
import pyautogui
import time
import numpy as np
# import easyocr
easyocr = None
from thefuzz import fuzz


pyautogui.PAUSE = 0.07
TILE_SIZE = 16
screen_width, screen_height = pyautogui.size()
SPEED = 0.01
SAFE = False

QR_SPAWN = 469
QR_FARM = 42


def time_func(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print(f"{func.__name__}:", str(time.time() - start)[:4])
    return wrapper


def focus_terraria():
    print(screen_width, screen_height)
    for i, w in enumerate(pyautogui.getWindowsWithTitle("terraria")):
        print(i, w.title)
        if "Terraria" in w.title:
            print("Terraria window found:", w.title)
            w.minimize()
            w.maximize()
            return
        
    print("Terraria window not found, exiting...")
    exit()




def left_click(duration=SPEED):
    pyautogui.mouseDown()
    time.sleep(duration)
    pyautogui.mouseUp()

def hold_key(key, hold_time=SPEED):
    key = str(key)
    start = time.time()
    while time.time() - start < hold_time:
        pyautogui.keyDown(key)
    pyautogui.keyUp(key)


def select_slot(slot):
    hold_key(slot, SPEED)


def place_block():
    select_slot(4)
    left_click()


def move_right():
    hold_key('d', 0.4)
    
def move_left():
    hold_key('a', 0.4)

    
def hammer_block(times=4):
    select_slot(3)
    for _ in range(times):
        left_click()
        time.sleep(0.1)

  
def mine_block():
    select_slot(2)
    left_click(0.2)
    


def reset_cursor():
    pyautogui.moveTo(screen_width/2, screen_height/2)
    cursor_move('left')    
    cursor_move('up', 2)
    
def place_wall(safe=SAFE):
    if safe:
        select_slot(2)
        mine_block()
    select_slot(5)
    left_click()
    

def place_torch():
    select_slot(6)
    left_click()



def cursor_move(axis, distance=1):
    p = distance * TILE_SIZE
    if axis == 'up':
        pyautogui.moveRel(0, -p)
    elif axis == 'down':
        pyautogui.moveRel(0, p)	
    elif axis == 'left':
        pyautogui.moveRel(-p, 0)	
    elif axis == 'right':
        pyautogui.moveRel(p, 0)
        


def leftside_hoik():
    reset_cursor()
    place_block()
    
    cursor_move('down')
    mine_block()
    place_wall()
    for _ in range(4):
        cursor_move('down')
        place_wall()
    
    
    cursor_move('down')
    place_block()
    cursor_move('left')
    
    
    for i in range(3):
        
        if i == 1:
            place_wall(safe=True)
            place_block()
            hammer_block(5)
            
        elif i == 2:
            place_wall(safe=True)
            place_block()
            hammer_block(4)
        else:
            place_block()
        cursor_move('up')

    for i in range(3):
        place_wall()
        if i == 1:
            place_torch()
        cursor_move('up')
        
    place_block()
    
    if SAFE:
        reset_cursor()
        cursor_move('down')
        cursor_move('left', 2)
        for _ in range(5):
            place_block()
            cursor_move('down')
        reset_cursor()
    else:
        cursor_move('down')
        cursor_move('left')
        place_block()
    
    move_left()





def fish_bot():
    reader = easyocr.Reader(['en'])
    
    
    def reset_cursor():
        pyautogui.moveTo(screen_width/2 + TILE_SIZE, screen_height/2 + TILE_SIZE * 2)
        # cursor_move('right')
        # cursor_move('down', 2)
        
    
    
    def check_fish():
        badluck = 0
        im = pyautogui.screenshot(region=(screen_width/2 - (8 * TILE_SIZE) , screen_height/2 - (2 * TILE_SIZE), 15 * TILE_SIZE, 3 * TILE_SIZE))
        
        im.save('screen.png')
        result = reader.readtext('screen.png')
        
        for r in result:
            
            for w in whitelist:
                ocr_raw = r[1].lower()
                ratio = fuzz.partial_token_sort_ratio(w, ocr_raw) / 100
                reset_cursor()
                if ratio > 0.6:
                    # im.save(f'screen-{time.time()}.png')
                    print(f'Caught: {w} for ratio {ratio} on {ocr_raw}')
                    left_click()
                    
                    return 'caught'
                else:
                    return 'wrong_item'
                    # print(f'DECLINED: {w} for ratio {ratio} on {ocr_raw}')
        return 'not caught'
                    
                    
    whitelist = ['caisse', 'zephyr']
    
    
    
    reset_cursor()
    select_slot(1)
    left_click()
    
    badluck = 0
    while True:
        ret = check_fish()
        if ret == 'caught':
            left_click()
            badluck = 0
            time.sleep(1)
        elif ret == 'wrong_item':
            print(f'{badluck=}')
            cursor_move('right', 2)
            
            badluck += 1
        
        if badluck > 3:
            print('badluck, resetting')
            badluck = 0
            left_click()
            reset_cursor()
            
        time.sleep(0.1)
    

def scan_qrcode():
    
    def reset_cursor():
        pyautogui.moveTo(screen_width/2, screen_height/2)
    reset_cursor()        
    
    center_x = int(screen_width/2) - (TILE_SIZE + TILE_SIZE/2)
    center_y = int(screen_height/2) - 3 - (TILE_SIZE * 6 + TILE_SIZE/2)
    
    im = pyautogui.screenshot(region=(center_x, center_y, 3 * TILE_SIZE, 3 * TILE_SIZE))
    im.save('screen_qr.png')
    
    x = TILE_SIZE/2
    y = TILE_SIZE/2
    qrcode = 0
    for i in range(9):
        rel_x = int(x + (TILE_SIZE * (i % 3)))
        rel_y = int(y + TILE_SIZE * (i // 3))
        px = im.getpixel((rel_x, rel_y))
        qrcode += get_color(px) * (2 ** i)
    return qrcode
    
def get_color(color):
    colors = [[0,0,0],[155,155,155]]
    colors = np.array(colors)
    color = np.array(color)
    distances = np.sqrt(np.sum((colors-color)**2,axis=1))
    index_of_smallest = np.where(distances==np.amin(distances))
    
    return index_of_smallest[0][0]
      
def check_spawn():
    return scan_qrcode() == QR_SPAWN    