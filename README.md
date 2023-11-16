# Image Processing Analysis

This program conducts a statistical analysis to ascertain the percentage of the green color present within an image, considering all shades from light to dark green. It also showcases the original image with the highlighted green color that has been detected.

## Algorithm Explanation

### Step 1: Read the Image
Using the **OpenCV library**, the program initiates the process by reading the input image and loading its color data, while ignoring any transparency present.

### Step 2: Convert Color Space
The color space of the image is converted from BGR (Blue, Green, Red) to HSV (Hue, Saturation, Value) to better analyze and detect colors.

### Step 3: Define Green Hue Bounds
The program sets two bounds to capture the spectrum of green hues within the image:

```python
green_lower_bound = np.array([36, 25, 25])  # Represents the lightest green
green_upper_bound = np.array([86, 255, 255]) # Represents the darkest green
```

Hue: First value, measured in degrees on the color wheel.
Saturation: Second value, indicating the color intensity.
Value: Third value, indicating the brightness level, where 0 is completely black and 255 is the brightest.

![Hue]((https://answers.opencv.org/upfiles/15186761085555681.png))


### Step 4: Create a Mask
A mask is generated where:

Pixels within the green color area are set to white.
All other pixels are set to black.
This effectively isolates the green areas in the image.

### Step 5: Analyze Green Percentage
The analysis involves calculating the sum of white pixels (representing green) in the mask and the total number of pixels in the image:

``` Calculate the percentage of green in the image
sum_white_pixels = np.sum(mask == 255)
percentage_of_green = (np.sum(mask == 255) / total_pixels) * 100
```

### Step 6: Display the Mask
The mask is displayed, highlighting the detected green color against a black background. This display continues until any key is pressed, which then triggers the closure of all OpenCV windows.

### Step 7: Return the Percentage
Finally, the calculated percentage of the green area within the image is returned by the program.
