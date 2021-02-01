# CNN BASED SURVEILLANCE VIDEO UPSCALE
Implementation of CVPR 2016 paper 
[Real-Time Single Image and Video Super-Resolution Using an Efficient Sub-Pixel Convolutional Neural Network](https://arxiv.org/abs/1609.05158).
We will use this as baseline model for our project.

## Requirements
- [Anaconda](https://www.anaconda.com/download/)
- PyTorch
```
conda install pytorch torchvision cuda80 # install it if you have installed cuda
```
- PyTorchNet
```
pip install git+https://github.com/pytorch/tnt.git@master
```
- opencv
```
conda install opencv
```

## Datasets

### Train、Val Dataset
The train and val datasets are sampled from [VOC2012](http://host.robots.ox.ac.uk/pascal/VOC/voc2012/).
Train dataset has 16700 images and Val dataset has 425 images.
Download the datasets from [here](https://drive.google.com/drive/u/0/folders/1I8cg0YbUW3k1sKfdtF38slE0tX6eOFUi), 
and then extract it into `data` directory. 

Note: You need to have the following directory structure for VOC2012 directory under the **data** directory if you are 
running the for VOC2012 dataset (**ignore** _**test, train and val**_ for this step)
```
├── test
│   └── VOC2012_3
│       ├── images
│       └── videos
├── train
│   └── VOC2012_3
│       ├── data
│       └── target
├── val
│   └── VOC2012_3
│       ├── data
│       └── target
└── VOC2012
    ├── train
    └── val
```

Finally run
```
python data_utils.py

optional arguments:
--upscale_factor      super resolution upscale factor [default value is 3]
--dataset_name        name of the dataset e.g. "UCF" [default is "VOC2012"]
```
to generate train and val datasets from VOC2012 with given upscale factors(options: 2、3、4、8).

## Usage

### Train

```
python train.py --num_epochs 5

OR

python -m visdom.server & python train.py --num_epochs 5 [OPTIONAL if you want to visualize loss using visdom UI]

optional arguments:
--upscale_factor      super resolution upscale factor [default value is 3]
--num_epochs          super resolution epochs number [default value is 100]
```
Visdom now can be accessed by going to `127.0.0.1:8097` in your browser, 
or your own host address if specified.

If the above does not work, try using an SSH tunnel to your server by 
adding the following line to your local `~/.ssh/config` :
`LocalForward 127.0.0.1:8097 127.0.0.1:8097`.

### Test Image

Add Test Images to data/test/<dataset_name_upscalefactor>/images/ directory something like below

```
├── test
│   └── VOC2012_3
│       ├── images
```

and then run ...

```
python test_image.py

optional arguments:
--upscale_factor      super resolution upscale factor [default value is 3]
--model_name          super resolution model name [default value is epoch_3_100.pt]
```
The output high resolution images are on `results/<dataset_name>_<upscalefactor>/images/` directory.

### Test Video

Add Test Images to data/test/<dataset_name>_<upscalefactor>/videos/ directory something like below

```
├── test
│   └── VOC2012_3
│       └── videos
```

and then run ...

```
python test_video.py

optional arguments:
--upscale_factor      super resolution upscale factor [default value is 3]
--is_real_time        super resolution real time to show [default value is False]
--delay_time          super resolution delay time to show [default value is 1]
--model_name          super resolution model name [default value is epoch_3_100.pt]
```
The output high resolution videos are on `results/<dataset_name>_<upscalefactor>/videos/` directory.

### Lets Start Experimenting !!!