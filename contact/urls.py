from django.urls import path
from articles.views import blog_page
from contact.views import contact_page, home_page, about_page, work_page

urlpatterns = [
    path('', home_page, name='home-page'),
    path('about/', about_page, name='about-page'),
    path('blog/', blog_page, name='blog-page'),
    path('work/', work_page, name='work-page'),
    path('contact/', contact_page, name='contact'),
]
