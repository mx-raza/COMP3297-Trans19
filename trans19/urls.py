from django.urls import path
from . import views

app_name = 'trans19'

urlpatterns = [
    path('', views.index, name='index'),
    path('locations/', views.locations, name='locations'),
    path('patients/', views.patients, name='patients'),
    path('patients/<int:patient_id>/', views.detail, name='detail'),
    path('patients/new/', views.PatientCreate.as_view(), name='patient_new'),
    path('patients/<int:pk>/edit', views.PatientUpdate.as_view(), name='patient_edit'),
    path('patients/<int:pk>/delete', views.PatientDelete.as_view(), name='patient_delete'),
    path('patients/search/', views.SearchConnectionsView, name='search_connections'),
    path('locations/new', views.location_new, name='location_new'),
    path('locations/<int:pk>/edit', views.location_edit, name='location_edit'),
    path('locations/<int:pk>/delete', views.LocationDelete.as_view(), name='location_delete'),
]
