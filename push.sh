#!/bin/sh

setup_git() {
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
}

commit_website_files() {
  git init
  git add .
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
}

upload_files() {
  git remote add origin https://${GH_TOKEN}@github.com/pbciat/pbciat.github.io.git
  git push -f origin master
}


###### git flow ######
setup_git

cd websocket-demo
> .nojekyll

# Compile client.js
curl -X POST -s --data-urlencode 'input@client.js' https://javascript-minifier.com/raw > client.min.js && rm client.js && mv client.min.js client.js

printf "server.py\nclientjs-design.png\n.DS_Store\n" > .gitignore
commit_website_files
upload_files

