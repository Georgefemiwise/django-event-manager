from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
# from django_filters.rest_framework import DjangoFilterBackend
from .models import Event, Category, Tag
from .serializers import (
    UserSerializer,
    RegisterSerializer,
    CustomTokenObtainPairSerializer,
    EventSerializer,
    EventCreateUpdateSerializer,
    EventStatusUpdateSerializer,
    CategorySerializer,
    TagSerializer,
)
from .permissions import IsAdmin, IsOrganizer, IsEventOrganizer

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer


class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdmin]


class CategoryRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdmin]


class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdmin]


class TagRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdmin]


class EventListView(generics.ListAPIView):
    queryset = Event.objects.filter(status="approved", is_public=True)
    serializer_class = EventSerializer
    permission_classes = [AllowAny]
    # filter_backends = [DjangoFilterBackend]
    filterset_fields = ["category", "tags", "start_time"]


class EventCreateView(generics.CreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventCreateUpdateSerializer
    permission_classes = [IsOrganizer]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)


class OrganizerEventListView(generics.ListAPIView):
    serializer_class = EventSerializer
    permission_classes = [IsOrganizer]

    def get_queryset(self):
        return Event.objects.filter(organizer=self.request.user)


class EventRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    permission_classes = [IsOrganizer | IsAdmin]

    def get_serializer_class(self):
        if self.request.method in ["PUT", "PATCH"]:
            if self.request.user.is_admin():
                return EventStatusUpdateSerializer
            return EventCreateUpdateSerializer
        return EventSerializer

    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            if self.request.user.is_admin():
                return [IsAdmin()]
            return [IsEventOrganizer()]
        return super().get_permissions()


class AdminEventListView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAdmin]
    # filter_backends = [DjangoFilterBackend]
    filterset_fields = ["status", "organizer", "category", "tags"]
