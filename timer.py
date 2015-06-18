#http://www.codeskulptor.org/#user40_Pd2wVZGU6NBy1cL.py
#import drawing modules
import simplegui
import random
#define global variable

message = "Beijing welcome you"
position = [50,50]
width = 200
height = 300
interval = 1000
# handler for text box
def update(text):
    global message
    message = text

#handler for timer    
def tick():
    x = random.randrange(0,width)
    y = random.randrange(0,height)
    position[0] = x
    position[1] = y
    
#handler to draw on canvas
def draw(canvas):
    global message,position
    canvas.draw_text(message,position,20 ,'White','serif' )


#create a frame
my_frame = simplegui.create_frame("Home",width, height )

#create timer
timer = simplegui.create_timer(interval, tick)

#register event handler
my_frame.set_draw_handler(draw)
text = my_frame.add_input("New message is: ",update,200)

#start frame and timer
my_frame.start()
timer.start()

timer.start()
