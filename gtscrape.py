import csv
header = ["Title", "Description", "Lat", "Long"]

with open('GT.csv', 'rb') as infile, open('gtscraped.csv', 'wb') as outfile:
  incsv = csv.reader(infile, delimiter=',', quotechar='"')
  outcsv = csv.writer(outfile, delimiter=',', quotechar='"')
  outcsv.writerow(header)
  for line in incsv:
    #spline = line.split(",")
    if line[0] != "" and line[0] != "Title": #check for non-empty title
      title = line[0]
      description = "<h2>goal:</h2> <p> %s </p><h2>status</h2><p> %s </p><h2>Progress Detail:</h2> <p> %s </p><h2>Challenges and Barriers:</h2><p> %s </p><h2>Next Steps:</h2> <p> %s </p>" % (line[1], line[8], line[11], line[12], line[13])
      lat = ""
      lon = ""
      outcsv.writerow([title, description, lat, lon])
