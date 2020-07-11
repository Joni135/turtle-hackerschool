import turtle

s = turtle.getscreen()

# Der Befehl forward/fd bewegt die Turtle in Blickrichtung 
#turtle.fd(0)

# Der Befehl backward/bk bewegt die Turtle in Blickrichtung
#turtle.bk(0)

# Der Befehl right/rt dreht die Turtle nach rechts
#turtle.rt(0)

# Der Befehl left/lt dreht die Turtle nach links
#turtle.lt(0)

# ----- Basis Formen -----

# Die Fukltion square lässt die Turtle ein Viereck der Größe x Zeichnen
# @param size ist die Seitenlänge des Quadrats
def square(size):
  for i in range(0, 4):
    turtle.fd(size)
    turtle.rt(90)

# Die Funktion isosceles_triangle lässt die Turtle ein gleichschenkliges Dreieck der Seitenlänge X Zeichnen.
# @param size ist die Seitenlänge des gleichschenkligen Dreiecks
def isosceles_triangle(size):
  for i in range(0, 3):
    turtle.fd(size)
    turtle.lt(120)

# Die Funktion circle zeichnet ein 60-Eck zeichnen. Dies sieht einem Kreis sehr ähnlich.
# @param size: Größe des 60-Ecks geteilt durch 10, damit die Angaben der Größe besser entsprechen.
def circle(size):
  for i in range(0, 60):
    turtle.fd(size/10)
    turtle.rt(6)

# Die Funktion rectangle zeichnet ein Rechteck mit frei wählbaren Seitenlängen
# @param size_x: Die Länge des Rechtecks
# @param size_y: Die Höhe des Rechtecks
def rectangle(size_x, size_y):
  for i in range(0, 2):
    turtle.fd(size_x)
    turtle.rt(90)
    turtle.fd(size_y)
    turtle.rt(90)

# Die Funktion triangle zeichnet ein Dreick basierend auf drei Seitenlängen und der Angabe ob es nach oben oder unten gerichtet ist.
# @param size_a: Seitenlänge der Seite A am Dreieck
# @param size_b: Seitenlänge der Seite C am Dreieck
# @param angle: Winkelgröße am Dreieck
def triangle(size_a, size_b, angle):
  start = turtle.pos()
  turtle.fd(size_a)
  turtle.rt(angle)
  turtle.fd(size_b)
  turtle.goto(start)

# ----- Zusammengesetze Formen -----

# Die Funktion house zeichnet ein Rechteck mit aufgesetztem Dreieck
# @param height_rectangle: Die Höhe des Rechtecks
# @param width: Die Breite des Hauses
def house(height_rectangle, width):
  rectangle(width, height_rectangle)
  turtle.pencolor("#FF0000")
  isosceles_triangle(width)
  starty = turtle.ycor()
  startx = turtle.xcor()
  starty = starty - height_rectangle
  startx = startx + (width*0.8)
  turtle.up()
  turtle.setx(startx)
  turtle.sety(starty)
  turtle.down()
  turtle.pencolor("#000000")
  rectangle(-width/3, -height_rectangle/2)

# Die Funktion check_int konvertiert Strings, Floats oder Binärwerte in Integer, wenn dies möglich ist.
# Sollte es nicht möglich sein, wird nochmal nach Input gefragt.
# @param try_int: Die Variable, die von Str / Float / Bin to Int Konvertiert wird.
def check_int(try_int):
  while True:
    try_int = input()
    try:
      try_int = int(try_int)
      return try_int
    except:
      print("Please do only use even numbers.")

# -----UI-----
# ----- Tastatur Steuerung -----

# turtle.setup(800,600)

def moveup():
  turtle.seth(90)
  turtle.forward(5)
def movedown():
  turtle.seth(270)
  turtle.forward(5)
def moveleft():
  turtle.seth(180)
  turtle.forward(5)
def moveright():
  turtle.seth(0)
  turtle.forward(5)

def selberZeichnen():
  print("Du kannst jetzt mit den Pfeiltasten selbst malen")
  turtle.listen()

turtle.onkey(moveup,"Up")
turtle.onkey(movedown,"Down")
turtle.onkey(moveleft,"Left")
turtle.onkey(moveright,"Right")


def Pendown():
  turtle.pendown()

def Penup():
  turtle.penup()



#turtle.onkey(red,"r")
#turtle.onkey(blue,"b")
#turtle.onkey(green,"g")
#turtle.onkey(yellow,"y")
#turtle.onkey(purple,"p")
#turtle.onkey(orange,"o")
#turtle.onkey(black,"space")
#turtle.onkey(Penup,"1")
#turtle.onkey(Pendown,"2")










# ----- UI -----

while True:
  print("")
  print("Welcome to the Turtle Demo.")
  print("What do you want to do?")
  print(" <D>: Create shape")
  print(" <C>: Change color")
  print(" <F>: Draw with arrow keys")
  print(" <Q>: Quit")
  welcome_input = str.upper(input())
  # Shapes
  if welcome_input == "D":
    print("")
    print("What Shape do you wan't to draw?")
    print(" <R>: Rectangle")
    print(" <C>: Circle")
    print(" <S>: Square")
    print(" <T>: Triangle")
    print(" <I>: Isosceles triangle")
    print(" <H>: House")
    shape_input = str.upper(input())
    # Rectangle
    if shape_input == "R":
      print("")
      print("What horizontal size should your rectangle have?")
      shape_input_rectangle_hor = ""
      check_int(shape_input_rectangle_hor)
      print("What vertical size should your rectangle have?")
      shape_input_rectangle_ver = ""
      check_int(shape_input_rectangle_ver)
      print("Your rectangle is now beeing drawn.")
      rectangle(shape_input_rectangle_hor, shape_input_rectangle_ver)
      #Circle
    if shape_input == "C":
      print("")
      print("What size should your circle have?")
      shape_input_circle = ""
      check_int(shape_input_circle)
      print("Your circle is now beeing drawn.")
      turtle.circle(shape_input_circle)
    # Square
    if shape_input == "S":
      print("")
      print("What size should your square have?")
      shape_input_square = ""
      check_int(shape_input_square)
      print("Your square is beeing drawn.")
      square(shape_input_square)
    # Triangle
    if shape_input == "T":
      print("")
      print("What length should line A have on your triangle?")
      shape_input_triangle_a = ""
      check_int(shape_input_triangle_a)
      print("What length should line B have on your triangle?")
      shape_input_triangle_b = ""
      check_int(shape_input_triangle_b)
      print("What angle should be inbetween line A and B?")
      shape_input_triangle_angle = ""
      check_int(shape_input_triangle_angle)
      print("Your triangle is beeing drawn.")
      triangle(shape_input_triangle_a, shape_input_triangle_b, shape_input_triangle_angle)
    # Isosceles_triangle
    if shape_input == "I":
      print("How big should your isosceles triangle be?")
      shape_input_isoceles_triangle = ""
      check_int(shape_input_isoceles_triangle)
      isosceles_triangle(shape_input_isoceles_triangle)
    # House
    if shape_input == "H":
      print("How wide should your house be?")
      shape_input_house_wide = ""
      check_int(shape_input_house_wide)
      print("How high should your house be?")
      shape_input_house_height = ""
      check_int(shape_input_house_height)

  # Arrow key drawing
  if shape_input == "F":
    selberZeichnen()