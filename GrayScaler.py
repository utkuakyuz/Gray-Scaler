import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#matplotlib.image library takes just .png files so do not try to use a jpeg or different formats of image

def gray_scaler(image): #This Function takes an image as parameter and make operations on its matrix.
    a=  image[:,:,0]    #Alghorithm for gray scaler is R+G+B/3 for every pixel of image which means every 
    b = image[:,:,1]    #lot of its matrix. This Function makes this operation for each pixel of image and returns
    c = image[:,:,2]    #a gray scaled image with this algorithm. a is red, b is blue, c is green value and z is gray value.
    Z = (a+b+c)/3
    print(a[0])
    image[:,:,0] = Z
    image[:,:,1] = Z
    image[:,:,2] = Z
    return image #This is the gray scaled image.
def anti_alias(matrix2, T):
    K = 0
    while K != T:
        K = K + 1
        for i in range(len(matrix2)-1):
            for j in range(len(matrix2[i])-1):
                matrix2[i][j][2] = (matrix2[i][j + 1][2] + matrix2[i][j - 1][2] + matrix2[i + 1 ][j][2] + matrix2[i - 1][j][2])/4
    return matrix2

def plotter(image, image2): #This function takes 2 images and plots them with using subplot commands. Output is
                            #2 images on a plot which is called subplot. Also images have title as RGB and Gray 
    plt.figure(dpi=150)     #And plt.figure(dpi?) value is 100 as default but to have a bigger and high quality photos
    plt.subplot(1,2,1)      #dpi can be increased. Output with default value is very low quality, so i changed it to 150.
    plt.title("RGB")
    plt.imshow(img2)
    plt.subplot(1,2,2)  #This subplot commands can be rewritten as plt.subplot(2,1,1) , (2,2,2)
    plt.title('Gray')
    plt.imshow(img)
    
    return plt.show() #This function returns 1 plot with 2 images.


img = mpimg.imread("sample.png") 
img2 = mpimg.imread("sample.png")   #Reading 2 .png images with mpimg commands.


gray_scaler(img)        #Calling the gray scaler function.
anti_alias(img,5)
plotter(img, img2)      #Calling plotter function.