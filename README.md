# Movie Library Python Mini-Project

Welcome to the code documentation for this mini-project. This is forked from [Udacity's ud036_StarterCode project](https://github.com/udacity/ud036_StarterCode). This is a python project so there are a few pre-requisites in order to run this project.

## Prerequistes

* Install python in your current Operating System. I am using [2.7.11](https://www.python.org/) .

## Project structure

* fresh_tomatoes.py (Is the python code from the main project that generates the webpage to display   our movies) <br/>

* video.py (is the main python class to be used to play videos.)<br/>
    | - media.py (is the python file that contains the class called Movies that holds information       about movies) extends Video class<br/>
    | - series.py (was supposed to be the python file that contains the class Series that would         hold information about Tv-series) extends Video class<br/>

* entertainment_center.py (The python file that contains the main execution code using the          fresh_tomatoes.py and media.py files)<br/>

## How to run?

* Clone or download this project to a location on your computer of your choosing

* Open your command line / Terminal and navigate to that folder

* In order to run this code from the command line you will have to enter the following command 
   ```
    python entertainment_center.py
   ```

* Once you run the above command It will generate a HTML page and then open that page in a browser.   which you can interact with. This generated HTML file is present inside the same folder of the      project. 
