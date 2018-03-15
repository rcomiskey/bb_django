lines_seen = set() # holds lines already seen
fields_seen = set()
outfile = open('test_feed', "w")
for line in open('product_feed.csv', "r"):
    field = line.split(';')
    if field[2] and field[8] not in fields_seen: # not a duplicate
        outfile.write(line)
        fields_seen.add(field[2] and field[8])
        lines_seen.add(line)
       
outfile.close()

# lines_seen = [] # holds lines already seen
# fields_seen = []

# outfile = open('test_feed', "w")

# for line in open('product_feed.csv', "r"):
#     field = line.split(';')
#     if field[2] and field[8] not in fields_seen: # not a duplicate
#         fields_seen.append(field[2] and field[8])
#         lines_seen.append(line)
    
        
        # lines_seen row with match, add field[11] from feed to lines seen
        
        
# This script reads a GPS track in CSV format and
#  prints a list of coordinate pairs
# import csv
 
# # Set up input and output variables for the script
# gpsTrack = open('product_feed.csv', "r")
 
# # Set up CSV reader and process the header
# csvReader = csv.reader(gpsTrack)
# header = next(csvReader)
# latIndex = header.index("lat")
# lonIndex = header.index("long")
 
# # Make an empty list
# coordList = []
 
# # Loop through the lines in the file and get each coordinate
# for row in csvReader:
#     lat = row[latIndex]
#     lon = row[lonIndex]
#     coordList.append([lat,lon])
 
# # Print the coordinate list
# print (coordList)



