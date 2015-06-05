# Multimedia Systems Laboratory Works

## Requirements & Installation

* [OpenCV](https://jjyap.wordpress.com/2014/05/24/installing-opencv-2-4-9-on-mac-osx-with-python-support/)
* [NumPy](http://www.scipy.org/scipylib/download.html)
* [PyGame](http://www.reddit.com/r/pygame/comments/21tp7n/how_to_install_pygame_on_osx_mavericks/)
* [pydub](https://github.com/jiaaro/pydub#installation)

__Note:__ `NumPy` package comes along with `SciPy` library.


__Note2:__ I run OS X 10.10, in case that some scripts aren't running as expected, 
contact me at [pascaripavel@gmail.com](pascaripavel@gmail.com). 


## Lab 1: Image Processing

#### Task1: Resize/Scale an image

`OpenCV` provides two transformation functions, `cv2.warpAffine` and `cv2.warpPerspective`, 
with which you can have all kinds of transformations. `cv2.warpAffine` takes a 2x3 transformation matrix 
while `cv2.warpPerspective` takes a 3x3 transformation matrix as input.

__Scaling__ / __Resizing__ Scaling is just resizing of the image. 
OpenCV comes with a function `cv2.resize()` for this purpose. 
The size of the image can be specified manually, or you can specify the scaling factor. 

Different interpolation methods are used. Preferable interpolation methods are `cv2.INTER_AREA` for shrinking
and `cv2.INTER_CUBIC` (slow) & `cv2.INTER_LINEAR` for zooming. 

By default, interpolation method used is `cv2.INTER_LINEAR` for all resizing purposes.
  
1. To load an image use `cv2.imread(img_path)`

        import cv2
        import numpy as np

        img = cv2.imread('messi5.jpg')

2. To get the rows and columns of the image:
        
        rows,cols = img.shape

3. The transformations of the images are done by using simple `numpy` methods on matrices.

        M = np.float32([[1,0,100],[0,1,50]])

4. To obtain the new image:
        
        dst = cv2.warpAffine(img,M,(cols,rows))
  
  __Note:__ Third argument of the `cv2.warpAffine()` function is the size of the output image,
   which should be in the form of (width, height, where width = number of columns, and height = number of rows).
   
5. Showing the image:

        cv2.imshow('img',dst)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
  
  __Note:__ `OpenCV` comes with a built-in UI generation framework, that, also, contains key binding support.
  
#### Output task 1

![output task 1](https://github.com/line2sun/sm_labs/blob/master/lab1/misc/Screenshot%202015-06-05%2011.23.16.png "output for Task 1")


#### Task2: Rotate an image at 90 degrees

To obtain the rotation of an image we simply have to change the method of obtaining the image matrices. 
__OpenCV__ provides scaled rotation with adjustable center of rotation so that you can rotate at any location you prefer.


To find this transformation matrix, OpenCV provides a function, `cv2.getRotationMatrix2D`. 

        M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
        dst = cv2.warpAffine(img,M,(cols,rows))
  
  __Note:__ The following code does not scale the image. 


And use the same methods for displaying the images.

#### Output task 2

![output task 2](https://github.com/line2sun/sm_labs/blob/master/lab1/misc/Screenshot%202015-06-05%2011.23.33.png "output for Task 2")




# Lab 2: Audio Processing

#### Task1: Play 2 audio files simultaneously

For this assignment, I have used `PyGame` and `pydub` libraries. (to install them, follow the links above)
 
The sound and music API's of `PyGame` and `pydub` are fairly simple. I feel funny basically going through the 
documentation and re-iterating it.

Sounds require the creation of sound objects that you have to hold on to. Much like images. 
Sounds have a simple `.play()` method that will start playing the sound.

So, we first have to init the mixer and load the sound:
    
        def init_sound(self, filename):
            pygame.init()
            pygame.mixer.init()
            pygame.mixer.music.load(filename.encode('utf8'))


__Note:__ Taking into consideration that creation of the User Interface is beyond of this course, I'll skip `Tk` code explanation.

In order to get the second audio file played alongside the first one I used `AudioSegment` module of `pydub`.

AudioSegment objects are immutable, and support a number of operators:
* export
* creation of a zero duration segment (`.empty()`)
* volume manipulation
* channels shuffling
* frame rates manipulations
* frame width manipulations
* etc.

The `another_song()` function asks `Tk` for the path to a new file. Creates an `AudioSegment`
object and sends it to `PyGame`'s mixer in order to play it.

        def another_song(self):
                filename = tkFileDialog.askopenfilename()
                sound = AudioSegment.from_mp3(filename)
                sound.export("~/Desktop/music.wav", format="wav")
                if not pygame.mixer.init():
                    pygame.mixer.init()
                snd1 = pygame.mixer.Sound("~/Desktop/music.wav")
                snd1.play()


## Lab 3: Video Processing

#### Task1: Develop a desktop application that shows in real time the input from your webcam.

`OpenCV` provides a very simple interface to capture live stream with camera.
To capture a video, we need to create a `VideoCapture` object. 
Its argument can be either the device index or the name of a video file. 
Device index is just the number to specify which camera. 

__Note:__ It is possible to select the second camera by passing 1 and so on. 

After that, you can capture frame-by-frame. 
__Note2:__ Don’t forget to release the capture. ;)

1. Initialize a `VideoCapture` object:
        
        import numpy as np
        import cv2

        cap = cv2.VideoCapture(0)
        
2. The frames are captured in n infinite loop.


        while(True):
            ret, frame = cap.read()
        
            # Our operations on the frame come here
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
            # Display the resulting frame
            cv2.imshow('frame',gray)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

3. With `cap.read()` we capture frames from WEB Camera.

4. It is also possible to choose the color processing of each frame by passing `cv2.COLOR_BGR2GRAY` as an argument.

5. Show the image with the `OpenCV`'s `imshow()`.

6. Lines 18 and 19 hold the logic of quiting the app when the stuff is done, by catching the pressing of `q` key.

7. And, of course don't forget to clean up the things, by calling the `release()` method over `VideoCapture` instance:

        cap.release()
        cv2.destroyAllWindows()


#### Output task 1

![output task 1](https://github.com/line2sun/sm_labs/blob/master/lab3/misc/Screenshot%202015-06-05%2010.48.40.png "output for Task 1")


