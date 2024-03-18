import os
from os.path import join, basename, isfile

cur_directory = os.path.dirname(os.path.realpath(__file__))

input_folder = f"{cur_directory}/input_videos"
output_folder = f"{cur_directory}/csv_output"

for filename in os.listdir(input_folder):
    in_filepath = join(input_folder, filename)
    # checking if it is a file
    if isfile(in_filepath):
        out_file_name = basename(filename)
        os.system(f"python3 -m ffmpeg_bitrate_stats  -a time -c 30 -of csv {input_folder}/{out_file_name}")
    
