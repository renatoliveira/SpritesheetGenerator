import sys
from PIL import Image

# translate the number of the file to open to a
# string we can actually use, in the format XXXX.png
# eg: not 1.png but 0001.png

def numberToFileName(n):
	nameLen = len(str(n))
	if nameLen < 4:
		# increase number of zeroes in the filename
		newName = ""
		for h in range(4 - nameLen):
			newName += "0"
		newName += str(n)
	return newName

# we need to get the command line arguments
# first the path to the input images
# second the path to the output image
# third the total frames/images
# fourth the image size (all images should have the
# 	same size)
# at last, the file type (png, jpg, etc)

inputFolderPath  = sys.argv[1]
outputFolderPath = sys.argv[2]
totalFrames      = sys.argv[3]
imageSize        = sys.argv[4]
fileType         = sys.argv[5]


# assuming all images have the same size, to generate
# the spritesheet we need to calculate the size of it,
# which is done by: number of images * size of images
# eg: 10 * 500 = 5000
#     10 images
#    500 pixels each

# we create an empty array of images and an empty 
# canvas (actually an empty image)

imageArray = []
comp_size = (int(totalFrames), imageSize)
composition = Image.new('RGBA', (int(totalFrames) * int(imageSize), int(imageSize)))

for i in range(int(totalFrames)):
	print("Range: " + totalFrames)
	print("File name: " + numberToFileName(i) + "." + fileType)
	print("For Index: " + str(i))
	
	imageArray.append(Image.open(str(inputFolderPath + "/" + numberToFileName(i)) + "." + fileType))
	if imageArray[i].mode != "RGBA":
		imageArray[i].convert("RGBA")
		print("Converted image to RGBA")

	print("Image: " + str(imageArray[i].size) + ", " + str(imageArray[i].mode))

print("All images loaded successfully!")


# now we run through the composition we created, pasting
# all the images we opened previously

for i in range(int(totalFrames)):
	print("Pasting at " + str(i * int(imageSize)))
	composition.paste(imageArray[i], (i * int(imageSize),0))

# lets save it
composition.save(inputFolderPath + "/outputfile." + fileType)

# we done bro
print("")
print("All done!")