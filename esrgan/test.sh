model_path=$1 #generator model path e.g generator_99.pth
image_path=$2
python test_on_image.py --checkpoint_model "$model_path" --image_path "$image_path"
