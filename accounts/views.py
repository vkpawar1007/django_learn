from .serializers import UserCreateSearializer , UserListSearializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny , IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsAdmin
from .models import User
# Create your views here.

class UserCreateAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self,request):
        serializer = UserCreateSearializer(data = request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    "message":"User created succesfully",
                    "user_id":user.id,
                    "role":user.role
                },
                status = status.HTTP_201_CREATED
            )

        return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)

class UserDeleteAPIView(APIView):    
    permission_classes = [IsAuthenticated,IsAdmin]

    def delete(self, request , user_id):
        try:
            user = User.objects.get(id = user_id)
        except User.DoesNotExist:
            return Response(
                {
                    'details':"User not Found"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        
        if user.role == 'ADMIN':
            return Response(
               {
                    'details':"You do not have permission to delete this user"
                },
                status=status.HTTP_403_FORBIDDEN
            )
        
        user.delete()

        return Response(
               {
                    'details':"User Deleted Succesufully",
                    'Deleted By':f"{request.user.username}"
                },
                status=status.HTTP_204_NO_CONTENT
            )

class UserListAPIView(APIView):
    # permission_classes = [IsAdmin]


    def get(self, request):

        users = User.objects.all().order_by('id')
        serialzer = UserListSearializer(users,many=True)
        return Response(serialzer.data)

class TestProtectedAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response(
            {'message':f"Hello {request.user.username}"}
        )