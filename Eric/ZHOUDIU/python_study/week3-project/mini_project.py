# template for "Stopwatch: The Game"
import simplegui

# define global variables
message = "0:00:0"
time = 0
x = 0
y = 0
miniseconds = 0
game = str(x) + "/" + str(y)
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global miniseconds
    result = ""
    miniseconds = time % 10
    seconds = time / 10
    minutes = seconds / 60
    seconds -= minutes * 60
    seconds_str = str(seconds)
    if(seconds < 10):
        seconds_str = "0" + seconds_str
    result = str(minutes) + ":" + seconds_str + ":" + str(miniseconds)
    return result
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global timer
    timer.start()


def stop_handler():
    global timer, x, y, miniseconds, game
    timer.stop()
    if(miniseconds == 0):
        x += 1
    y += 1
    game = str(x) + "/" + str(y)
    

def reset_handler():
    global time, timer, message
    time = 0
    message = "0:00:0"
    timer.stop()

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time += 1
    global message
    message = format(time)
    return

# define draw handler
def draw(canvas):
    canvas.draw_text(message, [100, 110], 50, "White")
    canvas.draw_text(game, [260,20], 20, "Green")
    
# create frame
frame = simplegui.create_frame("Stop watch", 300, 200)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, timer_handler)

# register event handlers
frame.add_button('Start', start_handler, 200)
frame.add_button('Stop', stop_handler, 200)
frame.add_button('Reset', reset_handler, 200)

# start frame
frame.start()
timer.start()

# Please remember to review the grading rubric

