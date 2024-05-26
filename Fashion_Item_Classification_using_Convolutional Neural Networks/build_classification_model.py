# Bringing in tensorflow
import tensorflow as tf
# Below code will prevent the error to occur , memory crashed
gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)

# Bringing in matplotlib for viz stuff
from matplotlib import pyplot as plt

# Do some data transformation
import numpy as np

# For dataset and Model Dumping
from tensorflow import keras # type: ignore

# Loading Fashion_mnist Dataset
fashion_mnist=keras.datasets.fashion_mnist
(train_images,train_labels),(test_images,test_labels)=fashion_mnist.load_data()

# Scaling the images in range 0 to 1
train_images=train_images/255.0
test_images=test_images/255.0


# Bring in the sequential api for the generator and discriminator
from tensorflow.keras.models import Sequential # type: ignore
# Bring in the layers for the neural network
from tensorflow.keras.layers import Conv2D, Dense, Flatten, Reshape, LeakyReLU, Dropout, UpSampling2D # type: ignore

# Model Initialization

model = Sequential([            
   Flatten(input_shape=(28,28)),
   Dense(128,activation=tf.nn.relu),
   Dense(10,activation=tf.nn.softmax)
])

# Compile the model using the correct optimizer
model.compile(optimizer=tf.keras.optimizers.Adam(), # type: ignore
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.summary()

# Training the model
model.fit(train_images,train_labels,epochs=30)

#Evaluating the model
test_loss,test_acc=model.evaluate(test_images,test_labels)
print("Model Accuracy" ,test_acc)


from keras.models import load_model # type: ignore
# Assuming your Keras model is named 'model'
model.save('Fashion_Mnist_CNN_Model.h5')
print("Model Saved")

