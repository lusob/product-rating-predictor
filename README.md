## Overview

Product rating prediction API
This flask application implements a REST API that willreturn the rating of a product based on its description text. 

You can use docker to try the project or install it locally in your workstation:

## Docker installation:

    $ docker build -t product_rating_predictor https://github.com/lusob/product_rating_predictor.git
    $ docker run -p 5000:5000 product_rating_predictor


## Locally installation

### To install it:

In the top-level directory:

    $ python3 -m venv env && source env/bin/activate
    $ pip install -r requirements.txt 

### To run it:

In the top-level directory:

    $ export FLASK_APP=main.py
    $ flask run

### To test it:

    $ curl  -u user1:pass1 --data "product_text='the tshirt is really confortable'"  http://localhost:5000/predict

    $ curl -u user1:pass1 --data "product_text='the tshirt is really not confortable'"  http://localhost:5000/predict

### To retrain the model

In the notebooks folder there is a notebook with the model generation, once retrained, the model will be saved in the data folder and it will be used by the API once you restarted the dev server (with flask run)

### Future improvements pending to do:

- Implement user management endpoints
- Improve authentification method using jwt or some other token-based method
- Using gunicorn instead of flask dev servere
- Test coverage (pytest) 
