import sys
import stdio

def main():
    if (len(sys.argv) > 2 or len(sys.argv) < 2):
        stdio.write("Only 2 arguments are allowed.\n")
        sys.exit(1)
