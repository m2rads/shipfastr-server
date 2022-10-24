# Hermeias Route Optimizatier Server

## To install the dependency, clone the project and cd to src then run:

`pip3 install -r requirements.txt `

## To run the development server run the following command inside the same directory:

`flask run`

## To run the server using Gunicorn option, run the following command:

`gunicorn --bind :$PORT --workers 1 --threads 8 app:app`

## Note: The demo data is built inside demo_data.py

## Create Distance Matrix:

To create a distance matrix, you need to pass your addresses to
`create_distance_matrix()`

This method devides your array of addresses into a group of 16 and sends a request to 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial' to get the distance matrix.

For more infromation on this, please visit this page: 'http://en.wikipedia.org/wiki/Vehicle_routing_problem'

## Caution: that you need to provide your Google API key as the first index of your Address array in order to get the distance matrces

## Route optimzer creates the response in a json format.
