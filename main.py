import pyautogui
import time
# from pynput.mouse import Button, Controller

TILE_SIZE = 22

screen_width, screen_height = pyautogui.size()


print(screen_width, screen_height)

def hold_key(key, hold_time):
    key = str(key)
    start = time.time()
    while time.time() - start < hold_time:
        pyautogui.keyDown(key)
    pyautogui.keyUp(key)

# (32 bits)

def focus_terraria():
    for i, w in enumerate(pyautogui.getWindowsWithTitle("terraria")):
        if "Terraria: " in w.title:
            print("Terraria window found:", w.title)
            w.minimize()
            w.maximize()
      
def select_slot(slot):
    hold_key(slot, 0.1)


def place_block():
    select_slot(4)
    pyautogui.mouseDown()
    time.sleep(0.01)
    pyautogui.mouseUp()

def move_right():
    hold_key('d', 1)
    
def hammer_block():
    select_slot(3)
    for _ in range(4):
        pyautogui.mouseDown()
        time.sleep(0.01)
        pyautogui.mouseUp()
        time.sleep(0.01)
        
def mine_block():
    select_slot(2)
    pyautogui.mouseDown()
    time.sleep(0.2)
    pyautogui.mouseUp()
    

    
    
# ============SETUP===============
focus_terraria()
    
# ============TEST===============


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

        
        
        
pyautogui.moveTo(screen_width/2, screen_height/2)
x, y = pyautogui.position()

time.sleep(0.1)
x += TILE_SIZE
pyautogui.moveTo(x, y)

while True:
    cursor_move('down')
    cursor_move('down')

    hammer_block()

    cursor_move('right')
    cursor_move('right')
    place_block()

    cursor_move('up')
    place_block()

    cursor_move('up')
    place_block()

    cursor_move('left')
    cursor_move('left')
    mine_block()

    cursor_move('down')
    mine_block()

    move_right()
    cursor_move('up')


# cursor_move('up', 1)
# time.sleep(0.2)
# cursor_move('down', 1)
# time.sleep(0.2)
# cursor_move('left', 1)
# time.sleep(0.2)
# cursor_move('right', 1)
# time.sleep(0.2)

# print(pyautogui.KEY_NAMES)


    



# time.sleep(7)
# for i in range(10):
#     mouse.press()
#     time.sleep(0.01)
#     mouse.release(Button.left)
#     hold_key('a', 0.22)