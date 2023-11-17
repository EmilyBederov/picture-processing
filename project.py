import cv2
import numpy as np

def process(image_path):

    img = cv2.imread(image_path, 1)
    #equalized_img = cv2.equalizeHist(img)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    #shades of grren
    green_lower_bound = np.array([36, 25, 25])
    green_upper_bound = np.array([86, 255, 255])
    
    #creating a mask
    mask = cv2.inRange(hsv, green_lower_bound, green_upper_bound)
    
    #calc the white pixels in the mask
    sum_white_pixels = np.sum(mask == 255)

    #total number of pixels
    width, height = img.shape[:2]
    Total_pixels = width * height

    #displaying the og image with the detected color highlighted
    cv2.imshow('color display', mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return (sum_white_pixels / Total_pixels) * 100

print("precntege of green is:\n" , process('/Users/emilybederov/Desktop/picture_proccesing/tree.jpg'), "%")

