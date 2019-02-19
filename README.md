
[![Maintainability](https://api.codeclimate.com/v1/badges/fa520a535e5047282886/maintainability)](https://codeclimate.com/github/jackiegitari1234/Questioner_v2/maintainability) [![Build Status](https://travis-ci.org/jackiegitari1234/homestudy.svg?branch=master)](https://travis-ci.org/jackiegitari1234/homestudy) [![Coverage Status](https://coveralls.io/repos/github/jackiegitari1234/homestudy/badge.svg?branch=master)](https://coveralls.io/github/jackiegitari1234/homestudy?branch=master)

# Questioner : challenge 3

## Endpoints
Required Method       | EndPoint       | Goal |
------------- | ------------- | ---------------
POST  | /api/v1/meetups  | Post a new meetup record   |
GET  | /api/v1/meetups/<int:meetup_id>  | Get a specific meetup   |
GET  | /api/v1/meetups/upcoming   | Get all upcoming meetup records   |
POST  | /api/v1/meetup/<int:meetup_id>/question | Create a question for a specific meetup.   |
PUT | /api/v1/questions/<int:question_id>/upvote | Adds votes by one |
PUT | /api/v1/questions/<int:question_id>/downvote | Decreases votes by one  |
POST | /api/v1/meetups/<int:meetup_id>/rsvps | Create a meetup RSVP
POST | /api/v1/signup | Creates an account|
POST | /api/v1/signin | Logs in a user|


## Project Overview
This is a project that is used by orgarnizers of various meetups to plan on which questions to be answered during the meetups. The information is collected from users of the Questioner. The users can register, login and upvote or downvote a question so that the total number of upvotes and downvotes can be collected and decisions are made.

## Getting Started
- To test the API on your local machine,
- Start by cloning the Repository $ git clone https://github.com/jackiegitari1234/Questioner
- run the commands
    • `cd Questioner/API` to navigate to the root folder
    • `pip3 install -r requirements.txt` to install all the requirements
    • `source venv/bin/activate` to create a virtual environment
    • `export FLASK_ENV=development` to setup the environment
    • `flask run` to launch the API
- Test the api using postman

## Running the tests
- run the commands
• `pip install pytest` to install pytest testing tool
• `pytest` to run the automated tests


### Prerequisites
- python 3.6 
- pip installed - python package manager
- Postman - for testing the end points
- Git - for version control


## This API includes
- Flask
- Git Version Control
- Pytest

## Acknowledgments
- slack nbo-36
- nbo-36 team 3 members


## Author
Jackline Gitari
