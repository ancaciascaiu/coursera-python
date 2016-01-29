# template for "Stopwatch: The Game"   http://www.codeskulptor.org/#user40_JnM6qCsrL8_2.py
import simplegui
# define global variables
interval = 100
attempts = 0
success = 0
stpwtch = True
count = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D

def format(t):
    milisecs = t % 10
    allsecs = int(t/10)
    secs = allsecs %60
    minute = int(allsecs/60)
    
    if secs < 10:
        secs = "0" + str(secs)
    
    string = str(minute) + ":" + str(secs) + "." + str(milisecs)
    return string
#print format(600)

# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global count, success, attempts, stpwtch
    stpwtch = False
    timer.start()

def stop():
    global attempts, success, count, stpwtch
    if stpwtch == True:
        return
    
    stpwtch = True
    attempts = attempts + 1
    if count%10 == 0:
        success = success + 1
    
    timer.stop()

def reset():
    global count, attempts, success
    count = 0
    success = 0
    attempts = 0
    timer.stop()
    

# define event handler for timer with 0.1 sec interval
def tick():
    global count
    count = count + 1

# define draw handler
def draw(canvas):
    global count, success, attempts
    display = format(count)
    canvas.draw_text(display, (140, 90), 40, "white")
    success_attempts = str(success) + '/' + str(attempts)
    canvas.draw_text(success_attempts, (230, 30), 20, "red")

# create frame
frame = simplegui.create_frame("Stopwatch", 300, 200)

# register event handlers
timer = simplegui.create_timer(interval, tick)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)
frame.set_draw_handler(draw)

# start frame
frame.start()
# Please remember to review the grading rubric
