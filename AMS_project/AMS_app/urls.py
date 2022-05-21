from django.urls import path
from AMS_app import views

urlpatterns = [
    path('apartment-list/', views.ApartmentList.as_view()),
    path('apartment/<int:pk>/', views.ApartmentDetail.as_view()),

    path('building-list/', views.BuildingList.as_view()),
    path('building/<int:pk>/', views.BuildingDetail.as_view()),

    path('apartmentType-list/', views.ApartmentTypeList.as_view()),
    path('apartmentType/<int:pk>/', views.ApartmentTypeDetail.as_view()),

]
