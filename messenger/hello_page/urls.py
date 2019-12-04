from hello_page.views import hello_page
from django.urls import path

urlpatterns = [
        path('', hello_page, name='hello_page'),
]
