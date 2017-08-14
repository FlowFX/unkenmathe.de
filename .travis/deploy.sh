#!/bin/bash

cd ../
eval "$(ssh-agent -s)"
chmod 600 .travis/deploy_key
ssh-add .travis/deploy_key
git remote add pythonanywhere flowfx@ssh.pythonanywhere.com:/home/flowfx/bare-repos/unkenmathe.git
git push -f pythonanywhere master
python .travis/reload-webapp.py