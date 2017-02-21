# Aeroplane-Management-System-API
Django REST Framework Best Practices

## DJANGO REST Framework
The connection to the AMS_DB mySQL database is implemented using the `DJANGO REST Framework`.

## Models
The Python objects that map the database can be found here:

[models.py](https://github.com/DonatoCappiello/Aeroplane-Management-System-API/blob/master/AeroplaneManagementSystemAPI/FlyingClub/models.py)

All models implements the __str__ function for dispaly and debug purposes.

The class decorator `@python_2_unicode_compatible` is used to ensure compatibility with older versions of Python.

Please notice that this application has been developed to demonstrate the DJANGO REST Framework used in more complex models show at my interview.

The relationship between tables has not been implemented as not necessary at this point in time.

Data relationship can easily been implemented as follow:

TABLE -> Flights 
Field -> member_no = models.ForeignKey(Members, on_delete=models.CASCADE)

## ADMIN interface

To facilitate data entry and debugging all tables have been registered with the DJANGO Admin interface.
[admin.py](https://github.com/DonatoCappiello/Aeroplane-Management-System-API/blob/master/AeroplaneManagementSystemAPI/FlyingClub/admin.py)

Data can now be edited using the DJango admin interface:

username: dcappiello
password: Sigmatic241!

## Expose DATA to the world: SERIALIZER

Serializers convert data a JSON format that the Angular 2 front end can understand.

[serializers.py](https://github.com/DonatoCappiello/Aeroplane-Management-System-API/blob/master/AeroplaneManagementSystemAPI/flyingclub/serializers.py)

## Expose DATA to the world: API views

Serve DATA to the front end

[api.py](https://github.com/DonatoCappiello/Aeroplane-Management-System-API/blob/master/AeroplaneManagementSystemAPI/flyingclub/serializers.py)

We are not performing sofisticated query here, just using an API view to retrieve all Aeroplanes and serialize them  into a JSON object.

please note that the ModelViewSet of the DJango Framework has all the functionalities to perform CRUD operations and run sophisticated queries.

## Expose DATA to the world: create URLs

URLs tells DJANGO where to serve the data.

[urls.py](https://github.com/DonatoCappiello/Aeroplane-Management-System-API/blob/master/AeroplaneManagementSystemAPI/flyingclub/urls.py)

## Results

To run the server use the command `python manage.py runserver`.

The Aeroplane data cna now be retrieved by the front end at the following address `http://127.0.0.1:8000/ams/aeroplanes` using the GET method.

![Postman Screenshot](https://github.com/DonatoCappiello/Aeroplane-Management-System-API/Postman.png)
