from django.urls import path
from .views import EmployeeView

urlpatterns = [
    path('employee/', EmployeeView.as_view(), name="employee"),
    path('employee/<int:pk>/', EmployeeView.as_view(), name="employee-details")

]