Image Processing
The program performs a statistical analysis to determine the percentage of the image that is green, ranging from light to dark hues. It also displays the original image with the detected green color highlighted.
Algorithm Explanation:
Using the OpenCV library, the program first reads the given image and loads its colors, ignoring any transparency. It then converts the image's color space from BGR (Blue, Green, Red) to HSV (Hue, Saturation, Value). Next, the program defines two bounds to represent the hues of green:
•	The lower bound represents the lightest green.
•	The upper bound represents the darkest green.




•	The first value (hue) is measured in degrees on the color wheel.
•	The second value (saturation) indicates the intensity level of a color.
•	The third value (value) refers to the brightness level, where 0 is completely black (no brightness at all) and 255 is the brightest.

The program then creates a mask—a binary image where pixels within the defined green color area are set to white, and all other pixels are set to black. This mask isolates all the green areas in the image, setting them to white, while all non-green areas are set to black.
To analyze the percentage of green color in the image, we sum up all the white pixels in the mask, then sum up all the pixels in the image. The percentage of the green area is calculated by dividing the sum of white pixels by the total number of pixels and multiplying the result by 100.
To display the image with the detected green color highlighted, the program uses the mask, where the detected color appears as white pixels and all other colors appear as black. The mask is displayed indefinitely until a key is pressed, at which point all OpenCV windows are closed.
Finally, the program returns the percentage of the green area within the given image.

![image](https://github.com/EmilyBederov/picture-processing/assets/151040825/f93bc75e-8fdf-4687-8482-5c8f7e13a78a)
