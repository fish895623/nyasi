#!/bin/bash
wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
apt-get update \
   && apt-get -y install --no-install-recommends google-chrome-stable
Version=$(google-chrome --version)
LATEST_RELEASE=${Version:14:2}
wget -O "/tmp/chrome_latest" "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_${LATEST_RELEASE}"

VER=$(cat "/tmp/chrome_latest")

wget -O "/tmp/chromedriver.zip" "https://chromedriver.storage.googleapis.com/${VER}/chromedriver_linux64.zip"
unzip "/tmp/chromedriver.zip" -d "/usr/bin"
