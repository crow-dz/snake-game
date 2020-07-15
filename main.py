from tkinter import *
import random

def up(event=None):
	global dx, dy
	dx,dy=0,-1
def down(event=None):
	global dx, dy
	dx,dy=0,1
def left(event=None):
	global dx, dy
	dx,dy=-1,0
def right(event=None):
	global dx, dy
	dx,dy=1,0
def food():
	global r_x ,r_y,Food,score
	if Food == True : 
		if 	n_head_x == r_x and n_head_y == r_y:
			adding()
			score+=1
			allscore ='Score : '+str(score)
			label.config(text=allscore)
			Food=False
	else:
		r_x = random.randrange(0,380,20)
		r_y = random.randrange(0,380,20)
		can.coords(foodie,r_x,r_y,r_x+20,r_y+20)
		Food=True
def move(event=None):
	global n_head_x,n_head_y,score
	flag = 1
	# to move right
	# finding id last part in snake body
	last_part = snake[0][0]
	# finding id of first part in snake body
	snake_lenth = len(snake)
	# using that id to store list of first part : [id,x,y]
	first_part = snake[snake_lenth-1]
	# store x and y
	head_x , head_y = first_part[1],first_part[2]
	# adding moveing victors
	n_head_x , n_head_y = head_x+u*dx , head_y+u*dy
	newHead=[last_part,n_head_x,n_head_y] # to know wich the head 
	for xo in snake:
		if xo[0] != newHead[0] and xo[1] == newHead[1] and xo[2] == newHead[2]:
			game_over_m='Game Over | Score : '+str(score)
			label.config(text=game_over_m, font="Arial 14 bold")
			flag = 0
	if n_head_x < 0 or n_head_x > 380 or n_head_y < 0 or n_head_y > 380:
		flag = 0
		game_over_m='Game Over | Score : '+str(score)
		label.config(text=game_over_m, font="Arial 14 bold")
	# giving new coords to last part 
	can.coords(last_part,n_head_x,n_head_y,n_head_x+u,n_head_y+u)
	food()
	# deleting old part
	snake.append([last_part,n_head_x,n_head_y])
	del(snake[0])
	if flag == 1:
		can.after(200,move)
#### vars #####
snake=[]
x,y,u=20,20,20
dx,dy=1,0
flag = 0
Food = True
score=0
r_x,r_y=random.randrange(0,380,20),random.randrange(0,380,20)
###############
#####GUI#######
window = Tk()
window.title('Snake')
window.geometry('410x430')
label = Label(window,width=400,text='Score : 0', font="Arial 14 bold")
label.pack()
can = Canvas(window,width=399,height=399,bg='light grey')
can.pack()

def adding():
	global x,y,u
	i = 0
	while i <1:
		head =can.create_rectangle(500, 500, 500+u, 500+u, fill="green")
		snake.append([head, x, y])
		x =x+u # le carré suivant sera un peu plus à droite
		i =i+1
head =can.create_rectangle(x, y, x+u, y+u, fill="green")
snake.append([head, x, y])

foodie=can.create_rectangle(r_x,r_y,r_x+20,r_y+20, fill='red')
window.bind("<space>",move)
window.bind("<Up>",up)
window.bind("<Down>",down)
window.bind("<Left>",left)
window.bind("<Right>",right)
window.mainloop()
###############
