import sys, stddraw, stdarray, stdio, math, stdrandom

def main():
    pattern = int(sys.argv[1])
    n = int(sys.argv[2])

    x = 0.5
    y = 0.5
    size = 0.5
    draw(n, x, y, size)
    stddraw.show()
    
    
def draw(n, x, y, size):
    RATIO = 2.2 # 2.2 to 1
    if n == 0:
        return

    drawSquare(x, y, size)

    # Recursively draw 4 smaller trees of order n-1
    draw(n-1, x - size/2, y - size/2, size/RATIO) # low left
    draw(n-1, x - size/2, y + size/2, size/RATIO) # up left
    draw(n-1, x + size/2, y - size/2, size/RATIO) # low right
    draw(n-1, x + size/2, y + size/2, size/RATIO) # up right

def drawSquare(x, y, size):
    stddraw.setPenColor(stddraw.LIGHT_GRAY)
    stddraw.filledSquare(x, y, size/2)
    stddraw.setPenColor(stddraw.BLACK)
    stddraw.square(x, y, size/2)

if __name__ == '__main__': main()
