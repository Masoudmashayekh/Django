from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm
from django.views import View

# Create your views here.

class ReviewView(View):
    def get(self, request):
        form = ReviewForm()         
        return render(request,"reviews/review.html",{"form": form })
    
    
    def post(self,request):
        form = ReviewForm(request.POST)
        if form.is_valid():    
            form.save()
            return HttpResponseRedirect("/thank-you") 
        return render(request,"reviews/review.html",{"form": form })
        
   
class ThankYouView(View):
    def get(self, request):
        return render(request, "reviews/thank_you.html")