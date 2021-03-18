#!/bin/bash
input_directory=$1 #directory holding up-scaled images
resolution_filename_mapping_path=$2 #path and filename for mapping file

for filename in $input_directory/*.jpg; do
    echo "$filename,$(ffmpeg -i $filename 2>&1 | grep -oP 'Stream .*, \K[0-9]+x[0-9]+')" >> $resolution_filename_mapping_path
done

