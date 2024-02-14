from django.urls import path
from . import views

urlpatterns = [
    # Define URLs for Employee views
    path('emp/', views.EmployeeCreateView.as_view(), name='employee-create'),
    path('emp/<int:pk>/', views.EmployeeRetreiveUpdateView.as_view(), name='employee-get-retrieve-update'),
    path('emp/get/', views.EmployeeGetView.as_view(), name='employee-get'),
    path('emp/token/<int:pk>/', views.EmployeeTokenCreationView.as_view(), name='employee-token-and-info'),
]
