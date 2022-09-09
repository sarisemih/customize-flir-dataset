def labelIndex(label):            # Uncomment the labels you want to use.
    if label == ["person"]:
        return 0                  # Check the json file for the name of the classes. Organize by datasets.
    if label == ["car"]:
        return 1
    if label == ["bike"]:
        return 2
    if label == ["motor"]:
        return 3
    if label == ["bus"]:
        return 4
    if label == ["truck"]:
        return 5
    #if label == ["light"]:
        return 6
    #if label == ["hydrant"]:
        return 7
    #if label == ["sign"]:
        return 8
    #if label == ["skateboard"]:
        return 9
    #if label == ["stroller"]:
        return 10
    #if label == ["other vehicle"]:
        return 11
    else:
        return -1


