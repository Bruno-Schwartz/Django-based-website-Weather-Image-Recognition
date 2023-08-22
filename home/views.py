from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import ImagePrediction

from PIL import Image
import keras
import numpy as np
import os
from django.core.files.storage import FileSystemStorage


# Create your views here.
def home(request):
    # Count the number of users registered
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # User name is unique and passwords match
        if form.is_valid():
            # Save the form
            form.save()
            # Redirect to the home page
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {
        'form': form
    })


# The folder to save the files is set here
media = 'media'
# The model is associated here
model = keras.models.load_model('model-ResNet50.h5')


# The functions for the CPSC project are copied and modify it to adapt it to multiclass predictions
def makepredictions(path):
    # we open the image
    img = Image.open(path)
    # we resize the image for model
    img_d = img.resize((256, 256))
    # we check if image is RGB or not
    if len(np.array(img_d).shape) < 4:
        rgb_img = Image.new("RGB", img_d.size)
        rgb_img.paste(img_d)
    else:
        rgb_img = img_d

    # here we convert the image into numpy array and reshape
    rgb_img = np.array(rgb_img, dtype=np.float64)
    rgb_img /= 255.
    rgb_img = rgb_img.reshape(1, 256, 256, 3)

    # we make predictions here
    predictions = model.predict(rgb_img)
    a = int(np.argmax(predictions))

    if a == 0:
        a = 'dew'
    elif a == 1:
        a = 'fogsmog'
    elif a == 2:
        a = 'frost'
    elif a == 3:
        a = 'glaze'
    elif a == 4:
        a = 'hail'
    elif a == 5:
        a = 'lightning'
    elif a == 6:
        a = 'rain'
    elif a == 7:
        a = 'rainbow'
    elif a == 8:
        a = 'rime'
    elif a == 9:
        a = 'sandstorm'
    else:
        a = 'snow'

    # We return the probabilities for both classes
    return a


def index(request):
    if request.method == "POST":

        # upload = request.FILES['upload']
        uploaded_files = request.FILES.getlist('upload[]')
        results = []
        for uploaded_file in uploaded_files:
            # fss = FileSystemStorage()
            # file = fss.save(uploaded_file.name, uploaded_file)
            # file_url = fss.url(file)

            # prediction = makepredictions(os.path.join(media, file))
            prediction = makepredictions(uploaded_file)

            image_prediction = ImagePrediction(image=uploaded_file, predicted_class=prediction)
            image_prediction.save()

            results.append({'pred': prediction, 'file_url': '/media/' + str(uploaded_file)})
        return render(request, 'index.html', {'results': results})

    predictions = ImagePrediction.objects.all()  # Retrieve all predictions from the database
    return render(request, 'index.html', {'predictions': predictions})
    # return render(request, 'index.html')


def details(request, image):
    prediction = ImagePrediction.objects.get(image=image)
    return render(request, 'details.html', {'image': image, 'prediction': prediction})
