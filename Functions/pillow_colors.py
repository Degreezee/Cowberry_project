from PIL import Image as IMG
from PIL import ImageColor as Color

def pillow_hex_to_dec(hexi:str):
	hexi = hexi.lower()
	# hexi is in format '#ffffff'
	dec = 0
	hexi_list = []
	l = [16**i for i in range(6)]
	hexi = hexi[1:]
	for i in hexi:
		if i == "a":
			i = 10
		elif i == "b":
			i = 11
		elif i == "c":
			i = 12
		elif i == "d":
			i = 13
		elif i == "e":
			i = 14
		elif i == "f":
			i = 15
		elif i.isdigit():
			i = int(i)
		else:
			print("String is not a hex value")
			return False
		hexi_list.append(i)
	hexi_list.reverse()
	for i, base_to_power in zip(hexi_list, l):
		dec += i * base_to_power
	return dec

  
def pillow_dec_to_hex(number:int):
	hexi = hex(number) #hexadecimal in the format 0xffffff
	hexi = hexi[2:] # removeing '0x'
		
	if len(hexi) < 6:
		missing_size = 6 - len(hexi) # calculating number of '0's to fill in
		hexi = "0" * missing_size + hexi # str * int is repeating str int num of times
		# this if fills in blacks: '1' --> '000001' 
	hexi = "#" + hexi # adding '#' to the start  of hexadecimal color 
	# so hexadecimal '0x0f55ae' turned into pillow form '#0f55ae'
	return hexi

def creating_shades(start_color, end_color, step_color):
	maximum_colors = 16**6-1 #constant
	if (start_color >= maximum_colors) or (end_color + 1 > maximum_colors):
		print("Colors beyond ffffff are not allowed")
		print("In decimals, maximum color is", maximum_colors) 
		print()
		return False # usually return False or -1 if unwanted result occures
	else:
		for i in range(start_color, end_color, step_color): # range(start, stop. step)
			c = pillow_dec_to_hex(i) # creating hex colour in the correct format
			new_img = IMG.new(mode="RGB", size=(100, 100), color=c)
			file_color_name = "c_" + c[1:] + ".png" # file name is 'c_ffffff.png'
			dirname = "ColorShades" # directory (dir) or folder name
			new_img.save(dirname + "/" + file_color_name)
		return True # usually True or 0 if code runs perfectly

def RGB_to_pillow_hex(rgb):
	hex_color = "{:X}{:X}{:X}".format(rgb[0], rgb[1], rgb[2])
	pillow_hex_color = "#" + "0"*(6-len(hex_color.lower())) + hex_color.lower()
	return pillow_hex_color

