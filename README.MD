# Dank Memer Farm (Send messages with post requests)

## Table of contents
* [General info](#general-info)
* [Setup](#setup)
* [Python Libraries](#pytho-libraries)

## General info
* This script sends requests with messages to a text channel on the discord 

## Setup
* Read a post request when a discord message is sent in the browser. Inspect element -> Network -> Send message -> Headers -> Get Authorization Value.
* Create .env file whit Authorization_Token = Value obtained
* On the second line of the same file, place url = Your Current Url (you need to be in the text channel you want to activate the script )
* Execute in promp: python main.py

## Python libraries
This project use the following modules:
* os
* requests
* dotenv(load_dotenv)
* time
* random
