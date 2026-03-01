from django.urls import path
from .views import UserCreateAPIView , UserDeleteAPIView ,UserListAPIView ,TestProtectedAPI

urlpatterns = [
    path('users/create/', UserCreateAPIView.as_view(), name='user-create'),
    path('user/delete/<int:user_id>/',UserDeleteAPIView.as_view()),
    path('users/' , UserListAPIView.as_view()),
    path('testprotected/',TestProtectedAPI.as_view(),name='test-protected')
]
