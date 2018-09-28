import sys, os, time, numpy as np, wave


def usage():
    print "Incorrect Usage!"


def main():
    if len(sys.argv) > 1:
        song = wave.open(sys.argv[1], 'r')
        N = song.getnframes()
        frate = song.getframerate()
        alpha = 0.300;
        print ((N * (1 + alpha)/frate) - (N/frate))/100

    else:
        usage()


if __name__ == '__main__':
    main()
