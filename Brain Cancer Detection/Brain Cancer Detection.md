## Overview:
1. This project uses the "Orvile Brain Cancer MRI Dataset" from Kaggle.
2. Using the "Kaggle json" I downloaded the dataset directly into Google Colab.
3. Dataset contains 3 classes: Brain Glioma, Brain Menin and Brain Tumor.
4. Main libraries used are OpenCV (cv2), TensorFlow (Keras), Scikit-Learn and NumPy.
5. I have also compared my model with the MobileNetV2 (Frozen base) model which has higher accuracy and performance.

## Images:
The images are in **Greyscale** and I have displayed 2 images of each class. Image size is (512,512).

## Pipeline:
### Load and Preprocess images:
1. Image classes have been labelled as followed: **Glioma (1), Menin (2), Tumor (3).**
2. I have resized the images to size **(128,128)** and normalized pixels to **[0,1]**.
3. NumPy arrays **X** contains image pixels and **y**  contains the respective labels [0,1,2].

### Train Test Split:
1. _80%_ dataset for training, _20%_ for testing.
2. Stratify ensures that the above ratio _(80:20)_ is maintained.

## Model:
We finally come to the most important part.
<br>**THE MODEL**</br>
My model is a Sequential Model consisting of:
1. **Input**: <br>Shape (128,128,1)</br>
2. **Conv2D**: <br>Convolution layer extracts spatial features of an image with help of a kernel or filter. My model has two of these layers, first with 32 kernels and second with 64 kernels.</br>
3. 
