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
turtle.bgcolor("#8888FF")

# -----UI-----

while True:
  print("")
  print("Welcome to the Turtle Demo.")
  print("Press <D> to draw a shape, <F> to freehand with arrow keys or press <Q> to quit.")
  welcome_input = input()
  if welcome_input == "D":
    print("")
    print("What Shape do you wan't to draw?")
    print(" <R>: Rectangle")
    print(" <C>: Circle")
    print(" <S>: Square")
    print(" <T>: Triangle")
    print(" <I>: Isosceles_triangle")
    print(" <H>: House")
    print(" other go up one layer")
    shape_input = str.upper(input())
    # Rectangle
    if shape_input == "R":
      print("")
      print("What horizontal size should your rectangle have?")
      while True:
        shape_input_rectangle_hor = input()
        try:
          shape_input_rectangle_hor = int(shape_input_rectangle_hor)
          break
        except:
          print("Please use an even number.")
      print("What vertical size should your rectangle have?")
      while True:
        shape_input_rectangle_ver = input()
        try:
          shape_input_rectangle_ver = int(shape_input_rectangle_ver)
          break
        except:
          print("Please use an even number.")
      print("Your rectangle is now beeing drawn.")
      rectangle(shape_input_rectangle_hor, shape_input_rectangle_ver)
      #Circle
    elif shape_input == "C":
      print("")
      print("What size should your circle have?")
      while True:
        shape_input_circle = input()
        try:
          shape_input_circle = int(shape_input_circle)
          break
        except:
          print("Please use an even number.")
      print("Your circle is now beeing drawn.")
      turtle.circle(shape_input_circle)
