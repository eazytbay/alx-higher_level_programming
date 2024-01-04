#!/usr/bin/python3
"""
nqueens program that prints the coordinates of n queens
on an nxn in a way that they are all in positions that are non_attacking
"""


from sys import argv

if __name__ == "__main__":
    c = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    t = int(argv[1])
    if t < 4:
        print("N must be at least 4")
        exit(1)

    # initialize the answer list
    for s in range(t):
        c.append([s, None])

    def already_exists(p):
        """confirm that a queen does not exist already in that p value"""
        for o in range(t):
            if p == c[o][1]:
                return True
        return False

    def reject(o, p):
        """confirms whether or not to reject the solution"""
        if (already_exists(p)):
            return False
        s = 0
        while(s < o):
            if abs(c[s][1] - p) == abs(s - o):
                return False
            s += 1
        return True

    def clear_a(o):
        """removes the answers from the exact point of failure"""
        for s in range(o, t):
            c[s][1] = None

    def nqueens(o):
        """recursively backtrack the function to locate the solution"""
        for p in range(t):
            clear_a(o)
            if reject(o, p):
                c[o][1] = p
                if (o == t - 1):  # accepts the solution
                    print(c)
                else:
                    nqueens(o + 1)  # moves on to next o value to continue

    # start the recursive process at o = 0
    nqueens(0)
