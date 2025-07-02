from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import ReviewForm
from django.views import View
from django.views.generic.base import TemplateView
from .models import Review
from django.views.generic import ListView, DetailView
# from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
# Create your views here.

class ReviewView(CreateView):
    # form_class = ReviewForm
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html" 
    success_url = "/thank-you"  
    
    # def form_valid(self, form):
    #     form.save()
    #     return super().form_valid(form)
    
     
    # def get(self, request):
    #     form = ReviewForm()         
    #     return render(request,"reviews/review.html",{"form": form })
    
    
    # def post(self,request):
    #     form = ReviewForm(request.POST)
    #     if form.is_valid():    
    #         form.save()
    #         return HttpResponseRedirect("/thank-you") 
    #     return render(request,"reviews/review.html",{"form": form })
        
   
class ThankYouView(TemplateView):
        template_name = "reviews/thank_you.html"
        
        
        def get_context_data(self, **kwargs):
             context= super().get_context_data(**kwargs)
             context["message"] = "This works!"
             return context # if we have message in thank_you html file we can add it here with get_context_data
         
         
class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"
    
    # def get_queryset(self):
    #      base_query = super().get_queryset()
    #      data = base_query.filter(rating__gt= 3)
    #      return data
    
class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    model = Review
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     review_id = kwargs["id"]
    #     selected_review = Review.objects.get(pk=review_id)
    #     context["review"] = selected_review
    #     return context  
    def get_context_data(self, **kwargs):
         context =  super().get_context_data(**kwargs) 
         loaded_review = self.object  
         request = self.request
         favorite_id = request.session["favorite_review"]
         context["is_favorite"] = favorite_id == str(loaded_review.id)
         return context
        
            
class AddFavoriteView(View):
    def post(self,request):
        review_id = request.POST["review_id"]
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id)
        