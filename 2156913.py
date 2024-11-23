from graphics import *

def pixelSize():
    #This function is for the user to input peferred pixel size between 5 and 7
    size = int(input("Enter pixel size[5,7]: "))#user input
    while size !=5 and size !=7:#To prompt the user if the user input a number outside 5 and 7
        size = int(input("Please enter either 5 or 7:"))
    return size

def rectanglepatch(win,x,y,colour):
    #the x and y variable is topleft of the shape
    rect = Rectangle(Point(x,y), Point(x + 100, y + 100))#the addition of 100 is for each rectangle to draw another one after it
    rect.setFill(colour)
    rect.draw(win)

def drawfinalPatch(win,tlPoint,colour):
    #the patchTLX and patchTLY are the topleft point of each rectangle
    patchTLX = tlPoint.getX()
    patchTLY = tlPoint.getY()
    #the patchBRX and patchBRY are the bottom right points of the draw rectangles
    patchBRX = tlPoint.getX() + 100
    patchBRY = tlPoint.getY() + 100
    for i in range(0,100,10):
        rectTLX = patchTLX
        rectTLY = patchTLY + i # after each rectangle is drawn rectTLY draws another rectangle inside a rectangle and goes on and on
        rectTL = Point(rectTLX, rectTLY)
        rectBR = Point(patchBRX - i, patchBRY)#i is being subtracted from the x axis bottom left point so that the rectangle shapes are halved in the window
        rectangle = Rectangle(rectTL, rectBR)
        rectangle.draw(win)
        if (i ==10 or i==30 or i ==50 or i==70 or i==90): # if statement so that it can draw a coloured shape in the y axis location
            rectangle.setFill(colour)
            rectangle.setOutline(colour)
        else:
            rectangle.setFill("white")
            rectangle.setOutline("white")

def triangle(win, tp, brp, blp, colour):
    t = Polygon(tp, brp, blp)
    t.setFill(colour)
    t.setOutline(colour)
    t.draw(win)
    return t


def drawTriPatch(win,x,y,colour):


    for i in range(0, 100, 20):
        for j in range(0, 101, 20): # the addition of 1 to 100,draws a halved triangle
        #x and y variable here are the topleft of the patch
            if (i ==0 or i == 40 or i == 80) and j<100: # for the drawn triangles in a 1st row ,3rd row and 5th row in range 5 respectively
                tp = Point(x+j+10,i+y)
                blp = Point(x+j, i+20+y)
                brp = Point(x+j+20,i+20+y)
                triangle(win, tp, brp, blp, colour)
            elif (i==20 or i==60) and j==0:#for the drawn triangles in a 2nd row and 4th row in range 5 respectively
                tp = Point(x+j,i+y)
                blp = Point(x+j, i+20+y)
                brp = Point(x+j+10,i+20+y)
                triangle(win, tp, brp, blp, colour)
            elif (i==20 or i==60) and j==100:#this if statement to draw a halved triangle in the patch
                tp = Point(x+j,i+y)
                blp = Point(x+j-10, i+20+y)
                brp = Point(x+j,i+20+y)
                triangle(win, tp, brp, blp, colour)
            elif j<100:#this if statement to draw a halved triangle in the patch
                tp = Point(x+j,i+y)
                blp = Point(x+j-10,i+20+y)
                brp = Point(x+j +10, i+20+y)
                triangle(win, tp, brp, blp, colour)

def main():
    size = pixelSize()
    dimension=100
    screenSize = size*dimension
    win = GraphWin("Test", screenSize, screenSize)

    validcolours = ["red", "green", "blue", "purple", "orange", "cyan"]#valid colours in the array
    colour=[] # empty array so that validcolours willl be appended to it
    for i in range(3):
        colourList = input("Choose between red, green, blue, purple, orange, cyan: ".format(str(validcolours)))
        while colourList not in validcolours:#to prompt the user if the user does not enter the correct colour in the vlaidcours array
            print("Please enter colour between red, green, blue, purple, orange, cyan")
            print(str(colour))
            colourList = input("Enter colour: ".format(str(validcolours)))
        if colourList in validcolours:
            colour.append(colourList)#to print appended list to the empty array



    for x in range(0, screenSize, 100):
        for y in range(0, screenSize, 100):
            tlPoint = Point(x, y)
            if y==0:# to draw plain patches at first row
                rectanglepatch(win,x,y,colour[0])
            elif x== 0:# to draw penultimate digit patch at fist column excluding the first row and the last row(implemented in the nested loop)
                drawTriPatch(win,x,y,colour[1])
                if y == screenSize - 100:
                    drawfinalPatch(win,tlPoint,colour[0])
                elif y == screenSize - 200:

                    rectanglepatch(win,x,y,colour[1])
                elif screenSize ==700:
                    if y==screenSize-300:

                        rectanglepatch(win,x,y,colour[1])
            elif x== screenSize - 100:# to draw penultimate digit patch at the last column excluding first two rows and last two rows

                drawTriPatch(win,x,y,colour[2])
                if y == screenSize - 100:#to draw final digit patch at last row

                    drawfinalPatch(win,tlPoint,colour[0])
                elif y == screenSize - 200:#to draw plain patch at second to last  row

                    rectanglepatch(win,x,y,colour[2])
                elif screenSize ==700:# implementing instance of 7 by 7 pixel to draw plain patch at the 4th row
                    if y==screenSize-300:

                        rectanglepatch(win,x,y,colour[2])

            elif y== screenSize - 100:#to draw final digit patch at second row

                drawfinalPatch(win,tlPoint,colour[0])
            elif y== screenSize - 200:#to draw final digit patch at third  row

                drawfinalPatch(win,tlPoint,colour[0])
            elif y==100:# to draw plain patch at the 2nd row

                rectanglepatch(win,x,y,colour[0])
            elif x==100:# to draw penultimate digit patch at the second column

                drawTriPatch(win,x,y,colour[1])
                if screenSize ==700:# implementing instance of 7 by 7 pixel to draw plain patch at the 3rd row
                    if y==screenSize-300:

                        rectanglepatch(win,x,y,colour[1])
            elif x== screenSize - 200:#to draw penultimate digit patch at the second to last column

                drawTriPatch(win,x,y,colour[2])
                if screenSize ==700:# implementing instance of 7 by 7 pixel to draw plain patch at the 3rd to last column
                    if y==screenSize-300:

                        rectanglepatch(win,x,y,colour[2])

            elif x==0 and y==400 :# to draw plain patch at exactly first column and 4th row

                rectanglepatch(win,x,y,colour[0])
            elif screenSize ==500:# implementing instance of 5 by 5 pixel to draw final digit patch at the 2nd row and second column
                if x==200 and y==200:

                    drawfinalPatch(win,tlPoint,colour[0])

            elif screenSize ==700:# implementing placement  of patches in 7 by 7 pixel
                if y==200:

                    rectanglepatch(win,x,y,colour[0])
                elif y==screenSize - 300:

                    drawfinalPatch(win,tlPoint,colour[0])
                elif x==300 and y==300:

                    drawfinalPatch(win,tlPoint,colour[0])
                elif x==200 and y==300:

                    drawTriPatch(win,x,y,colour[1])
                else:
                    drawTriPatch(win,x,y,colour[2])

