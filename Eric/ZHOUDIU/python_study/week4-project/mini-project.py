# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

score1 = 0
score2 = 0

paddle1_pos = [[1,HEIGHT / 2 - HALF_PAD_HEIGHT], [1, HEIGHT / 2 + HALF_PAD_HEIGHT]]
paddle2_pos = [[WIDTH,HEIGHT / 2 - HALF_PAD_HEIGHT], [WIDTH, HEIGHT / 2 + HALF_PAD_HEIGHT]]
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0, 0]
paddle1_vel = [0, 0]
paddle2_vel = [0, 0]


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    if(direction == 'LEFT'):
        ball_vel[0] = -random.randrange(5, 7)
        ball_vel[1] = -random.randrange(3, 5)
    elif(direction == 'RIGHT'):
        ball_vel[0] = random.randrange(5, 7)
        ball_vel[1] = -random.randrange(3, 5)
    

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    spawn_ball('LEFT')

def reset_handler():
    new_game()
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    #if ball_pos[0] < 0 or ball_pos[0] > WIDTH:
    if ball_pos[0] <= BALL_RADIUS and ball_pos[1] < paddle1_pos[0][1] or ball_pos[0] <= BALL_RADIUS and ball_pos[1] > \
        paddle1_pos[1][1] or ball_pos[0] >= WIDTH - BALL_RADIUS and ball_pos[1] < paddle2_pos[0][1] or ball_pos[
        0] >= WIDTH - BALL_RADIUS and ball_pos[1] > paddle2_pos[1][1] or ball_pos[0] < 0 or ball_pos[0] > WIDTH:
        if ball_pos[0] <= BALL_RADIUS and ball_pos[1] < paddle1_pos[0][1] or ball_pos[0] <= BALL_RADIUS and ball_pos[1] > paddle1_pos[1][1]:
            score2 += 1
        if ball_pos[0] >= WIDTH - BALL_RADIUS and ball_pos[1] < paddle2_pos[0][1] or ball_pos[
            0] >= WIDTH - BALL_RADIUS and ball_pos[1] > paddle2_pos[1][1]:
            score1 += 1
            
        ball_pos = [WIDTH / 2, HEIGHT / 2]
        temp = random.randrange(0, 2, 1)
        if temp == 0:
            spawn_ball('RIGHT')
        else:
            spawn_ball('LEFT')
       
            
    else:
        if ball_pos[0] <= BALL_RADIUS:
            ball_vel[0] = -ball_vel[0] * 1.1

        if ball_pos[0] >= WIDTH - BALL_RADIUS:
            ball_vel[0] = -ball_vel[0] * 1.1


         
    if ball_pos[1] <= BALL_RADIUS:
                    ball_vel[1] = - ball_vel[1]
    if ball_pos[1] >= HEIGHT - BALL_RADIUS:
                    ball_vel[1] = -ball_vel[1]
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")    
    
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos[0][1] >= 0 and paddle1_pos[1][1] <= HEIGHT:
        paddle1_pos[0][1] += paddle1_vel[0]
        paddle1_pos[1][1] += paddle1_vel[1]
        if paddle1_pos[0][1] < 0:
            paddle1_pos[0][1] = 0
            paddle1_pos[1][1] = PAD_HEIGHT
        if paddle1_pos[1][1] > HEIGHT:
            paddle1_pos[0][1] = HEIGHT - PAD_HEIGHT
            paddle1_pos[1][1] = HEIGHT
    
    if paddle2_pos[0][1] >= 0 and paddle2_pos[1][1] <= HEIGHT:
        paddle2_pos[0][1] += paddle2_vel[0]
        paddle2_pos[1][1] += paddle2_vel[1]
        if paddle2_pos[0][1] < 0:
            paddle2_pos[0][1] = 0
            paddle2_pos[1][1] = PAD_HEIGHT
        if paddle2_pos[1][1] > HEIGHT:
            paddle2_pos[0][1] = HEIGHT - PAD_HEIGHT
            paddle2_pos[1][1] = HEIGHT
    
    # draw paddles
    canvas.draw_polyline(paddle1_pos, PAD_WIDTH, 'Red')
    canvas.draw_polyline(paddle2_pos, PAD_WIDTH, 'Yellow')
    # determine whether paddle and ball collide    
    
    # draw scores
    canvas.draw_text(str(score1), [125, 100], 50, 'Red')
    canvas.draw_text(str(score2), [450, 100], 50, 'Yellow')

        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["w"]:
        paddle1_vel = [-5, -5]
    elif key==simplegui.KEY_MAP["s"]:
        paddle1_vel = [5, 5]
    elif key==simplegui.KEY_MAP["up"]:
        paddle2_vel = [-5, -5]
    elif key==simplegui.KEY_MAP["down"]:
        paddle2_vel = [5, 5]

   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key==simplegui.KEY_MAP["w"] or key==simplegui.KEY_MAP["s"]:
        paddle1_vel = [0, 0]
    if key==simplegui.KEY_MAP["up"] or key==simplegui.KEY_MAP["down"]:
        paddle2_vel = [0, 0]

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_draw_handler(draw)
frame.add_button('Reset', reset_handler)


# start frame
new_game()
frame.start()

