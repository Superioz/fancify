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
If you want to setup your own RESTful server with this little application:
- Execute `docker build -t idfancy .` in the main directory of this project.
  - or use `docker pull superioz/idfancy` :stuck_out_tongue_winking_eye:
- Execute `docker run --name idfancy -p 1337:1337 idfancy` and enjoy!
