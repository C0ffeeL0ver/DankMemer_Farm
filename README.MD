# Dank Memer Farm (Send messages with post requests)

## Table of contents
* [General info](#general-info)
* [Setup](#setup)
* [Python Libraries](#python-libraries)

## General info
* This script sends requests with messages to a text channel on the discord 

## Setup
* Read a post request when a discord message is sent in the browser. Inspect element -> Network -> Send message -> Headers -> Get Authorization Value.
* Change the name of the ".txt" file to ".env"
* Setup the Authorization_Token and url in .env file
* In te first line add Authorization_Token = Value obtained
* On the second line of the same file, place url = https://discord.com/api/v8/channels/[YOUR_SECOND_ID]/messages (copy de second ID, wich is the ID from channel that you want to activate the script )
* Execute in promp: python main.py or  Execute start.bat in windows

## Python libraries
This project use the following modules:
* os
* requests
* dotenv(load_dotenv)
* time
* random
