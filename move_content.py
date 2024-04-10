import os
import sys
import shutil


if __name__ == '__main__':
  source_dir = sys.argv[1]
  dest_dir = sys.argv[2]

  files = os.listdir(source_dir)

  for f in files:
    shutil.copy2(os.path.join(source_dir, f), dest_dir)
    print(f'Copied {f}')