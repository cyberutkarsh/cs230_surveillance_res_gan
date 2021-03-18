model_path=$1 #generator model path e.g generator_99.pth
images_dir=$2

progress_bar()
{
  local PROG_BAR_MAX=${1:-30}
  local PROG_BAR_DELAY=${2:-1}
  local PROG_BAR_TODO=${3:-"."}
  local PROG_BAR_DONE=${4:-"|"}
  local i

  echo -en "["
  for i in `seq 1 $PROG_BAR_MAX`
  do
    echo -en "$PROG_BAR_TODO"
  done
  # Note: The following line echoes:
  # 1)   "]" (to end the "[...]" bar)
  # 2)   Control-M (aka Carriage Return) (aka Octal \0015)
  # 3)   "[" (to replace the original "[" and put the cursor in the right place)
  #echo -en "]^M["
  echo -en "]\0015["
  for i in `seq 1 $PROG_BAR_MAX`
  do
    echo -en "$PROG_BAR_DONE"
    sleep ${PROG_BAR_DELAY}
  done
  echo
}

# loop over directory
for filename in $images_dir/*.jpg; do
    python test_on_image.py --checkpoint_model "$model_path" --image_path "$filename" --residual_blocks 23
done
