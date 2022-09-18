# AI-Image-Attractiveness

This project tests the controversial hypothesis of whether AI generated images are, on average, more interesting to look at over human created art, in light of the recent incidents surrounding the use of AI generated art in art competitions and winning. The basic function of this application is to use eye tracking to determine which image is more interesting to the user when presented with two images side by side, one created by a human, and another using AI. At the end of the experiment, hopefully the results will tell us which is more interesting. We apologize in advance to any art majors out there.

This application will use opencv for the video feed and dlib for facial and eye detection. The eye detector will only target the right eye because we're assuming your pupils can't point in different directions. If your eyes can do this, don't do it. In order to determine the direction, we will be taking the feed of the eye, converting it to grayscale, then applying a binary threshold to convert it all to black and white pixels. We will then create two separate feeds with varied bounds for looking left and right and count the black pixels present (pupil) to determine a direction.

## Post hackathon notes

Given that we had 24 hours to create something functional and presentable, we had to introduce some compromises. Out initial ideas for webscraping images didn't exactly work out due to issues with dependencies and python not wanting to cooperate. As well, our plans to host the app on a website also didn't work out since none of us had any extensive experience in web design and react. However, we were able to create a functioning client gui with some preloaded images that would be sufficient for a short demo and presentation. Despite this, our main goal remains the same, to determine whether or not AI has the capability of art compared to humans. This idea will be put to the test in the demo, and in the future if we decide to get the webscraping functionality down.

# Dependencies
pip3 install virtualenv<br>
virtualenv env<br>
source env/bin/activate<br>
pip3 install opencv-python <br>
pip3 install flask<br>
pip3 install flask-wtf<br>
pip3 install jyserver<br>

## installing dlib
Linux: <br>
sudo apt install cmake<br>
pip3 install cmake<br>
pip3 install dlib<br>

windows: <br>
install cmake from the web<br>
pip3 install cmake<br>
pip3 install dlib<br>

macOS:
I dont know how to use macOS so somebody help

# other stuff to install:

## commands in terminal:
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
pip install torch
pip install transformers
pip install diffusers
pip install lxml
pip install bs4
pip install requests
