#!/bin/bash
apt-get update
apt-get install -y --no-install-recommends wget unzip curl gnupg2
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list
apt-get update 
apt-get install -y --no-install-recommends google-chrome-stable

VERSION=$(google-chrome --version)
echo "${VERSION:14:2}"
VERSION=$(curl -L "http://chromedriver.storage.googleapis.com/LATEST_RELEASE_${VERSION:14:2}")
wget -P /tmp http://chromedriver.storage.googleapis.com/$VERSION/chromedriver_linux64.zip
unzip /tmp/chromedriver_linux64.zip -d /usr/bin