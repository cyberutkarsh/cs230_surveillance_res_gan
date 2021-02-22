#! /bin/bash
##### DO THIS FIRST
# conda activate IQA-optimization | This needs to be done manually
##### DO THIS FIRST

algo_file=$1 #e.g. VIF.py
output_file=$2 #path to csv file that will have results
path_to_IQA_pytorch_dir=$3 # path to directory containing he Algo files
resolution_filename_mapping_path=$4 #path and filename for mapping file (generated in Step 1)

cd $path_to_IQA_pytorch_dir
while IFS="," read -r filename resolution
do
  ref_fname="$filename"
  dist_fname="${ref_fname/upscaled_/original_}"
  score=$(python $algo_file --ref $ref_fname --dist $dist_fname)
  echo "$filename,$score" >> $output_file
done < <(tail -n +2 $resolution_filename_mapping_path)
