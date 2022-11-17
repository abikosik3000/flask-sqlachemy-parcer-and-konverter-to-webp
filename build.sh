#!/bin/bash
app="abik"
docker build -t ${app} .
docker run -d -p 5000:5000 \
  -v $PWD:/app ${app}
#bash build.sh /