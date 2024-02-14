from core_api.viewsets import EmployeeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employee',EmployeeViewSet)

# localhost:p/api/ -> for coming in thi router
# localhost:p/api/employee -> list function will be called which will provide data for employee model
# localhost:p/api/employee/5(id) -> it will call retrive function that will get data table about the datapoint with that id
