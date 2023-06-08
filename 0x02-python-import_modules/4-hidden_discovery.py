#!/usr/bin/python3
import hidden_4

def main():
    x = dir(hidden_4)
    for a in range(len(x)):
        if (x[a][0] != '_'):
            print("{}".format(x[a]))

            if __name__ == "__main__":
                main()
