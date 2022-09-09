import json
import numpy
import os
import sys
from labels import labelIndex

jsonFolderPath = sys.argv[1]
for file in os.listdir(jsonFolderPath):
    if file.endswith(".json"):
        jsonPath = os.path.join(jsonFolderPath, file)

        # Reading json file
        f = open(jsonPath)
        data = json.load(f)
        f.close()
        break

os.mkdir(os.path.join(jsonFolderPath, "labels"))
os.chdir(os.path.join(jsonFolderPath, "labels"))

# Create label txt files
for index, element in enumerate(data["frames"]):
    height, width = element["height"], element["width"]

    txt_name = "video-"+element["videoMetadata"]["videoId"] +\
               "-frame-"+(6-len(str(element["videoMetadata"]["frameIndex"])))*"0" +\
               str(element["videoMetadata"]["frameIndex"]) +\
               "-"+element["datasetFrameId"]+".txt"
    txtFile = open(txt_name, "a")
    for box_index in range(len(element["annotations"])):
        boundingBox = element["annotations"][box_index]["boundingBox"]
        keys = ["x", "y", "w", "h"]
        boundingBox = numpy.array([boundingBox.get(key) for key in keys], dtype=numpy.float64)
        boundingBox[:2] += boundingBox[2:] / 2  # xy top-left corner to center
        boundingBox[[0, 2]] /= width  # x
        boundingBox[[1, 3]] /= height  # y

        label = labelIndex(element["annotations"][box_index]["labels"])
        if label != -1:
            listToStr = ' '.join([str(elem) for elem in boundingBox])
            listToStr = str(label)+" "+listToStr+"\n"
            txtFile.write(listToStr)

    txtFile.close()
