import sys
import stdio

def main():
    num = len(sys.argv)
    if (num == 1): stdio.write("*crickets*\n")
    if (num == 2): stdio.write("Palin is arguing with themself.\n")
    if (num == 3): stdio.write("Palin is having an argument with Cleese.\n")
    if (num == 4): stdio.write("Much hilarity ensues.\n")
    if (num == 5): stdio.write("Much hilarity ensues.\n")

if __name__ == '__main__': main()
