# Unsupervised Segmentation
Using unsupervised method to do semantic segmentation on cell images.  

The work was edited from [Double DIP: Unsupervised Image Decomposition via Coupled Deep-Image-Priors](https://github.com/yossigandelsman/DoubleDIP)
---

## Overview

### Data

The dataset is in folder `DATA`.

### Training

Train first step, only restrained by hints.  
Train second step, add reconstruction loss, hint restrain relaxed after few iterations.  
Early stop if achieving PSNR goal.  

hyper-parameters:
- psnr_goal: PSNR goal, if achieved, stop second step.  
- output_path: result saving path.  
- show_every: frequency for saving results, results including networks output, mask output etc.
- first_step_iter_num, second_step_iter_num: choose total iteration times.  
- plot_during_training: whether to show loss value during training.

---

## Usage

### pre-processing.ipynb
get foreground and background hints from original images.  

### run.ipynb
run network to get mask results saved in to `outputs` folder.

### evaluation.ipynb
calculated accuracy, IoU, Dice metrics of the results.

### continue_run.ipynb
Pre-trained on ground truth mask hint, use this pre-trained model to do segmentation on other image with rough hint. 

---
