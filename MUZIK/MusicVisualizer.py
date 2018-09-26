import sys, os, time, wave, numpy as np

''' Inline Colors '''
CEND   = '\33[0m'
CBOLD  = '\33[1m'
CITAL  = '\33[3m'
CWHBLK = '\33[7m'
CBLINK = '\33[5m'
CRED   = '\33[31m'
CPURP  = '\33[35m'
CGREEN = '\33[92m'
CBLUE  = '\33[34m'
CBROWN = '\33[46m'
CREDBG = '\33[41m'
CBLKBG = '\33[100m'


def swapfiledump(fname):
    data = []
    for line in open(fname, 'r').readlines():
        data.append(line.replace('\n', ''))
    return data


def song_select():
    os.system("p=$PWD;cd /media/root/DB0/songs;"
              "find -name '*.mp3' >> $p/songs.txt ;cd $p")
    mp3_files = swapfiledump('songs.txt')
    os.system('rm songs.txt')
    print str(len(mp3_files)) + " MP3s to choose from: "
    songs = {}
    II = 0
    for song in mp3_files:
        songs[II] = song
        print str(II) + "- \t" + song
        II += 1
    opt = int(input('Enter a selection: '))
    return songs, opt


def main():
    songs, opt = song_select()
    cmd = 'mpg123 -w out.wav /media/root/DB0/songs/' + songs[opt]
    os.system(cmd)
    os.system('clear')
    print CPURP + CBOLD + "\t\tPlaying " + \
          CBOLD + CGREEN + songs[opt].replace('./', '').replace('.mp3', '') + CEND

    os.system('paplay out.wav & python Visuals.py out.wav')
    #os.system('python Visuals.py out.wav')
    os.system('rm out.wav')


if __name__ == '__main__':
    main()