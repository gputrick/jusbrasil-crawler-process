# jusbrasil-crawler-process [![Build Status](https://www.travis-ci.org/gputrick/jusbrasil-crawler-process.svg?branch=master)](https://www.travis-ci.org/gputrick/jusbrasil-crawler-process)


##  Description

Crawler developed in django and react to crawler processes in TJAL.

## Usage [Dev]

To run in local environment to development you can use docker-compose simply by running in project dir:

``` shell
$ docker-compose up
```

## Production

The production build is available here: 

http://production.tnajnqmmpx.us-east-2.elasticbeanstalk.com/ 

## Structure [Dev]

Backend in django with python and postgres database, provides a REST Api to frontend maked in react using ant design.

## Structure [Prod]

The diferences in production environment are the database for tests is using sqlite3.

Uses nginx to host the back and front in the same port, making the proxy by the prefix 'api/' to backend and root redirect to frontend.

 Front is builded and hosted by serve -s build.