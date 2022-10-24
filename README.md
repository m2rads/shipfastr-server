# Hermeias Route Optimizatier Server

## To install the dependency, clone the project and cd to src then run:

`pip3 install -r requirements.txt `

## To run the server run the following command inside the same directory:

`flask run`

## Note: The demo data is built inside demo_data.py

## Create Distance Matrix:

To create a distance matrix, you need to pass your addresses to
`create_distance_matrix()`

This method devides your array of addresses into a group of 16 and sends a request to 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial' to get the distance matrix.

For more infromation on this, please visit this page: 'http://en.wikipedia.org/wiki/Vehicle_routing_problem'
