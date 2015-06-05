# Multimedia Systems Laboratory Works


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


#### Task1: Rotate an image at 90 degrees

To obtain the rotation of an image we simply have to change the method of obtaining the image matrices. 
__OpenCV__ provides scaled rotation with adjustable center of rotation so that you can rotate at any location you prefer.


To find this transformation matrix, OpenCV provides a function, `cv2.getRotationMatrix2D`. 

        M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
        dst = cv2.warpAffine(img,M,(cols,rows))
  
  __Note:__ The following code does not scale the image. 


And use the same methods for displaying the images.

#### Output task 2

![output task 2](https://github.com/line2sun/sm_labs/blob/master/lab1/misc/Screenshot%202015-06-05%2011.23.33.png "output for Task 2")






