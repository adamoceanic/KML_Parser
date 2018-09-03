# Python script that takes in a specified kml file in the directory, strips the icons and timestamps,
# changes the track name to a specified name and then outputs to a new kml file in the directory

import os

if __name__ == "__main__":
	
	chk = os.listdir()
	
	# Enter the input file. Kml extension is not required
	inp = input("Please enter file name:")
	if inp[-4:] != ".kml":  inp += ".kml"
	while inp not in chk:
		print("Error: File not found in current directory.")
		inp = input("Please enter file name: ")
		if inp[-4:] != ".kml":
			inp += ".kml"
	
	# Set output file, kml extension not required, will be added if not inputted.
	out = input("Enter name of output file: ")
	if out[-4:] != ".kml":
		out += ".kml"
	
	track = input("Please enter name of track: ")  # Desired name of the track
	
	f = "".join(open(inp, "r").readlines())
	
	f = f[:f.find("<name>") + 6] + track + f[f.find("</name>"):]
	
	# Strips the data stored within <Point>
	while f.find("<Point>") != -1:
		f = f[:f.find("<Point>")] + f[f.find("</Point>") + 8:]
	
	# Strips the data stored within <IconStyle>
	while f.find("<IconStyle>") != -1:
		f = f[:f.find("<IconStyle>")] + f[f.find("</IconStyle>") + 12:]
	
	open(out, "w").write(f)
