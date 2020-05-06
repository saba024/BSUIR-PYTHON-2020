from django.urls import path
from . import views

urlpatterns = [
    path("", views.WinesView.as_view(), name="wine_list"),
    path("filter/", views.FilterWinesView.as_view(), name="filter"),
    path("search/", views.Search.as_view(), name="search"),
    path("add-rating/", views.AddStarRating.as_view(), name="add_rating"),
    path("<slug:slug>/", views.WineDetailView.as_view(), name="wine_detail"),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
    path("grape/<str:slug>/", views.GrapeView.as_view(), name="grape_sort_detail"),
]
