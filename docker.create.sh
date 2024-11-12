#!/bin/bash


# create docker
docker build ./sphinxDocker/ -t sphinxdoc/sphinx:v3

# install web server
npm install http-server -g
