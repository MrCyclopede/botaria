import pyautogui
import time

pyautogui.PAUSE = 0.07
TILE_SIZE = 22
screen_width, screen_height = pyautogui.size()
SPEED = 0.01
SAFE = False


def time_func(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        print(f"{func.__name__}:", str(time.time() - start)[:4])
    return wrapper

def focus_terraria():
    for i, w in enumerate(pyautogui.getWindowsWithTitle("terraria")):
        if "Terraria: " in w.title:
            print("Terraria window found:", w.title)
            w.minimize()
            w.maximize()
print(screen_width, screen_height)


def left_click(duration=SPEED):
    pyautogui.mouseDown()
    time.sleep(duration)
    pyautogui.mouseUp()

def hold_key(key, hold_time):
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
    cursor_move('right')    
    cursor_move('up', 2)


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




def place_wall(safe=SAFE):
    if safe:
        select_slot(2)
        mine_block()
    select_slot(5)
    left_click()
    

def place_torch():
    select_slot(6)
    left_click()


def do_zone():
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
    cursor_move('right')
    
    
    for i in range(3):
        
        if i == 1:
            place_wall(safe=True)
            place_block()
            hammer_block(4)
            
        elif i == 2:
            place_wall(safe=True)
            place_block()
            hammer_block(5)
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
        cursor_move('right', 2)
        for _ in range(5):
            place_block()
            cursor_move('down')
        reset_cursor()
    else:
        cursor_move('down')
        cursor_move('right')
        place_block()
    
    move_right()
    
    

focus_terraria()
for i in range(100):
    do_zone()