## End to End Fashion Item Classification using Convolutional Neural Networks

## Overview

This project demonstrates how to classify fashion items using Convolutional Neural Networks (CNNs). It includes a FastAPI application for serving the model and a web interface for users to upload images and get classification results.


## Run the Project Directly

To run this project directly, open a terminal and execute the following commands:

1. **Pull the Docker Image**:
   
   ```bash
   docker pull mitul012/fas-img-class
    ```

2. **Run the Docker Container**:
   
   ```bash
   docker run -p 8000:8000 mitul012/fas-img-class
    ```

This will start the FastAPI application, and it will be accessible at http://localhost:8000.


## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
  - [Model Training](#model-training)
  - [Model Serving](#model-serving)
  - [Frontend Interface](#frontend-interface)
- [API Endpoints](#api-endpoints)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)
- [Deployment on AWS](#deployment-on-aws)

## Project Overview

The objective of this project is to classify images of clothing items into their respective categories using a Convolutional Neural Network (CNN) model. The Fashion MNIST dataset, which consists of 70,000 grayscale images in 10 categories, is used to train and evaluate the model.

Additionally, a frontend interface allows users to upload images for classification, and the entire application is containerized using Docker for ease of deployment.

## Dataset

The Fashion MNIST dataset is a collection of images of fashion items such as T-shirts, trousers, pullovers, dresses, etc. It is available through TensorFlow/Keras datasets.

## Installation

To run this project locally, follow these steps:

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/fashion-item-classification.git
    cd fashion-item-classification
    ```

2. Set up a virtual environment:

    ```sh
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Model Training

To train the CNN model, run:



