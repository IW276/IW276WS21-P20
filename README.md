# Project-Template for IW276 Autonome Systeme Labor

After former projects already focused on identifying objects in images and video feeds this project is about re-identifying those objects in a sequence of images.

<p align="center">
  
  [Demo Video](https://github.com/IW276/IW276WS21-P20/blob/master/resources/2022-01-13%2019-16-16.mkv)
  
  [Presentation Video](https://github.com/IW276/IW276WS21-P20/blob/master/resources/AutonomeSystemeLabor_IW276WS21P20video.mp4)
</p>

> This work was done by Sascha Isele, Michael Niepalla, Kai Michael Schwark during the IW276 Autonome Systeme Labor at the Karlsruhe University of Applied Sciences (Hochschule Karlruhe - Technik und Wirtschaft) in WS 2021 / 2022. 

## Table of Contents

* [Requirements](#requirements)
* [Prerequisites](#prerequisites)
* [Docker](#docker)
* [Running](#running)
* [Acknowledgments](#acknowledgments)

## Requirements
* Python 3.6 (or above)
* OpenCV 4.1 (or above)
* Jetson Nano
* Jetpack 4.4
> [Optional] Monitor, mouse & keyboard directly connected to the Jetson Nano

## Prerequisites
1. Clone the repository
```
// https
git clone https://github.com/IW276/IW276WS21-P20.git

// ssh
git clone git@github.com:IW276/IW276WS21-P20.git
```

2. Move inside the directory
```
cd IW276WS21-P20
```

3. Enable jetson_clocks to increase performance
```
sudo jetson_clocks
```

4. (optional) using own images and detectionfile

If you intend to use your own data you have to put the images into the "/dataset" folder of the repository.
Best is to put the images into for a folder called "/dataset/img" for example and the detection file into "/dataset/det" to have it seperated.

If you already have such kind of folder structure just copy it using the following command and insert te correct paths.
```
cp -a /source/. /dest/
```
if you dont have the folder structure as mentioned above add the folders using 
```
mkdir /new-directory-path/
```

> [Optional] If you intend to view the process live you have to use a monitor directly connected to the Jetson Nano, else there will most likely be an error telling you "could not connect to display / Aborted (core dumped)"

## Docker

Executing and building the project is done using docker.

### Build

Execute the following code in order to build the docker image (while being in the project folder /IW276WS21-P20)

```
sudo bash docker-build.sh
```

## Running

To run the demo, pass path to the pre-trained checkpoint and camera id (or path to video file):
```
sudo bash docker-run.sh
```

In the Docker container run the three commands listed below together with one of the 4 options listet below.

```
cd /deep-person-reid
python3 setup.py develop
cd /src
```
Option 1: run application using builtin sample data with gui
```
python3 opencv_gui.py --image_path --detection_path --identified_images
```
Option 2: run application using builtin sample data headless
```
mkdir /images_outputfolder
python3 opencv_gui.py --identified_images /images_outputfolder
```
Option 3: run application using own data with gui
```
python3 opencv_gui.py --image_path IMAGES_FOLDER_LOCATION_PATH --detection_path DET_FILE_PATH
```
> INFO: own images and detection file need to be placed in the /datasets folder previous to building.

Option 4: run application using own data headless
```
mkdir /images_outputfolder
python3 opencv_gui.py --image_path IMAGES_FOLDER_LOCATION_PATH --detection_path DET_FILE_PATH --identified_images /images_outputfolder
```
> INFO: own images and detection file need to be placed in the /datasets folder previous to building.


> INFO: for option 1 and 3 remember to have a monitor connected to you Jetson Nano.

## Acknowledgments

This repo is based on
  - [deep-person-reid](https://github.com/KaiyangZhou/deep-person-reid)
  - [L4T-ML](https://ngc.nvidia.com/catalog/containers/nvidia:l4t-ml)

Thanks to the original authors for their work!

## Contact
Please email `mickael.cormier AT iosb.fraunhofer.de` for further questions.
