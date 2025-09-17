# Vision demos

Visualizations of the vision system's inner workings. Not all aspects are 100% scientifically accurate, but the demos illustrate the basic principles well.

# Installation
```
pip install -f requirements.txt
```

to install the dependencies (numpy, opencv-python, and pyautogui)

# Demos

## Edge detection
The demo performs edge detection via difference of Gaussians (DOG). Horizontal mouse position controls the positive Gaussian's width; vertical position, the negative Gaussian.

The retina exhibits a similar mechanism, with ON and OFF bipolar cells 

## Color opponent channels
This demo illustrates how the red, green, and blue cone cells respond to their corresponding colors, and combinations thereof form the color-opponent channels of red-green and blue-yellow (plus luminance).