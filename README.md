# Face Spoof Detection using Deep Learning

## Project Overview

This project is a deep learning based project- **face spoof detection system** that identifies whether a face presented to a camera is a **real human face** or a **spoof attack** such as a photo or a screen replay.

The model is trained on a face anti-spoofing dataset using transfer learning with a hybrid architecture built from **ResNet50** and **VGG16**. After training, the model is used in a real-time webcam application that detects a face, predicts whether it is real or fake, and displays the prediction with a confidence score.

The project is implemented in **Python**, trained in **Google Colab**, and tested locally using **OpenCV**.

---

## Project Objectives

* Detect real and spoof faces using deep learning.
* Build a binary image classification model for face anti-spoofing.
* Use transfer learning to improve model performance.
* Perform real-time face spoof detection through a webcam.
* Save and reuse the trained model for live predictions.

---

## Features

* Binary classification: **REAL** or **SPOOF**.
* Hybrid deep learning model using **ResNet50** and **VGG16**.
* Image preprocessing and data augmentation.
* Automatic train, validation, and test dataset splitting.
* Class weight balancing for imbalanced data.
* Model accuracy and loss visualization.
* Confusion matrix and classification report for evaluation.
* Real-time webcam prediction with face detection.
* Confidence score displayed for every prediction.
* FPS display during live webcam detection.
* Option to save webcam snapshots.

---

## Technologies Used

| Category             | Tools and Libraries   |
| -------------------- | --------------------- |
| Programming Language | Python                |
| Deep Learning        | TensorFlow, Keras     |
| Computer Vision      | OpenCV                |
| Pre-trained Models   | ResNet50, VGG16       |
| Data Processing      | NumPy, Scikit-learn   |
| Visualization        | Matplotlib            |
| Environment          | Google Colab, VS Code |

---

## Project Workflow

1. Mount the dataset from Google Drive.
2. Extract the dataset into the working directory.
3. Split images into training, validation, and testing folders.
4. Apply image preprocessing and data augmentation.
5. Create balanced class weights.
6. Build a hybrid ResNet50 and VGG16 model.
7. Train the model on the training dataset.
8. Evaluate the model on the testing dataset.
9. Visualize accuracy and loss graphs.
10. Generate a confusion matrix and classification report.
11. Save the trained model as an H5 file.
12. Load the saved model for real-time webcam prediction.

---

## Dataset Structure

The dataset is organized into two classes:

```text
                                                   Dataset/
                                                      |
                —————————————————————————————————————————————————————————————————————————————————
                |                                     |                                          |
                |                                     |                                          |
              Train/                              Validation/                                  Test/
                |                                     |                                          |
                |——> REAL/                            |——> REAL/                                 |——> REAL/  
                |                                     |                                          |
                |——> SPOOF/                           |——> SPOOF/                                |——> SPOOF/ 
```

The notebook automatically creates the training, validation, and testing folders from the original dataset.

---

## Model Architecture

The model combines features extracted from two popular pre-trained convolutional neural networks:

* **ResNet50**
* **VGG16**

The extracted feature maps are combined using a skip connection and passed through fully connected layers to perform binary classification.

This hybrid architecture helps the model learn both deep and fine-level facial features useful for spoof detection.

---

## Data Preprocessing

The following preprocessing steps are applied before training:

* Image resizing to **224 × 224** pixels.
* Pixel value normalization.
* Random image rotation.
* Width and height shifting.
* Zoom augmentation.
* Horizontal flipping.
* Validation and test images are only normalized.

---

## Model Training

Training includes:

* Transfer learning using pre-trained ImageNet weights.
* Binary Cross Entropy loss function.
* Adam optimizer.
* Class weight balancing.
* Validation after every epoch.
* Fine-tuning by unfreezing the last layers of both backbone models.

---

## Model Evaluation

The trained model is evaluated using:

* Test accuracy.
* Test loss.
* Accuracy curve.
* Loss curve.
* Confusion matrix.
* Classification report including precision, recall, and F1-score.

These evaluation metrics help measure the model's spoof detection performance.

---

## Real-Time Face Spoof Detection

The real-time application performs the following steps:

1. Opens the webcam.
2. Detects a face using Haar Cascade.
3. Crops and preprocesses the detected face.
4. Loads the trained anti-spoofing model.
5. Predicts whether the face is **REAL** or **SPOOF**.
6. Displays the prediction and confidence score on the video frame.
7. Shows FPS for real-time performance.
8. Allows saving webcam snapshots.

---

## Project Structure

```text
Face-Spoof-Detection/
│
├── Face_Spoof_Detection.ipynb
├── realtime_antispoof.py
├── anti_spoofing_model.h5
├── dataset/
├── README.md
└── requirements.txt
```

---

## Installation

### Clone the repository

```bash
git clone <repository-url>
cd Face-Spoof-Detection
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the real-time detection

```bash
python realtime_antispoof.py
```

Make sure the trained model file `anti_spoofing_model.h5` is placed in the project directory before running the webcam application.

---

## Requirements

* Python 3.x
* TensorFlow
* OpenCV
* NumPy
* Matplotlib
* Scikit-learn

---

## Results

The project produces:

* A trained face anti-spoofing model.
* Accuracy and loss graphs after training.
* Confusion matrix for model evaluation.
* Real-time webcam detection showing **REAL** or **SPOOF** predictions with confidence scores.

---

## Author

**Atul Gaikwad**

Deep Learning and Computer Vision Project for Face Anti-Spoof Detection using TensorFlow, Keras, OpenCV, ResNet50, and VGG16.
