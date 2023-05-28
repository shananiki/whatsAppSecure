# whatsAppSecure
Attempt to bring local encryption to WhatsApp!

-------------------

Table of contents
=================

<!--ts-->
   * [Preparation](#preparation)
      * [Chromium](#chromium)   
      * [Chrome Profiles](#chrome-profiles)   
      * [Python](#python-3104)   
      * [Required PIP packages](#required-pip-packages)
   * [Use cases](#use-cases)
     * [Example 1](#example-1)
<!--te-->


Preparation
===========
-----------

Chromium
--------
You can download chromium webdriver for your Google Chrome version by [here](https://chromedriver.chromium.org/).

Chrome Profiles
---------------
Make sure you have a profile, one is created by default. My profile name is shananiki.\
The path to the profile will most likely be "C:\Users\$USER\AppData\Local\Google\Chrome\User Data\Default" if it is your first profile.\
![](https://github.com/shananiki/whatsAppSecure/blob/main/gifs/chrome_profile.gif?raw=true)


Python 3.10.4
-------------
I used python 3.10.4, so I don't know if other versions are compatible. Download [here](https://www.python.org/downloads/release/python-3104/).

Required PIP packages
---------------------
You can either install it with pip manually or use the requirements.txt !
```bash
selenium==4.9.1
```
```bash
pip install -r requirements.txt
```

Use cases
=========
In the following I am showing examples on what you can do with this piece of "art".

Example 1
---------
This is basic message sending. And has nothing to do with securing the chat.\
Sending x amount of messages to a person by giving it's name. First we create an instance of WhatsAppSecure class.

The set functions work as following:\
**setTarget** - Sets the name of the target you want to send a message to. Make sure to pass the target is double quotes '"name"'\
**setMessage** - Sets the content of the message.\
**setMessageCounter** - Sets the amount of messages to be sent.
---
Other functions explained:\
**loadProfile** - Uses your profile and cookies of your real Google Chrome.\
**openWhatsApp** - Will navigate to https://web.whatsapp.com. \
**sendMessage** - Will send the message set before to the target person for the counter set.
```python
was = WhatsAppSecure()
was.loadProfile()
was.setTarget('"Phil Gassen Neu"')
was.setMessage("Bot Test")
was.setMessageCounter(2)
was.openWhatsApp()
was.sendMessage()
```
