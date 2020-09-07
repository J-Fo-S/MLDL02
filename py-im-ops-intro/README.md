### py-im-ops-intro

Before we go anywhere near machine or deep learning, we have some familiarizing to do with Python and some of its core packages. In particular, we'll need to operate with various types of data for a variety of processing tasks that one often encounters in machine and deep learning. 

*Note that we are using the term **familiarity**, and not something like "mastery".* There are 2 points: 1 is that you will get better as you practice, so be patient with yourself if you don't understand all at once. Taken together with our immersion into such large and experimental fields as machine and deep learning, understanding all at once is probably impossible.

The 2nd point is that most of the machine and deep learning code we will be working with are pre-programmed and will run. So we don't have to write anything from scratch (that would actually be very advanced). Instead, our goal is to begin to understand each part of these large programs 1 by 1, and how we may work with and modify the programming for our goals. In time, we'll be able to understand the entire system. For now, we'll go piece-by-piece.

The programs here are intended in the following order:
1. py-gen-ops-intro
2. np-plt-img-intro
3. seam-carve

### Tasks: py-gen-ops-intro
1. Write a function that returns the result of a basic math formula to a variable
2. Write a function that returns a different result depending if its argument is greater or less than some value, and throws an error if the argument is a string
3. Write a function that prints returns a list of the letters of a string one by one
4. Write a function that scrambles the the lines of poem.txt and saves it as a newly named txt file.

### Tasks:np-plt-img-intro
1. Plot an accurate representation of the length of a soundwave of 55hz in comparison to ones of 550hz and 5,500 hz.
2. Find a real life example for both a uniform and a normal probability distribution, and plot an example of each based on their actual parameters (according to your research).
3. Design and plot another handwriting example that can be mimmicked with the addition of noise (e.g. perhaps a smiley face or some other doodle).
4. Experiment with different images and changing the parameters for the image convolution section. What parameters visibly work best, and are they consistent for each different image? And what is the effect of larger and smaller convolution kernels?
5. Write a function that shows images SVD encoded from rank 1 - 50.

### Tasks: seam-carve
1. Have fun with this neat algorithm and find which images it works well with and not - and determine why.


### Sources/resources:

**[Stanford CS231n Python-Numpy tutorial](http://cs231n.github.io/python-numpy-tutorial/)**

**[scikit-image processing examples](http://scikit-image.org/docs/dev/auto_examples/index.html)** 

**[imgaug library with many image augmentation exs](http://scikit-image.org/docs/dev/auto_examples/index.html)** https://github.com/aleju/imgaug 

**[image kernels visually explained](http://setosa.io/ev/image-kernels/)** 

**[image convolution interactive python](http://machinelearninguru.com/computer_vision/basics/convolution/image_convolution_1.html)** 

**[edge detection tutorial in python](http://blog.yhat.com/posts/image-processing-with-scikit-image.html)** 

**[SVD image compression explanation](https://blogs.sas.com/content/iml/2017/08/28/singular-value-decomposition-svd-sas.html)** 

**[seam-carving tutorial in python](https://karthikkaranth.me/blog/implementing-seam-carving-with-python?utm_source=mybridge&utm_medium=blog&utm_campaign=read_more)**

