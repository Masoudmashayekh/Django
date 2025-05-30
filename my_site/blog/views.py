from datetime import date
from django.shortcuts import render


all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Masoud",
        "date": date(2023,7,1),
        "title": "Mountain Hiking",
        "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Masoud",
        "date": date(2018, 7, 21),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Masoud",
        "date": date(2022, 7, 21),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.  

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis aperiam est praesentium, quos iste consequuntur omnis exercitationem quam velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
    "slug": "first-django-project",
    "image": "First.jpeg",
    "author": "Masoud",
    "date": date(2020, 7, 21),
    "title": "My First Django Web App",
    "excerpt": "Building my first Django project was both challenging and rewarding. I learned how powerful and structured backend development can be.",
    "content": """
      I started by learning how Django handles URLs, views, and models. After that, I connected my app to a SQLite database and created basic CRUD operations.

      One key part of this experience was implementing Django templates to display dynamic content. I also applied HTML and CSS to design a simple user interface.

      Overall, it gave me a solid foundation in how web apps work behind the scenes and boosted my confidence in backend development.
    """
},
{
    "slug": "learning-html-css",
    "image": "css_html.png",
    "author": "Masoud",
    "date": date(2019,7,1),
    "title": "Styling with HTML & CSS",
    "excerpt": "Before diving into Python and Django, I spent time learning the basics of the web: HTML and CSS.",
    "content": """
      I practiced building static web pages from scratch using semantic HTML and modern CSS layout techniques like Flexbox and Grid.

      Styling web pages taught me the importance of clean structure and visual hierarchy. I explored responsive design to make pages look great on any screen size.

      This experience made me appreciate front-end development and how it connects with the backend to create complete user experiences.
    """
},
{
    "slug": "building-blog-django",
    "image": " Blog_App_.png",
    "author": "Masoud",
    "date": date(2022,3,21),
    "title": "Creating a Blog App with Django",
    "excerpt": "I built a blog app where users can read posts, and as an admin, I could create, update, and delete them. It was a big leap in understanding full-stack logic.",
    "content": """
      The project involved designing models for blog posts, writing views to handle logic, and creating templates for display.

      I used Django's built-in admin panel for content management, and added basic styling with HTML and CSS for a clean look.

      This hands-on experience helped me understand how to build functional, maintainable web applications from the ground up.
    """
}

]

def get_date(post):
    return post["date"]

# Create your views here.

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date, reverse=True)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html",{"posts": latest_posts})

def posts(request):
    return render(request, "blog/all-posts.html",{"all_posts": all_posts})
   

def post_detail(request,slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request,"blog/post-detail.html",{"post": identified_post} )
