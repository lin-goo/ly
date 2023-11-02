from django.urls import path
from django.conf.urls import url

from students import views


app_name = "students"
urlpatterns = [
    url(r"(?P<pk>\d+)", views.StudentInfoView.as_view()),
    url(r"", views.StudentsView.as_view()),
]


