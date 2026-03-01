from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from students.views import StudentViewSet


router = DefaultRouter()
router.register('students',StudentViewSet)

urlpatterns = router.urls

# urlpatterns = [
    

#     # student endpoints
#     path('students/',StudentViewSet.as_view(
#         {
#             'get': 'list',
#             'post': 'create'
#         }
#     ))
# ]
