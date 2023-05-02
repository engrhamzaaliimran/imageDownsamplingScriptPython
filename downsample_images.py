from PIL import Image
import os

# define the source and destination folders
src_folder = '/path/to/source/folder'
dst_folder = '/path/to/destination/folder'

# set the maximum image size (in pixels)
max_size = (1024, 1024)

# loop through all files in the source folder
for file_name in os.listdir(src_folder):
    # check if the file is an image
    if file_name.endswith('.jpg') or file_name.endswith('.jpeg') or file_name.endswith('.png'):
        # open the image file
        img = Image.open(os.path.join(src_folder, file_name))

        # get the current image size
        curr_size = img.size

        # check if the image needs to be downsampled
        if curr_size[0] > max_size[0] or curr_size[1] > max_size[1]:
            # calculate the new image size
            ratio = min(float(max_size[0])/curr_size[0], float(max_size[1])/curr_size[1])
            new_size = (int(round(curr_size[0]*ratio)), int(round(curr_size[1]*ratio)))

            # downsample the image
            img = img.resize(new_size, resample=Image.LANCZOS)

        # save the downsampled image to the destination folder
        img.save(os.path.join(dst_folder, file_name))
