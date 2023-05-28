# whatsAppSecure
Attempt to bring local encryption to WhatsApp!

-------------------

Table of contents
=================

<!--ts-->
   * [Preparation](#Preparation)
      * [Chromium](#chromium)   
      * [Python](#python-3.10.4)   
      * [Required PIP packages](#Required-PIP-packages)
      * [Required packages on Linux](#Required-packages-on-Linux)
   * [Documentation](#Documentation)
      * [LMouse](#LMouse)
      * [Core](#Core)
      * [Tab](#Tab)
      * [FastLogin](#FastLogin)
<!--te-->


Preparation
===========
------------------------




Python 3.10.4
-------------


Chromium
--------
You can download chromium webdriver for your Google Chrome version by [here](https://chromedriver.chromium.org/).

------------------

------------------
### PIP Requirements 

```bash
pip install selenium
```
or
```bash
pip install -r requirements.txt
```

-------------------

To load your default profile (including cookies) you can use the following function
```python
ChromeOptions options = new ChromeOptions();
options.addArguments("user-data-dir=/path/to/your/custom/profile");
```