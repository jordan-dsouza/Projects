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
3. NumPy arrays **X** contains image pixels and **y**  contains the respective labels **[0,1,2]**.

### Train Test Split:
1. _80%_ dataset for training, _20%_ for testing.
2. Stratify ensures that the above ratio _(80:20)_ is maintained.

## Model:
We finally come to the most important part.
<br>**THE MODEL**</br>
My model is a Sequential Model consisting of:
1. **Input**: <br>Shape (128,128,1)</br>
2. **Conv2D**: <br>Convolution layer extracts spatial features of an image with help of a kernel or filter. My model has two of these layers, first with 32 kernels and second with 64 kernels.</br>
3. **Batch Normalization**: <br>Batch Normalization is a technique used in training neural networks to improve their stability and speed of convergence by normalizing the input to each layer.
   My model has two such layers. </br>
4. **MaxPooling2D**:<br>Reduces spatial dimensions while retaining important features. In my model, it selects maximum pixel value using a (2x2) filter. My model has two such layers.</br>
5. **Dropout**:<br> Randomly zeroes out a certain percentage of neurons during training to prevent overfitting and improve the model's generalization ability. This is achieved by setting the output of randomly selected neurons to zero with a specified probability (dropout rate). For input the dropout rate is 0.3 and for dense layer it is 0.5.</br>
6. **Flatten**:<br>Flattens inputs.</br>
7. **Dense**:<br>Deeply connected layer. Every neuron is connected to every other neuron in previous layer so droput rate is set to 50%.</br>

## Model Compiler:
1. My model is compiled with the **ADAM** (short for Adaptive Moment Estimation) optimizer which is highly effective, especially when working with large datasets and complex models, because it is memory-efficient and adapts the learning rate dynamically for each parameter.
2. Loss is **Sparse Categorical Cross Entropy** which is designed for cases where the target labels are not one-hot encoded.
3. Metric is **accuracy**.

## Model Training:
1. I have used **Early Stopping** which is a regularization technique used in machine learning to prevent overfitting by stopping the training process before the model begins to memorize the training data and loses its ability to generalize to new, unseen data. Here, early stopping is done if _validation loss_ doesn't improve after 3 epochs.
2. Model is trained using 10 epochs with batch size 32.
3. Time taken: 33 min.

## Model Testing:
1. Test accuracy is 78.47%.
2. "_Loss over Epochs_" and "_Accuracy over Epochs_" graphs have been shown.

## Pretrained Model MobileNetV2:
1. Input shape is (128,128,3). Default channels are 3 (RGB), so I have to resize my images and add 3 channels.
2. Model training is similar to my model with same parameters.
3. Some layers are frozen so as to not train it again and save time.
4. Test accuracy is 94.06%.

## Model Accuracy Improvement:
<br>There are various ways to improve model accuracy. I haven't followed them all due to time, memory and resource constraints.</br>
1. Adding more layers including Dense, Dropout and Batch Normalization (Explained why in the [Model](#model) section). Training time increased to 33 min.
2. Image size could be increased to (224,224) for more accuracy.
3. K fold cross validation can find the best parameters by dividing the dataset into "k" folds and training/testing the model. If k=5 (4 train, 1 test), training time x 5.
4. Unfreeze the frozen layers of the pretrained model.
