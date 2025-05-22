from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenges_dic = {
    "january": "1. Build a calculator that supports basic operations (+, -, *, /) and handles errors gracefully.",
    "february": "2. Create a to-do list CLI app that allows adding, editing, completing, and deleting tasks.",
    "march": "3. Build a simple text-based game (e.g., Hangman or Tic-Tac-Toe).",
    "april": "4. Scrape data from a public website and store it in a CSV file.",
    "may": "5. Create a personal expense tracker that stores data in a JSON or SQLite database.",
    "june": "6. Build a command-line weather app using an external API.",
    "july": "7. Create a basic chatbot that answers predefined questions using pattern matching.",
    "august": "8. Write a Python script to automate sending emails with attachments.",
    "september": "9. Build a unit converter (length, weight, temperature, etc.) with a GUI using Tkinter.",
    "october": "10. Implement a sorting algorithm visualizer using Matplotlib or Tkinter.",
    "november": "11. Build a file organizer script that sorts files into folders based on file extensions.",
    "december": "12. Create a Python Advent calendar that reveals a daily coding puzzle until Christmas."
}

# Create your views here.


def index(requerst):
    list_items = ""
    months = list(monthly_challenges_dic.keys())
    for month in months:
        capitalized_month = month.capitalize()
        month_path = reverse("monthly_challenges_by_me", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenges_by_number(request, month):
    months = list(monthly_challenges_dic.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    else:
        redirect_month = months[month - 1]
        redirect_path = reverse("monthly_challenges_by_me", args=[
                                redirect_month])  # challenges/january
        return HttpResponseRedirect(redirect_path)


def monthly_challenges_by_text(request, month):
    try:
        challenge_text = monthly_challenges_dic[month]
        return render(request, "challenges/challenge.html",{
            "text": challenge_text,
            "month_name": month.capitalize()
            })
    
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
 