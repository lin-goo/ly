from django.conf.urls import url

from records import views


app_name = "records"
urlpatterns = [
    url(r"(?P<pk>\d+)", views.RecordInfoView.as_view()),
    url(r"", views.RecordsView.as_view()),
]


