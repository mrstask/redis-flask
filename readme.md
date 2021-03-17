###This is a template of the application that contain Flask app binded to a Redis database.
Everything is running using Dockerfile for Flask coupled with Redis in docker-compose file.

To debug using Pycharm you need to create new project interpretator that runs on docker-compose file
in Debug configuration you need to select Flask app configurator, and inside you need to select your interpreter as an interpreter
Also you need to add **additional options** _--host 0.0.0.0_ and **Docker-compose command** and option is set to _up -- build_