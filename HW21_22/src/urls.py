from django.contrib import admin
from django.template.context_processors import static
from django.urls import path, include

from my_app.views import index, hello_user
import cw20
from cw20.views import user_details
import cw21
from cw21.views import home_page
from hw21.views import hw21_home_page, add_person
from src import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('hello_user/', hello_user, name='hello_user'),
    path('cw21/home_page/', home_page, name='home_page'),
    path('user_details/', user_details, name = 'user_details'),
    path('hw21_home_page/', hw21_home_page, name='hw21_home_page'),
    path('add_person/', add_person, name ='add_person'),
]
