# Flask-Geo_Distance
a flask api to calculate distance between two points, and if the coordinates are inside a certain range.

How to use: 

- clone this repo, go to project directory with terminal, type python app.py
- go to your browser and test it by entring localhost:5000/, you should be able to see a reply if its succesfull

To use get-distance endpoint use postman or python requests module.

The expected request input: 

url = 'http://localhost:5000/get-distance'
data = {'location':[41.024877037266341,29.01338920833063]}

Expected output: 

{'Distance': distance in km}


Notes: 
- used yandex geocoder to find a default comparison point(coordinates).
- used Haversine formula, which calculates the great-circle distance between two points.
- used marshamallow module schemas for requests input data type control.
- used flask blueprints for the get distance service.
- you can modify the default coordinate, its in app.py document.
- you can also modify the default area range to check if a given coordinate is inside an area coordinates range.
