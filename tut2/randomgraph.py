import sys, stdio, stdarray, math, stddraw, stdrandom

def main():
    N = int(sys.argv[1])
    p = float(sys.argv[2])

    r = 10

    points = stdarray.create2D(N, 2, 0)
    a = (2*math.pi) / N

    for i in range(N):
        points[i] = [r * math.cos(a * i), r * math.sin(a * i)]

    stdarray.write2D(points)

    stddraw.setXscale(-15.0, 15.0)
    stddraw.setYscale(-15.0, 15.0)
    stddraw.clear(stddraw.WHITE)

    for point in points:
        stddraw.point(point[0], point[1])
        
        for to in points:
            if stdrandom.bernoulli(p) and not to == point:
                stddraw.line(point[0], point[1], to[0], to[1])
        
    stddraw.show()

if __name__ == '__main__': main()
