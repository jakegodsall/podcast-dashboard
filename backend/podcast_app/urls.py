from django.urls import path

from .views import  LanguageList, LanguageDetail, AuthorList, AuthorDetail, PodcastList, PodcastDetail


urlpatterns = [
    path('language/', LanguageList.as_view()),
    path('language/<int:pk>', LanguageDetail.as_view()),
    path('author/', AuthorList.as_view()),
    path('author/<int:pk>', AuthorDetail.as_view()),
    path('podcast/', PodcastList.as_view()),
    path('podcast/<int:pk>', PodcastDetail.as_view())
]
    