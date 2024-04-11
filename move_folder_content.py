import os
import shutil
import argparse

def run_parser():
  parser = argparse.ArgumentParser(
      prog='move_folder_content.py',
      description='Move content from one folder to another'
    )
  parser.add_argument('source_dir', type=str)
  parser.add_argument('dest_dir', type=str)
  args = parser.parse_args()
  return args

if __name__ == '__main__':
  args = run_parser()
  source_dir = args.source_dir
  dest_dir = args.dest_dir

  if not os.path.exists(source_dir):
    raise Exception('Source folder does not exist')

  if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)
    
  files = os.listdir(source_dir)

  for f in files:
    shutil.move(os.path.join(source_dir, f), dest_dir)
    print(f'Moved {f} from {source_dir} to {dest_dir}')