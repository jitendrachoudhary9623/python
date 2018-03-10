import turtle #one of the graphics library

def draw_square():
#step0 draw the window
	window=turtle.Screen();
	window.bgcolor("red");

	
#step2 -> draw square
	draw_circle(90);
#lastStep 
	window.exitonclick();

def draw_circle(ang):
# - grab a Turtle
	t2=turtle.Turtle();
	t2.color("yellow");
	
	t2.left(ang);
	for i in range(0,4):
		t2.forward(100);
		t2.right(90);
	
	draw_circle(ang+10);
	
draw_square();
