# Rest Api Model

A little Python project that publishes, using Ngrok, an ML model trained with Tensorflow and serialized with Pickle.

The model predicts the chance of a certain customer buying a product, using Age and Salary as parameters, it was trained with an public dataset.

# Instalation and Execution

## Cloning the repository

    $ git clone https://github.com/Bsindra/rest_api_model

## Installing dependencies

    $ pip install -r requirements.txt

## Running the server

    $ python rest_client.py
    
> Note the "Forwarding" URL, we will need it in the next step.

## Using the API

    $ python rest_post.py URL age salary
 > Change URL for the previously copied Ngrok URL.
 > You can specify any **Int** value for _**Age**_ and _**Salary**_, but for better results keep these within the range of 18-60 for age, and 20,000-60,000 for salary.
