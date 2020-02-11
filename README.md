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

Credit to @aj-4 for his tutorial on how to build a Tinder swipe bot, which can be found here:
https://www.youtube.com/watch?v=lvFAuUcowT4&t=280s

## Using the program

Once you run the program from ther terminal, and are ready to use the autoswipe feature, call `bot.autoSwipe()` to activate the auto swiping feature.

Enjoy, and have fun!
