from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


monthly_challenges = {
    "January": "Build a calculator that supports basic operations (+, -, *, /) and handles errors gracefully.",
    "February": "Create a to-do list CLI app that allows adding, editing, completing, and deleting tasks.",
    "March": "Build a simple text-based game (e.g., Hangman or Tic-Tac-Toe).",
    "April": "Scrape data from a public website and store it in a CSV file.",
    "May": "Create a personal expense tracker that stores data in a JSON or SQLite database.",
    "June": "Build a command-line weather app using an external API.",
    "July": "Create a basic chatbot that answers predefined questions using pattern matching.",
    "August": "Write a Python script to automate sending emails with attachments.",
    "September": "Build a unit converter (length, weight, temperature, etc.) with a GUI using Tkinter.",
    "October": "Implement a sorting algorithm visualizer using Matplotlib or Tkinter.",
    "November": "Build a file organizer script that sorts files into folders based on file extensions.",
    "December": "Create a Python Advent calendar that reveals a daily coding puzzle until Christmas."
}

# Create your views here.

def monthly_challenges_by_number(request,month):
    return HttpResponse(month) 



def monthly_challenges(request,month):
    challenge_text = None
    if month == "january":
        challenge_text = "1th Month"
    elif month == "february":
        challenge_text = "2th Month"
    elif month == "match":
        challenge_text = "3th Month"
    else:
        return HttpResponseNotFound("This month is not supported!")
        
    return HttpResponse(challenge_text)


