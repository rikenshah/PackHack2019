from PIL import Image

def crop_image(path, section, save=False):
	original = Image.open(path)
	filename, file_extension = os.path.splitext(path)
	width, height = original.size

	if section == 1:
		left = 0
		top = 0
		right = width/2
		bottom = height/2
	elif section == 2:
		left = width/2
		top = 0
		right = width
		bottom = height/2
	elif section == 3:
		left = width/2
		top = height/2
		right = width
		bottom = height
	elif section == 4:
		left = 0
		top = height/2
		right = width/2
		bottom = height
	else:
		return
	if(save):
		path = 'images/cropped'+str(file_extension)
	cropped_example = original.crop((left, top, right, bottom))
	cropped_example.save(path)