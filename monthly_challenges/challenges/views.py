from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


monthly_challenges = {
    "january": "Build a calculator that supports basic operations (+, -, *, /) and handles errors gracefully.",
    "february": "Create a to-do list CLI app that allows adding, editing, completing, and deleting tasks.",
    "march": "Build a simple text-based game (e.g., Hangman or Tic-Tac-Toe).",
    "april": "Scrape data from a public website and store it in a CSV file.",
    "may": "Create a personal expense tracker that stores data in a JSON or SQLite database.",
    "june": "Build a command-line weather app using an external API.",
    "july": "Create a basic chatbot that answers predefined questions using pattern matching.",
    "august": "Write a Python script to automate sending emails with attachments.",
    "september": "Build a unit converter (length, weight, temperature, etc.) with a GUI using Tkinter.",
    "october": "Implement a sorting algorithm visualizer using Matplotlib or Tkinter.",
    "november": "Build a file organizer script that sorts files into folders based on file extensions.",
    "december": "Create a Python Advent calendar that reveals a daily coding puzzle until Christmas."
}

# Create your views here.

def monthly_challenges_by_number(request,month):
    return HttpResponse(month) 



def monthly_challengess(request,month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
            return HttpResponseNotFound("This month is not supported!")
         
    


