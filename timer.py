#http://www.codeskulptor.org/#user40_q25bqUuodyV2D7Q.py

import simplegui
import random
#define global variable

message = "Beijing welcome you"
position = [50,50]
width = 200
height = 300
interval = 1000
# define the message
def update(text):
    global message
    message = text

#define draw handler
def draw(canvas):
    global message,position
    canvas.draw_text(message,position,20 ,'White','serif' )
def tick():
    x = random.randrange(0,width)
    y = random.randrange(0,height)
    position[0] = x
    position[1] = y

#create a frame
my_frame = simplegui.create_frame("Home",width, height )

#create timer
timer = simplegui.create_timer(interval, tick)

#draw text on canvas
my_frame.set_draw_handler(draw)

#register the text
text = my_frame.add_input("New message is: ",update,200)

#start frame and timer
my_frame.start()
timer.start()
