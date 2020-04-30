from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('patient/create/', views.PatientCreate.as_view(), name='createPatient'),
    path('travel/create/', views.TravelHistoryCreate.as_view(), name='createTravelHistory'),
    path('patients/', views.PatientListView.as_view(), name='patients'),
    path('travels/', views.TravelListView.as_view(), name='travels'),
    path('patient/<int:pk>',
         views.PatientDetailView.as_view(), name='patient-detail'),
    path('travel/<int:pk>',
         views.TravelHistoryDetailView.as_view(), name='travelhistory-detail'),
    
    # new path add by Nicholas on 28th April
    path('travel/delete/<int:pk>', views.TravelHistoryDelete.as_view(), name='deleteTravelHistory'),
]