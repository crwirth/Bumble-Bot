# Bumble-Bot

An automated swiping bot for Bumble

## Setup
This program has two dependencies:

1. Download chromedriver here:
    - http://chromedriver.chromium.org/
    - unzip, move to /usr/local/bin (mac os / linux)
2. pip3 install selenium

After you are finished installing the dependencies, then create a file called 'secrets.py' where you will store your username and password like this:

```python
 username = 'username'
 password = 'password'
```

## Using the program

Once you execute the program, you can use an interactive shell such as iPython to call `bot.autoSwipe()` and activate the auto swiping feature.

Enjoy, and have fun!
