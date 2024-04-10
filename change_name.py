import os, shutil
import xml.etree.ElementTree as ET

# def remove_folder_content(path_to_folder):
#   for filename in path_to_folder:

#     file_path = os.path.join(path_to_folder, filename)

#     try:
#       if os.path.isfile(file_path) or os.path.islink(file_path):
#         os.unlink(file_path)
#       elif os.path.isdir(file_path):
#         shutil.rmtree(file_path)

#     except Exception as e:
#       print(f'Could not delete {file_path} because of {e}')

def rename_in_xml(path_to_xml_file, new_name):
  tree = ET.parse(path_to_xml_file) # get the xml tree
  root = tree.getroot() # get the root element
  file_name = root.find('filename') # find the filename (EX: <filename>something</filename> )
  depth = root.find('size/depth')
  try:
    file_name.text = new_name # modify the filename element
    depth.text = '3'
    tree.write(path_to_xml_file) # save the changes
  except Exception as e:
    print(f'Could not modify because {e}')

# def add_depth(path_to_xml_file):
#   tree = ET.parse(path_to_xml_file) # get the xml tree
#   root = tree.getroot() # get the root element
#   depth = root.find('depth') # find the filename (EX: <filename>something</filename> )
#   print(depth.text)

if __name__ == '__main__':
  KEYWORD = 'frame_' # shouldn't be changed
  dir_content = os.listdir('Annotations')
  path_to_directory = os.path.join(os.getcwd(), 'Annotations')

  for file_name in dir_content:

    path_to_file = os.path.join(path_to_directory, file_name) # path to file
    starting_idx = path_to_file.find(KEYWORD) # idx of where the word 'frame_' starts
    old_name = path_to_file[starting_idx + len(KEYWORD):] # from the end of 'frame_' onwards
    path_before_old_name = path_to_file[:starting_idx + len(KEYWORD)] # full path until the end of 'frame_'

    for char in old_name: # remove the 0's one by one until a non-zero number is found
      if char != '0':
        break
      else:
        old_name = old_name[1:]

    new_name = old_name # transfer variable
    new_path_to_file = path_before_old_name + new_name # create new path to file
    name_for_inside_xml_file = ((KEYWORD + new_name)[:-4]) + '.png' # add extension for inside the xml file

    os.rename(path_to_file, new_path_to_file) # rename the old path to file to the new one
    try:
      rename_in_xml(new_path_to_file, name_for_inside_xml_file) # replace: path_to_file | with: new_path_to_file
    except Exception as e:
      print(f'Could not finish the operation because of {e}')
    
