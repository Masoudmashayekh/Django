from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm

# Create your views here.

def review(request):
    if request.method == "POST":
        from = ReviewForm(request.post)
        if entered_username == "" and len(entered_username) >= 100:
            return render(request, "reviews/review.html",{"has_error": True})
        print(entered_username)
        return HttpResponseRedirect("/thank-you")   
    form = ReviewForm()        
    return render(request,"reviews/review.html",{"form": form })
   

def thank_you(request):
    return render(request, "reviews/thank_you.html")