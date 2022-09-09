### CustomizeFlirDataset ~ JSONtoYolo
Convert and customize FLIR dataset  to YOLO txt files. Works with any Conservator formatted annotation (JSON) file.

### Usage:
- Json file  must be in conservator format.
- This script will convert labels in your json file to yolo format and creates the labels folder. You can select the labels you want to convert from the `labels.py`  
- Converted YOLO annotation files have `.txt` extension. Txt files are located in the labels folder.
- Edit your ```labels.py``` based on the labels found in your json file

### Demo:
- JSON TO YOLO:
   - ```python jsontoyolo/convert.py demo/jsonfolder```
   - After that the ```.txt``` files should appear in the ```demo/jsonfolder/labels``` folder.
