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