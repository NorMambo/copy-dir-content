import os
import argparse
import xml.etree.ElementTree as ET

def rename_in_xml(path_to_xml_file, new_name):
  tree = ET.parse(path_to_xml_file) # get the xml tree
  root = tree.getroot() # get the root element
  file_name = root.find('filename') # find the filename (EX: <filename>something</filename> )
  depth = root.find('size/depth')
  try:
    file_name.text = new_name # modify the filename element
    depth.text = '3' # 3 is for color image
    tree.write(path_to_xml_file) # save the changes
  except Exception as e:
    print(f'Could not modify because {e}')

def run_parser():
  parser = argparse.ArgumentParser(
      prog='change_CVAT_pasc_voc_annot_filename.py',
      description='Rename the CVAT pascal voc annotations'
    )
  parser.add_argument('annotations_dir', type=str)
  args = parser.parse_args()
  return args

if __name__ == '__main__':
  KEYWORD = 'frame_' # shouldn't be changed
  args = run_parser()
  annotations_dir = args.annotations_dir

  dir_content = os.listdir(annotations_dir)

  for file_name in dir_content:

    path_to_file = os.path.join(annotations_dir, file_name) # path to file
    starting_idx = path_to_file.find(KEYWORD) # idx of where the word 'frame_' starts
    old_name = path_to_file[starting_idx + len(KEYWORD):] # from the end of 'frame_' onwards
    path_before_old_name = path_to_file[:starting_idx + len(KEYWORD)] # full path until the end of 'frame_'

    new_name = old_name
    for char in new_name: # remove the 0's one by one until a non-zero number is found
      if char != '0':
        break
      else:
        new_name = new_name[1:]

    new_path_to_file = path_before_old_name + new_name # create new path to file
    name_for_inside_xml_file = ((KEYWORD + new_name)[:-4]) + '.png' # add extension for inside the xml file

    try:
      os.rename(path_to_file, new_path_to_file) # rename the old path to file to the new one
      print(f'Renamed {old_name} to {new_name}')
    except Exception as e:
      print(f'Failed to rename {file_name} because {e}')

    try:
      rename_in_xml(new_path_to_file, name_for_inside_xml_file) # replace: path_to_file | with: new_path_to_file
    except Exception as e:
      print(f'Could not finish the operation because of {e}')
    
