import os
import argparse
import random
import shutil



def run_parser():
  parser = argparse.ArgumentParser(
      prog='split_image_set.py',
      description='Split directory content into train and test data.'
    )
  parser.add_argument('source_dir')
  parser.add_argument('train_dir')
  parser.add_argument('test_dir')
  parser.add_argument('train_percentage')
  args = parser.parse_args()
  return args


if __name__ == '__main__':
  args = run_parser()
  source_dir = args.source_dir
  train_dir = args.train_dir
  test_dir = args.test_dir
  desired_train_percent = int(args.train_percentage)

  if not os.path.exists(train_dir):
    os.mkdir(train_dir)
  if not os.path.exists(test_dir):
    os.mkdir(test_dir)


  files = os.listdir(source_dir)

  if len(files) % 2 == 0: # check for equal even amount of files, as we need equal amount of xml and png files
    train_files_nr = round(((len(files)/2)/100)*desired_train_percent) # get the 80 %
    train_files_nr = int(train_files_nr)
    files = os.listdir(source_dir)

    i = 0
    while (i < train_files_nr):

      rnd_idx = random.randint(0, len(files)-1)
      filename = files[rnd_idx]
      no_extension_name = filename[:-4]

      if not os.path.exists(os.path.join(source_dir, filename)):
        continue

      if str(filename).endswith('.xml'):
        shutil.move(os.path.join(source_dir, filename), train_dir) # move the xml file
        shutil.move(os.path.join(source_dir, no_extension_name + '.png'), train_dir) # move corresponding png
      elif str(filename).endswith('.png'):
        shutil.move(os.path.join(source_dir, filename), train_dir) # move the png file
        shutil.move(os.path.join(source_dir, no_extension_name + '.xml'), train_dir) # move corresponding xml
      i+=1

    remaining_files = os.listdir(source_dir)

    for f in remaining_files:
      shutil.move(os.path.join(source_dir, f), test_dir)
  else:
    print('There is not an equal number of xml and png files!')
      


  

  