## USEFUL PYTHON SCRIPTS FOR WORKING WITH DIRECTORIES AND LARGE AMOUNTS OF FILES IN COLAB

# NOTE
- CLI pathnames that contain whitespaces can still be used by wrapping the path in quotation marks
  - Example: ```python3 change_CVAT_pasc_voc_annot_filename.py "/Users/../pascal voc annotations"```

# change_CVAT_pasc_voc_annot_filename.py
- CVAT bounding box annotation creation (with tracking option) creates xml files that do not correspond to the names of the images (ex. frame_54.png and frame_000054.xml)
- This causes problems
- This program removes all the zeros before the number starts and updates the .png filename inside the xml file itself.
- **positional arguments for running with CLI:**
  1. .xml annotation files directory path (if there are whitespaces in the path, surround path with quotations marks)
- **EXAMPLE:**
  - ```python3 change_CVAT_pasc_voc_annot_filename.py /Users/../../../annotations```

# copy_folder_content.py
- Copies the content of one folder to another
- **EXAMPLE:**
  - ```python3 copy_folder_content.py /Users/../../../source /Users/../../../destination```

# move_folder_content.py
- Moves the content of one folder to another
- **EXAMPLE:**
  - ```python3 move_folder_content.py /Users/../../../source /Users/../../../destination```

## split_image_set.py
- Randomly splits (by user-definded %) the content of an image/xml folder and moves one part into a train and the other part into a test folder
- The mixed (train and test) source folder needs to have images with the corresponding annotation xml file (pascal voc)
- The name of the png files (the image) without the extension .png must coincide with the name of the xml files without the extension .xml (Example: frame_58.png and frame_58.xml)
- **positional arguments for running with CLI:**
  1. source_dir
  2. train_dir (can already exist or will be created at specified location)
  3. test_dir (can already exist or will be created at specified location)
  4. train_percentage (Ex: 80 -> 80 % of folder content goes to train and 20% goes to test)
- **EXAMPLE:**
  - ```python3 split_image_set.py /Users/../../../mixed /Users/../../../train /Users/../../../test 80```
  - Where 'mixed' is the folder that contains (ex): frame_1.png, frame_1.xml, frame_2.png, frame_2.xml, etc...