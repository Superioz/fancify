idfancy :sweat_drops:
=======
Simple python script to generate a random German name from a gameid.  
Example: `GthM7pA3` would result in `das visuelle Allergen`, pretty funny, huh?

Current size of adjectives: **5560**  
Current size of nouns: **48994**

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

We have a simple UI at `localhost:1337` for user input as well:
![UI](/.github/images/web_ui.png "UI")

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

Keep in mind that the maximum of requests are 1000 **per hour** and 24000 **per day**.

Java Example :coffee:
------------
You could use the command line for requests forevery, but using a program might be easier.
Here is an example for **Java** users:
``` JAVA
try {
  String gameId = "Xhg1bgsb";

  URL urlObject = new URL("http://idfancy.freggy.de/");
  HttpURLConnection con = (HttpURLConnection) urlObject.openConnection();

  // set request type to POST
  con.setRequestMethod("POST");

  // other user-agents might not work .. therefore: custom
  con.setRequestProperty("User-Agent", "dank");

  // set the content type to json, as we want to pass a json string
  con.setRequestProperty("Content-Type", "application/json");

  // Write into the output-stream of the connection
  con.setDoOutput(true);
  DataOutputStream output = new DataOutputStream(con.getOutputStream());
  output.write(("[\"" + gameId + "\"]").getBytes());
  output.flush();
  output.close();

  BufferedReader input = new BufferedReader(new InputStreamReader(con.getInputStream()));
  String inputLine;
  StringBuilder response = new StringBuilder();
  while ((inputLine = input.readLine()) != null) {
    response.append(inputLine);
  }
  input.close();

  // result of the request
  // prints: {"data":{"Xhg1bgsb":"die dreitürige Berechnung"},"status":"ok"}
  System.out.println(response.toString());
} catch (IOException ex) {
  // something went wrong, either a 400+ error or some
  // other connection issue
  ex.printStackTrace();
}
```
As sending POST requests in other languages like **Go** or **Python** is much easier, I'm not gonna give an example for them.

Contribution :raised_hands:
------------
Feel free to create **pull requests** or **issues**.  
Doesn't matter if you just want to add new nouns/adjectives or if you have found a bug.  
