# Unsupervised Segmentation
Using unsupervised method to do semantic segmentation on cell images.  

The work was edited from [Double DIP: Unsupervised Image Decomposition via Coupled Deep-Image-Priors.](https://github.com/yossigandelsman/DoubleDIP)
---

## Overview

### Data

The dataset is in folder `DATA`.

### Training

Train first step for 2000 iterations, only restrained by hints.  
Train second step for 4000 iterations, add reconstruction loss, hint restrain relaxed after 1000 iterations.  
Early stop with PSNR over 30.  

---

## Usage

### pre-processing.ipynb
get foreground and background hints from original images.  

### run.ipynb
run network to get mask results save in to `outputs` folder.

### evaluation.ipynb
calculated accuracy, IoU, Dice metrics of the results.

### continue_run.ipynb
Pre-trained on ground truth mask hint, use this pre-trained model to do segmentation on other image with rough hint. 

---
