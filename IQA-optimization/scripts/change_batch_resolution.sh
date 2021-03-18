#! /bin/bash
resolution_filename_mapping_path=$1 #path and filename for mapping file (generated in Step 1)

#while IFS="," read -r filename resolution
#do
#  fname="$filename"
  # new_fname="${fname/original_/upscaled_}"
#  new_fname="${fname/upscaled_/original_}"
#  res="$resolution"
#  new_res="${res/x/:}"
#  yes | ffmpeg -i $new_fname -vf scale=$new_res $new_fname
#done < <(tail -n +2 $resolution_filename_mapping_path)


while IFS="," read -r filename resolution
do
  fname=$filename
  new_fname=$(echo "$fname" | sed "s/original/downscaled/")
  yes | ffmpeg -i $new_fname -vf scale="iw/4:ih/4" $new_fname
  #echo $new_fname
done <"$resolution_filename_mapping_path"
