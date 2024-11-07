from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def first_view(request):
    if request.method == 'GET':
        return Response({"message": "Hello, world!"})
    if request.method == 'POST':
        try: 
            msg = request.data['message']
            return Response({"your_message": msg})
        except:
            return Response({"message": "error"})