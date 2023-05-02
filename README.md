# Image Downsampling Script
This is a Python script that downsamples all images in a given directory to a specified maximum size.

## Requirements
To run this script, you need to have the following packages installed:

## Pillow
You can install the required packages using pip:

pip install -r requirements.txt

## Usage
To use this script, follow these steps:

Clone the repository or download the script downsample_images.py to your local machine.

Navigate to the directory where the script is located in a command prompt or terminal window.

Run the script using the following command:

python downsample_images.py /path/to/source/folder /path/to/destination/folder max_width max_height

Replace /path/to/source/folder with the path to the directory containing the images you want to downsample, and replace /path/to/destination/folder with 
the path to the directory where you want to save the downsampled images.

You can also specify the maximum width and height of the downsampled images by replacing max_width and max_height with the desired values. If you don't specify these values, the default maximum size of 1024x1024 pixels will be used.

The script will loop through all the image files in the source directory and downsample each image that is larger than the specified maximum size. The downsampled images will be saved in the destination directory.

Example
Here's an example command that downsamples all images in the directory /home/user/images to a maximum size of 800x800 pixels and saves the downsampled images in the directory /home/user/downsampled_images:


python downsample_images.py /home/user/images /home/user/downsampled_images 800 800

## License
This script is licensed under the MIT License. Feel free to use, modify, and distribute it as you like. See the LICENSE file for more information.
