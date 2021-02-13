# KML_Parser
Handy tool to munge raw kml/gps data into a formats needed for my flight tracking application
In order to use, copy desired .kml file into same directory as python script. Run script and input the file name when asked 
(kml extension not required). Enter desired output file (kml extension not required) and the name of the track when opened in 
Google Earth.
To Do: More efficient parser, current relies on putting kml file in memory and then slicing the Point and IconStyle out, then outputting
to new file
