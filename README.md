# 1️⃣ WebSearch Project
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg) 
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![HitCount](http://hits.dwyl.com/{username}/{project-name}.svg)](https://github.com/Shivansh-007/TWT-Code-Jam)
[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

:star: Star us on GitHub — it helps!

Hi! For TWT's August Code-Jam we were tasked to create a "generator" themed project. Our team, [Sachin](https://github.com/Shivansh-007) , [FunkyMonkey](https://github.com/Roshannarma), [NMarco](https://github.com/marco-create), [wowzers](https://github.com/tshe777), decided to create a website generator. 
Our project will ask the user for an input and then return a website on it with a definition, some fun facts on it, Youtube videos, news articles and relevant images. Have Fun!

##  Contributors


|                                       [Shivansh](https://github.com/Shivansh-007)                                       |                                       [FunkyMonkey](https://github.com/Roshannarma)                                        |                                       [NMarco](https://github.com/marco-create)                                        |                                       [wowzers](https://github.com/tshe777)                                        |
| :-----------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------------------------------------------: | 
|                      [<img src="https://www.dalesjewelers.com/wp-content/uploads/2018/10/placeholder-silhouette-male.png" width = "200" />](https://github.com/Shivansh-007)                       |                      [<img src="https://www.dalesjewelers.com/wp-content/uploads/2018/10/placeholder-silhouette-male.png" width = "200" />](https://github.com/Roshannarma)                         |                      [<img src="https://www.dalesjewelers.com/wp-content/uploads/2018/10/placeholder-silhouette-male.png" width = "200" />](https://github.com/marco-create)                      |                      [<img src="https://www.dalesjewelers.com/wp-content/uploads/2018/10/placeholder-silhouette-male.png" width = "200" />](https://github.com/tshe777)                     |                      [<img src="https://www.dalesjewelers.com/wp-content/uploads/2018/10/placeholder-silhouette-male.png" width = "200" />](https://github.com/Shivansh-007)                        |
|                 [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/Shivansh-007)               |            [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/Roshannarma)              |           [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/marco-create)           |          [<img src="https://github.com/favicon.ico" width="15"> ](https://github.com/tshe777)         |
| [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/) | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/) | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/in/marco-ninghetto-a0b983142/) | [ <img src="https://static.licdn.com/sc/h/al2o9zrvru7aqj8e1x2rzsrca" width="15"> ](https://www.linkedin.com/) |


## Table of Contents

- [Installation](#installation)
- [Usage](#Usage)
- [Setting Up APIs](#Setting-Up-APIs)
- [Examples](#Exampl.es)
    - [Search Page](#Search-Page)
    - [Result](#Results-Page)
    - [Screen Recording](#iScreenRecording)
- [License](#License)
- [Links](#Links-And-Resourcse)

## Installation

### Clone

- Clone this repo to your local machine using `https://github.com/Shivansh-007/TWT-Code-Jam`


**Linux**
```shell
$ sudo apt-get install python3.8-venv
$ python3.8 -m venv venv
```
Move all the files from the cloned folder to this virtual venv

```shell
$ git clone https://github.com/Shivansh-007/WebSearch.git
$ cd WebSearch
$ pip install -r requirements.txt
$ . bin/activate
$ export FLASK_ENV=development
$ export FLASK_APP=server.py
$ flask run
```

**Windows**

!! open PowerShell as ***Administrator***
```PowerShell
> git clone https://github.com/Shivansh-007/WebSearch.git
> cd \cloned\repository
> Set-ExecutionPolicy Unrestricted -Force
> py -m pip install -r requirements.txt
> py -m pip install --upgrade pip
> py -m pip install --user virtualenv
```
Following commands always inside the cloned repository folder
```PowerShell
> py -m venv env
> .\env\Scripts\activate
```
Run the app
```PowerShellv
> $env:FLASK_APP = "server.py"
> flask run
```


## Usage

Once everything is set, the command line should run like the following (example for Windows)

![Picture](https://user-images.githubusercontent.com/53913990/91655073-5fc24e00-eaae-11ea-856a-05158fb4178a.png)

Just copy the url and paste it into browser and go!

## Setting Up APIs for YouTube ([check how to do it](https://www.youtube.com/watch?v=th5_9woFJmk&t=185s)) :information_desk_person:

<details open>
<summary>Setting up the YouTube APIs!!</summary>
<br>

- Go to https://developers.google.com/ and log in or create an account, if necessary.
- After logging in go to this link https://console.developers.google.com/project and click on the blue CREATE PROJECT button as depicted in the photo below. Wait a moment as google prepares your project.

![Picture](http://www.slickremix.com/wp-content/uploads/2015/04/Screen-Shot-2016-08-06-at-4.12.36-PM.png)
- Fill in whatever Project Name you want.

![Picture](http://www.slickremix.com/wp-content/uploads/2015/04/Screen-Shot-2016-08-06-at-4.14.40-PM.png)
- Then click GoogleAPIs link in the top left corner and then click the link option called “YouTube Data API v3” It’s under YouTube API’s. You can see it below:

![Picture](https://plugins360.com/wp-content/uploads/2018/11/youtube-data-api-v3-box.png)
- Now click on the “ENABLE” button.
- Next click on the blue ‘Go to Credentials’ button to the right.

![Picture](http://www.slickremix.com/wp-content/uploads/2015/04/Screen-Shot-2016-08-06-at-4.17.34-PM.png)
- Choose the select option YouTube Data API v3 for the first select option and Web server(e.g. node js. Tomcat) for the second selection. Then choose Public data. Now click the blue button, “What credentials do I need?.”

![Picture](http://www.slickremix.com/wp-content/uploads/2015/04/Screen-Shot-2016-08-06-at-4.21.07-PM.png)
- Almost done, wait for google to create your new project and you should see the screen below where you can copy your API Key.

![Picture](http://www.slickremix.com/wp-content/uploads/2015/04/Screen-Shot-2016-08-06-at-4.21.38-PM.png)
- **Copy the API Key (it will be requested by the terminal)**

</details>

## Examples

### Search Page

Enter the topic you'd like to look for and press ENTER

![Picture](https://user-images.githubusercontent.com/53913990/91727640-44386f80-eba2-11ea-80e5-2cf0cb5e0fc0.png)

### Results Page

![Picture](https://user-images.githubusercontent.com/53913990/91800027-8efcca80-ec28-11ea-97aa-490ba8087a68.png)

![Picture](https://user-images.githubusercontent.com/53913990/91800214-e13deb80-ec28-11ea-9730-9259c812c6d8.png)

### Of course, sometimes something can go wrong

404 error page

![Picture](https://user-images.githubusercontent.com/53913990/91727915-a85b3380-eba2-11ea-9bde-27c43261ae93.png)

### ScreenRecording

To be Done

## License

MIT License

Copyright (c) 2020 Sachin

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


## Links And Resourcse

- [Dictionary API](https://dictionaryapi.com/)  
- [Wikipedia Library](https://pypi.org/project/wikipedia/)  
- [Wikipedia API](https://pypi.org/project/Wikipedia-API/)  
- [How to install Youtube API - easy](https://www.youtube.com/watch?v=th5_9woFJmk&t=185s)  
- [Google News API](https://pypi.org/project/GoogleNews/)
- [Older Repo Of This Project 1](https://github.com/Shivansh-007/TWT-Code-Jam/graphs/contributors)
- [Older Repo Of This Project 2](https://github.com/Roshannarma/code_jam/graphs/contributors)
