idfancy :sweat_drops:
=======
Simple python script to generate a random German name from a gameid.  
Example: `GthM7pA3` would result in `das visuelle Allergen`, pretty funny, huh?

Usage :pray:
-----
- Install [python 3.7+](https://www.python.org/downloads/release/python-370/) and set up the environment variables accordingly. Otherwise you won't be able to use the `python` command.
- Download the sources of this repository and place them wherever you want.  
- Open the command line and execute `python script.py yourId`. `yourId` can be replaced with any id of pattern `(http://)?game.rewinside.tv/([a-zA-Z0-9]{8})`.
- Enjoy the result!

You can pass as many ids as you want. Simply add them to the script arguments (`yourId1 yourId2 yourId3`).

REST Server :joy:
-----------
If you want to setup your own RESTful server with this little application, you have to fetch the docker image first.
Either use:
```
docker pull superioz/idfancy
```
Or inside the main project directory:
```
docker build -t superioz/idfancy .
```

After the image has been successfully installed you can use:
```
docker run --name idfancy -p 1337:1337 superioz/idfancy
```
to start the docker container. Now `localhost:1337/ping` should give a response.

Protocol :swimmer:
--------
**Content-Type**: `application/json`

**POST** Request Body:
```json
[
  "oRRUcuvc",
  "UTlsBvC6",
  "7mbRvBOY"
]
```

**Response**:
```json
{
    "data": {
        "7mbRvBOY": "der vorsintflutliche Verdauungstrakt",
        "UTlsBvC6": "die kastenförmige Tierhaltung",
        "oRRUcuvc": "die abkömmliche Rauferei"
    },
    "status": "ok"
}
```

The respective **curl** command would be:
```
curl -X POST -H "Content-Type: application/json" -d ["oRRUcuvc","UTlsBvC6","7mbRvBOY"] localhost:1337
```

