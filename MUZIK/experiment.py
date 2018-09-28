import numpy as np, sys, time, os
import matplotlib.pyplot as plt, matplotlib.animation as animation
import scipy.ndimage as ndi
import wave

conv = np.array([[0,1,1,1,0],
                 [1,1,2,1,1],
                 [1,2,3,2,1],
                 [1,1,2,2,1],
                 [0,1,1,1,0]], dtype=int)


flair = np.array([[1,0,1,0,1],
                  [0,1,1,1,0],
                  [0,0,2,0,0],
                  [0,1,1,1,0],
                  [1,0,1,0,1]])


# Prep space for the animation
film_reel = []
f = plt.figure()
# define the audio to examine
test_song = sys.argv[1]
# Open the stream
stream = wave.open(test_song, 'r')
# Start the Clock
start = time.time()
# get important fields from the stream
frame_rate = stream.getframerate()
nframes = stream.getnframes()
# iterate by frame through entire audio file
index = 0
for frame in range(nframes/frame_rate):
    # read a frame into data buffer, and split left and right channels
    data_buffer = np.fromstring(stream.readframes(frame_rate))
    left = data_buffer[0::2].reshape((120, 100))
    right = data_buffer[1::2].reshape((120, 100))
    # Create a visual sum of left and right audio
    visual = np.concatenate((left, right), 1)
    # add the image to the reel
    #film_reel.append([plt.imshow(visual, 'gray')])
    film_reel.append([plt.imshow(np.abs(np.fft.fft(ndi.convolve(visual, conv, origin=0), axis=1)), 'gray')])
    film_reel.append([plt.imshow(np.abs(np.fft.fft(ndi.convolve(visual,flair,origin=0),axis=1)), 'gray')])
    # film_reel.append([plt.imshow(np.abs(np.fft.fft(visual, axis=1)), 'rainbow')])
    # film_reel.append([plt.imshow(visual, 'rainbow')])
    index += 1
# Stop the clock
stop = time.time()
print '\033[34;0m'+"* "+str(stop-start) + " seconds elapsed " + '\033[0m'
print  "* Animating "+str(len(film_reel))+" Frames"
# Render the film reel into an animation and show it
a = animation.ArtistAnimation(f, film_reel, interval= 333,
                              blit=True, repeat_delay=1000)
print"* Total Time elapsed After Rendering: " + str(time.time() - start)
plt.show()
