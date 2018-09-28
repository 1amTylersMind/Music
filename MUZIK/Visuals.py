import sys, os, time, wave, numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import scipy.ndimage as ndi

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


class Visualize:


    FrameRate = 0
    NFrames = 0

    def __init__(self,song):
        stream = wave.open(song, 'r')
        self.FrameRate = stream.getframerate()
        self.NFrames = stream.getnframes()
        pram = list(stream.getparams())
        pram[3] = 0
        print pram
        print "Frame Rate:" + str(self.FrameRate)
        print "N Frames: " + str(self.NFrames)
        print CBOLD+CITAL+"(Estimated Filesize (" + \
              str(float(self.NFrames*self.FrameRate)/(1000000*np.power(2,16)))+" MB)"+CEND
        stream.close()

    def run(self, song):
        stream = wave.open(song, 'r')
        images = []
        for frame in range(int(self.NFrames / self.FrameRate)):
            # Read a 1s sample of the song and split into L & R
            self.DATA_BUFFER = np.fromstring(stream.readframes(self.FrameRate),
                                             dtype=np.int16)
            # Split the signal into left and right signal
            self.L = np.array(self.DATA_BUFFER[0::2])
            self.R = self.DATA_BUFFER[1::2]
            #lmin = self.L.min()
            #rmin = self.R.min()
            if np.sqrt(self.FrameRate) % 2 == 0:
                LEFT = self.L.reshape((int(np.sqrt(self.L.shape[0])),
                                       int(np.sqrt(self.L.shape[0]))))
                RIGHT = self.R.reshape((int(np.sqrt(self.R.shape[0])),
                                        int(np.sqrt(self.R.shape[0]))))


                images.append([plt.imshow(np.concatenate((LEFT,RIGHT),0),'gray')])
                print CITAL+CGREEN+CBOLD+"STYLE A"+CEND
            else:
                '''
                # print CITAL + CBLUE + CBOLD + "STYLE A" + CEND
                # filtah = [1,1,0,0,1,1,1,0,0,1,1]
                # filta2 = [0,0,1,1,0,0,0,1,1,1,1]
                # filterb = [[1,1,1],[1,0,1],[1,1,1]]
                # self.L = ndi.convolve(ndi.convolve(self.L,filtah)/self.L.max(),filta2,origin=0)
                '''
                L = np.abs(np.fft.fft(self.L, axis=0))
                iMatL = np.array(L[0:44100]).reshape((441,100))
                streak = [[0,0,1,0,0],
                          [0,1,1,1,0],
                          [1,0,1,0,1],
                          [0,1,1,1,0],
                          [0,0,1,0,0]]
                spark = [[1,0,1,0,1],
                         [0,1,0,1,0],
                         [0,1,1,1,0],
                         [0,1,0,1,0],
                         [1,0,1,0,1]]
                bloom = [[1,1,1,1,1],
                         [1,0,1,0,1],
                         [1,0,1,0,1],
                         [1,1,1,1,1]]
                buffd = [[1],[0],[0],[0],[1],[1],[0],[0],[0],[1]]

                # i = self.generateCascadingImages(ndi.convolve(iMatL[0:100, :],streak,origin=0),5)
                # for imat in i:
                #    i = plt.imshow(iMatL[0:100,:], 'rainbow')
                #    images.append([i])

                if frame%2==0:
                    alpha = np.array(ndi.convolve(iMatL[0:250, :]*10, spark, origin=0)).conjugate()
                else:
                    alpha = np.array(ndi.convolve(iMatL[0:250, :]*10, streak, origin=0)).conjugate()
                for pt in alpha.flatten():
                    if pt>3:
                        pt=5
                    if pt < 3 and iMatL.flatten()[frame]:
                        pt += 1
                images.append([plt.imshow(alpha[0:30,0:100],'rainbow')])
                images.append([plt.imshow(alpha[30:60, 0:100], 'rainbow')])
                images.append([plt.imshow(alpha[60:90, 0:100], 'rainbow')])
                images.append([plt.imshow(alpha[90:120, 0:100], 'rainbow')])
                images.append([plt.imshow(alpha[120:150, 0:100], 'rainbow')])
                #images.append([plt.imshow(iMatL, 'rainbow')])
                #images.append([plt.imshow(iMatL.conjugate(), 'rainbow')])

        stream.close()
        return images

    def generateCascadingImages(self,soundmat,recursion_depth):
        neighbors = [[1,1,1,1,1],[1,1,0,1,1],[1,1,1,1,1]]
        generation = 0
        cascade = []
        while generation < recursion_depth:
            seed = ndi.convolve(soundmat, neighbors, origin=0)
            index = 0
            copy = np.zeros((seed.shape[0]*seed.shape[1]))
            for cell in seed.flatten():
                if cell <= 5 or cell >=2:
                    copy[index] = 1
                elif soundmat.flatten()[index]==0 and cell==3:
                    copy[index] = 1
                index += 1
            seed = copy.reshape((soundmat.shape[0],soundmat.shape[1]))
            generation += 1
            cascade.append(seed)
        return cascade
def usage():
    print CBOLD + CITAL + "***************************" + CEND
    print CBOLD + CITAL + "*"+ CRED+"     INCORRECT USAGE!  " + CEND+CBOLD+CITAL+"  *"+CEND
    print CBOLD + CITAL + "***************************" + CEND
    try:
        os.system('paplay /usr/local/lib/python2.7/dist-packages/pygame/examples/data/punch.wav')
    except:
        pass
    return 0


def main():
    if len(sys.argv) != 2:
        usage()
    else:
        try:
            f = plt.figure()
            images = Visualize(sys.argv[1]).run(sys.argv[1])
            print "Rendering " + str(len(images)) + " images"
            a = animation.ArtistAnimation(f, images, interval=100,
                                          blit=True, repeat_delay=3000)
            plt.show()
        except KeyboardInterrupt:
            pass
        exit(0)


if __name__ == '__main__':
    main()
