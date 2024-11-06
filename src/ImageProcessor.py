import os
from PIL import Image
import numpy

class ImageProcessor:

	def __init__(self, path: str):
		self.__path = path

	def process_folder(self, size: int):
		savedirPath = self.__path + "/processed"
		try:
			os.rmdir(savedirPath)
		except:
			pass
		os.mkdir(savedirPath)
		for imagePath in os.listdir(self.__path):
			print(imagePath)
			imageFile: Image.ImageFile = Image.open(self.__path + "/" + imagePath)
			resizedImage: Image.ImageFile = self.__resize(imageFile, size)
			filledImage: Image.Image = self.__add_padding(resizedImage)
			filledImage.save(savedirPath + "/" + imagePath)
			print("alerte4")

	
	def __resize(self, imageFile: Image.Image, size: int) -> Image.Image:
		image = numpy.array(imageFile)
		height = image.shape[0]
		width = image.shape[1]

		if width > height:
			width = width * (size * 100 // height)
		elif height > width:
			height = height * (size * 100 // width)

		image = numpy.resize(image, (height, width))

		return Image.fromarray(image)


	def __add_padding(self, imageFile: Image.Image) -> Image.Image:
		image = numpy.array(imageFile)
		height = image.shape[0]
		width = image.shape[1]

		if height == width:
			return imageFile
		elif height > width:
			return Image.fromarray(numpy.resize(image, (height, height)))
		else:
			return Image.fromarray(numpy.resize(image, (width, width)))
