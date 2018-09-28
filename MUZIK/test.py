import sys, os, time, wave, numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import scipy.ndimage as ndi

'''
start = time.time()
# plt.imshow(r,'gray')
conv1 = [[1,1,1,1,1],[1,1,0,1,1],[1,1,1,1,1]]
rc1 = ndi.convolve(r.reshape((100,100)),conv1,origin=0)
# plt.imshow(rc1, 'gray')
stop = time.time()
print("10k Image Codepoints in "+str(stop - start)+" seconds. ")
#plt.show()
'''
#############################################################################################################3
r = np.random.rand(10000) > 0.3
plt.imshow(r.reshape((100,100)),'gray')
plt.title('SEED')
plt.show()

startA = time.time()
f = plt.figure()
generations = []
ngen = 100
gen = 0

bool_mask = [[True, True, True,  True, True],
        [True, True, False, True, True],
        [True, True, True,  True, True]]
conv = [[1,1,1,1,1],[1,1,0,1,1],[1,1,1,1,1]]
print(np.array(ndi.convolve(r.reshape((100,100)),bool_mask)))
copy = np.random.rand(10000) > 0.7
while gen < ngen:
    index = 0
    convflatmat = ndi.convolve(copy.reshape((100,100)),conv,origin=0)
    swaps = 0
    for pt in r.flatten():
        cell = convflatmat.flatten()
        if cell[index]<=3:
            copy[index] = 1
        else:
            copy[index] = 0
            #print(np.nonzero(cell[index]))
        index += 1
    print('Generation '+str(gen)+' '+str(swaps)+' swaps made')
    generations.append([plt.imshow(copy.reshape(100,100),'gray')])
    gen += 1
stopA = time.time()
print(str(len(generations))+" frames computed in "+str(stopA-startA)+" seconds")
a = animation.ArtistAnimation(f,generations,interval=30,
                              blit=True,repeat_delay=2000)
plt.show()