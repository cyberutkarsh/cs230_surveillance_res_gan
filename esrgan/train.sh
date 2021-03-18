dataset_name=$1
#python3 -m visdom.server & python3 esrgan.py --batch_size 5 --dataset_name "$dataset_name"  --n_epochs=100 --checkpoint_interval 10
python3 esrgan.py --batch_size 5 --dataset_name "$dataset_name"  --n_epochs=200 --checkpoint_interval 10 --residual_blocks 23
