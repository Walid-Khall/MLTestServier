# Servier ML test
In this test, we will develop three Deep Learning models (Model1, Model2 and Mdel3).

We will creat a Flask api.

Finally, we will package the application and create a Docker image for the Flask api.

The project will include a web app where you can input a smile and get classification results . 

## Project Components
The project composed of a main Package (servierpackage) including two subpackages.

    1. Flask Web App
    In a Python script, app.py, which is the web application.



    2. Models
    We find three models in this subpackage:

    In a Python script, Model1.py, which is a machine learning pipeline that:

    Loads data from the Dataset
    Splits the dataset into training and test sets
    Builds a  Deep Learning model
    Trains and tunes a model using Keras
    Outputs results on the test set
    Exports the final model as a h5 file

    In a Python script, Model2.py, which is a machine learning pipeline that:

    Loads data from the Dataset
    Splits the dataset into training and test sets
    Builds a text processing and build a Deep Learning model
    Trains and tunes a model using Keras
    Outputs results on the test set
    Exports the final model as a h5 file

    In a Python script, Model3.py, which is a machine learning pipeline that:

    Loads data from the Dataset
    Splits the dataset into training and test sets
    Builds a text processing and build a machine learning pipeline
    Trains and tunes a model 
    Outputs results on the test set
    Exports the final model as a pickle file

    3. Jupyter notebook with clean code for a general overview



## Instructions:

### Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.



1. There is two methods to run this app


   1.1. Run the main.py in the main package and and follow the instructions.


   1.2. Run the following commands in the project's root directory to set up your database and model.

    - To run model1 ML pipeline that trains classifier and saves
        `python models/model1.py data/dataset_single.csv models/model1.h5`

    - To run model2 ML pipeline that trains classifier and saves
        `python models/model2.py data/dataset_single.csv models/model2.h5`

    - To run model3 ML pipeline that trains classifier and saves
        `python models/model3.py data/dataset_multi.csv models/model3.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://127.0.0.1:3001/


#### Packaging
You can install this package by typing:
`py -m pip install --index-url https://test.pypi.org/simple/ --no-deps servier-package-walid-khall`

You can test that it was installed correctly by importing the package `>>import servierpackage`.

Make sure you’re still in your virtual environment, then run Python:  `py`

You can test that it was installed correctly by importing the package. Make sure you’re still in your virtual environment, then run Python:  `py`
=======
You can test that it was installed correctly by importing the package `>>import servierpackage`.
Make sure you’re still in your virtual environment, then run Python:  `py`

Import the package `>>from servierpackage import main`

Execute `>> main.main()` and follow the instructions.
