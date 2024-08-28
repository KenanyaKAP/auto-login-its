Tested and works in 
- <b>Ubuntu 18.04.5 LTS & Windows 11</b>
- <b>Python 3.8.10 | Pip 20.0.2</b>
- <b>Selenium 4.24.0</b>
- <b>Chrome version 105</b>

# For Ubuntu
## Install Selenium
Make sure you have python installed in your ubuntu server
```sh
pip install selenium
```

## Install Chrome
Install chrome
```sh
sudo dpkg -i google-chrome-stable_105.0.5195.102-1_amd64.deb
```

Check version
```sh
google-chrome --version
```

## Install Chrome driver
Unzip
```sh
unzip chromedriver_linux64.zip
```

Move to bin and give access
```sh
sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver
```

## Test chrome driver
Make sure its working
```sh
chromedriver --url-base=/wd/hub
```

# How to use
## Put Your Credential
Put your credential in `main.py`
```python
# Enter below your login credentials
username = "50xxxxxxxx"
password = "password"
```

## Run the program
For ubuntu
```sh
python3 main.py
```
For windows
```sh
python main.py
```