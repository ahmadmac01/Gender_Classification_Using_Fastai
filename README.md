# Gender Classification Using Fastai
Gender classifier using fastai library.
This project is a Gender Image Classifier built using the FastAI library. The classifier uses a ResNet-18 model to differentiate between male and female faces. The data for training and testing is gathered from Fastbook, and various data processing techniques are applied to ensure the accuracy of the model.

## Table of Contents
* Installation
* Data Gathering and Processing
* Model Training
* Use Case
### Installation
  To run this project, you need to have FastAI and Fastbook installed. You can install them using pip:

    !pip install fastai fastbook

### Data Gathering and Processing

The data for this project is collected using the search_images_ddg function from Fastbook, which gathers images from the internet based on specified search terms.
* **Search and Download Images:**
 1. Male faces
 2. Female faces
* **Verify and Remove Failed Images:**

    Use verify_images to remove any corrupted or invalid images.

* **Data Block Setup:**

    Define a DataBlock for image classification with proper item and batch transformations.

### Model Training
  The model is trained using a ResNet-18 architecture with a fine-tuning approach.

* **Initialize Learner:**

  Use vision_learner to create a learner object with ResNet-18.

* **Fine-Tune the Model:**

  Train the model for a few epochs to improve its performance.

### Use Case

This Gender Image Classifier can be used in various applications such as:

* Automated sorting of images based on gender for data organization.
* Preprocessing step in facial recognition systems to categorize faces by gender.

#### [Hugging Face spaces Link](https://huggingface.co/spaces/ahmadmac/gender)

