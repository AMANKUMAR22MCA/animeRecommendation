from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegisterSerializer
from .graphql_service import search_anime


class RegisterView(APIView):
    """
    Handles user registration and returns JWT tokens on success.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def search_anime_view(request):
    """
    Search for anime based on a query parameter.
    """
    query = request.GET.get('q')
    if not query:
        return Response({"error": "Query param 'q' is required."}, status=status.HTTP_400_BAD_REQUEST)
    
    data = search_anime(query)
    return Response(data)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def user_preferences(request):
    """
    Retrieve or update user's favorite genres.
    """
    user = request.user

    if request.method == 'GET':
        return Response({'favorite_genres': user.favorite_genres})

    if request.method == 'POST':
        user.favorite_genres = request.data.get('favorite_genres')
        user.save()
        return Response({'message': 'Preferences updated successfully.'})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def anime_recommendations_view(request):
    """
    Return anime recommendations based on user's favorite genres.
    """
    user = request.user
    genres = user.favorite_genres or []

    if not genres:
        return Response({"error": "No genres set in preferences."}, status=status.HTTP_400_BAD_REQUEST)

    recommendations = []
    for genre in genres:
        data = search_anime(genre)
        media = data.get("data", {}).get("Page", {}).get("media", [])
        recommendations.extend(media)

    return Response({"recommendations": recommendations})
