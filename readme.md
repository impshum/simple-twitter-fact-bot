# Simple Twitter Facts Bot

--------------------------------------------------------------------------------

- Make sure python is installed correctly -  <http://docs.python-guide.org>

- Clone this repo
~~~
git clone https://github.com/impshum/simple-twitter-facts-bot
~~~
Or use the download button (your choice).

- Move into the folder

  ```
  cd simple-twitter-facts-bot
  ```

- Build a virtual environment

  The scripts are in python 2.7 so...

  ```
  virtualenv -p /usr/bin/python2.7 venv
  ```

- Start said environment

  ```
  source venv/bin/activate
  ```

- Install requirements

  ```
  pip install twython requests bs4 lxml
  ```

- Create a twitter account for your project: <https://twitter.com>

- Create a twitter app for your project and grab your keys: <https://apps.twitter.com>

- Open up the files in an editor (I use <http://atom.io>)

- Have a spy around.

- Insert said keys into facts.py

- Open up facts.txt

The facts bot tweets a fact from facts.txt, moves the used line to liners.txt and sleeps for 15 mins then runs again until all lines have been used up. For sanity reasons there's a funtion which removes lines with more than 140 chars as Twatter only allows 140 chars.

To run the script

```
python bot.py
```

--------------------------------------------------------------------------------

woo.py is a very simple web scraper that grabs the top trending hashtag from <https://ritetag.com/hashtag-search> and simply prints it out. Beautiful Soup is fantastic!

Again, to run the script

```
python woo.py
```

--------------------------------------------------------------------------------

- To stop the environment

```
deactivate
```

--------------------------------------------------------------------------------

I'm sure you can get this running in no time. A raspberry pi comes in handy for running these 24/7.
