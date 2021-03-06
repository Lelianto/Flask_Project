#!/bin/bash

eval "$(ssh-agent -s)" &&
ssh-add -k ~/.ssh/id_rsa &&
cd ~/var/www/backend
git pull

source ~/.profile
echo "$DOCKERHUB_PASS" | docker login --username $DOCKERHUB_USER --password-stdin
docker stop portofolio
docker rm portofolio
docker rmi lelianto257/kutubuku:be
docker run -d --name portofolio -p 5000:5000 lelianto257/kutubuku:be