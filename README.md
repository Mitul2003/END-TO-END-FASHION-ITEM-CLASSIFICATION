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
- [Deployment on AWS](#deployment-on-aws)
- [License](#license)

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

```sh
python build_classification_model.py
```

### Model Serving

To serve the trained model using FastAPI and Docker:

1 . Build the Docker image:

```sh
docker build -t fashion-item-classification.
```

2 . Run the Docker container:

```sh
docker run --platform linux/amd64 -p 8000:8000 fashion-item-classification

```

#### Frontend Interface

The application includes a simple HTML interface to upload images and see the classification results. Once the Docker container is running, access the frontend interface by navigating to http://localhost:8000 in your web browser.

## API Endpoints

- `POST /upload`: Upload an image for classification.

#### Example

To classify an image, send a POST request to /upload with the image file: 

```sh
curl -X POST "http://localhost:8000/upload" -H "accept: application/json" -H "Content-Type: multipart/form-data" -F "image=@/path/to/your/image.png"
```
## Results

The model achieves an accuracy of approximately 88% on the test set.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or new features.

## Deployment on AWS

To deploy this project on AWS, follow these steps:

### Prerequisites

1 . An AWS account
2 . AWS CLI configured
3 . An EC2 instance with Docker installed

**Steps**

1 .Launch an EC2 instance:

- Choose an Amazon Machine Image (AMI) such as Amazon Linux 2.
- Select an instance type (e.g., t2.micro for free tier eligibility).
- Configure the security group to allow inbound traffic on port 8000.

2 . Connect to the EC2 instance:

Use SSH to connect to your instance.

```sh
ssh -i /path/to/your-key-pair.pem ec2-user@your-ec2-instance-public-dns
```
3 . Install Docker on the EC2 instance:

```sh
sudo yum update -y
sudo amazon-linux-extras install docker
sudo service docker start
sudo usermod -a -G docker ec2-user
```

4 . Clone the repository on the EC2 instance :

```sh
git clone https://github.com/yourusername/fashion-item-classification.git
cd fashion-item-classification
```

5 . Build and run the Docker container:

```sh
docker build -t fashion-item-classification .
docker run --platform linux/amd64 -p 8000:8000 fashion-item-classification
```

6 . Access the application:

 - Open your web browser and navigate to http://<your-ec2-instance-public-dns>:8000 to access the frontend interface.
   
You should now be able to upload images and see the classification results from the model running on your AWS EC2 instance.

By following these instructions, you can deploy your Fashion Item Classification project on AWS and make it accessible over the internet.

```sh

### Explanation
- **Project Overview**: General description of the project and its objectives.
- **Dataset**: Brief description of the dataset used.
- **Installation**: Step-by-step instructions to set up the project locally.
- **Usage**: Instructions on how to train the model, serve it using Docker, and interact with the frontend.
- **API Endpoints**: Description of the API endpoint with an example using `curl`.
- **Results**: Placeholder for model performance and example classifications.
- **Contributing**: Information for potential contributors.
- **License**: Licensing information.
- **Deployment on AWS**: Detailed steps on how to deploy the application to AWS EC2, including instance setup, Docker installation, and accessing the deployed application.

Make sure to replace placeholders like `https://github.com/yourusername/fashion-item-classification.git` and `<your-ec2-instance-public-dns>` with your actual repository URL and your EC2 instance's public DNS address, respectively.
```

## License
This project is licensed under the MIT License. See the LICENSE file for details.
