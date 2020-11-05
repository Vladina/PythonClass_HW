import sys
import argparse
from argparse import ArgumentParser
import os
from typing import Any, Union
import shutil

parser = ArgumentParser()
parser.add_argument('-f', '--folder-name', required=True)
parser.add_argument('-fl', '--file-name', required=True)
args = parser.parse_args()

file_path = os.path.abspath(__file__)
dir_name = os.path.dirname(file_path)
# os.mkdir(f'{dir_name}/{args.folder_name}')

with open(args.file_name, 'w') as new_file:
    pass

print(os.path.abspath(args.file_name))
print(os.listdir())
print(os.path.join(os.path.dirname(file_path), args.folder_name, args.file_name))

# os.replace({dir_name}/{new_file}, {dir_name}/{args.folder_name}/{new_file})
#
# os.rename('dinav/PycharmProjects/pythonProject/Lesson14/Some_File',
#           'dinav/PycharmProjects/pythonProject/Lesson14/Task14_05/Some_File')
#
# Currently dir_fd parameters only work on Unix platforms; none of them work on Windows.
print(os.stat in os.supports_dir_fd)