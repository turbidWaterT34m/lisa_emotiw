#script to read all bounding boxes and create histogram for  width and height values of bounding boxes

import os
import csv
import pylab as P

path = '/data/lisa/data/faces/EmotiW/picasa_boxes/Train'
bbox = []
heights = []
widths = []

id = 0

for root, subdirs, files in os.walk(path):
    for file in files:
        if os.path.splitext(file)[1].lower() in ('.txt'):
            filePath = os.path.join(root, file)
            data = open (filePath,"r")
            c = csv.reader(data, delimiter=',', skipinitialspace=True)
            for line in c:
                print id
                id += 1
                bb = []
                for val in line:
                    bb.append(int(val))
                heights.append(bb[3]-bb[1])
                widths.append(bb[2]-bb[0])
                bbox.append(bb)
                

    
print len(heights)

# the histogram of the data with histtype='step'
n, bins, patches = P.hist(heights, 100, normed=0, histtype='bar')
P.setp(patches, 'facecolor', 'r', 'alpha', 0.75)
P.show()


