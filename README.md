# RGB to Gray Image Conversion and Anti-Aliasing
This Python code is used for converting an RGB image to a grayscale image using the R+G+B/3 algorithm. It also contains a function for anti-aliasing which smooths out the image by averaging pixel values. The code imports the matplotlib.pyplot and matplotlib.image libraries.

![image](https://user-images.githubusercontent.com/79662515/235304639-881de962-b764-4784-a7c9-463f8cf7013a.png)

## Functions
The code includes the following functions:

`gray_scaler(image)`
This function takes an RGB image as a parameter and returns a grayscale version of the image. The function first separates the red, green, and blue color values for each pixel in the image using slicing operations. Then, it calculates the gray value for each pixel by taking the average of the red, green, and blue values. Finally, it updates the image matrix with the gray values and returns the grayscale image.

`anti_alias(matrix2, T)`
This function takes an image matrix and an integer T as parameters. It performs anti-aliasing on the image by smoothing out the pixel values. The function loops through the image matrix and calculates the average of the pixel values in its immediate neighbors. This value is then used to update the pixel value of the current pixel. The process is repeated T number of times. The function returns the updated image matrix.

`plotter(image, image2)`
This function takes two images (an RGB image and a grayscale image) as parameters and plots them side by side using subplot commands. The function sets the titles of the images as "RGB" and "Gray" respectively. The function returns the plot.

## Usage
To use the code, first save the RGB image as a .png file. Then, call the mpimg.imread() function from the matplotlib.image library to read the image file. Pass this image to the gray_scaler() function to convert it to grayscale. Finally, call the anti_alias() function to perform anti-aliasing on the image. The resulting grayscale image can then be plotted alongside the original RGB image using the plotter() function.

Note that the gray_scaler() function only works with .png files as the matplotlib.image library only supports this format.
