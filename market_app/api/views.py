from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def first_view(request):
    if request.method == 'GET':
        return Response({"message": "Hello, world!"})
    if request.method == 'POST':
        try: 
            msg = request.data['message']
            return Response({"your_message": msg}, status=status.HTTP_201_CREATED)
        except:
            return Response({"message": "error"}, status=status.HTTP_400_BAD_REQUEST)