# Django-based-website-Weather-Image-Recognition

# Author
- Bruno Schwartz

# Details
The project involves developing a Django-based website comprising two frontend pages:
- The initial page serves as a Login Page which includes user registration and authentication functionalities.
- The second page is designated for implementing a pre-built Convolutional Neural Network (CNN) classifier to do Weather Image Recognition. Within the homepage, a table will be presented, featuring each user-uploaded image alongside its corresponding class prediction. An image Upload button allows users to upload multiple images simultaneously. A Submit button triggers the prediction process. Upon making a prediction, relevant information is stored including the image and its class, and showcase it within the aforementioned table.

The dataset used can be downloaded from the following link: 
[dataset](https://www.kaggle.com/datasets/jehanbhathena/weather-dataset)

Inside the `model` folder, the file `Weather_Image_Recognition.ipynb` contains the source code necessary to generate the .h5 model file that needs to be stored in the root of the Django files with the name `model-ResNet50.h5`.

# Preview
<img width="450" alt="image" src="https://github.com/Bruno-Schwartz/Django-based-website-Weather-Image-Recognition/assets/preview.png">
