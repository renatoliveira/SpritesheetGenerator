import sys
from PIL import Image

# path = "E:/Blender/isometric/animations/"
# test = Image.open(path + "0000.png")
# print(test.size)

def numberToFileName(n):
	nameLen = len(str(n))
	if nameLen < 4:
		# increase number of zeroes in the filename
		newName = ""
		for h in range(4 - nameLen):
			newName += "0"
		newName += str(n)
	return newName

inputFolderPath  = sys.argv[1]
outputFolderPath = sys.argv[2]
totalFrames      = sys.argv[3]
imageSize        = sys.argv[4]
fileType         = sys.argv[5]

imageArray = []

# assuming all images have the same size, to generate
# the spritesheet we need to calculate the size of it,
# which is done by: number of images * size of images
# eg: 10 * 500 = 5000
#     10 images
#    500 pixels each

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

for i in range(int(totalFrames)):
	print("Pasting at " + str(i * int(imageSize)))
	# composition.paste(imageArray[i], (i * int(imageSize), int(imageSize)))
	composition.paste(imageArray[i], (i * int(imageSize),0))

composition.save(inputFolderPath + "/outputfile.png", fileType)