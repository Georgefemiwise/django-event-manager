from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import (
    RegisterView,
    LoginView,
    CurrentUserView,
    CategoryListCreateView,
    CategoryRetrieveUpdateDestroyView,
    TagListCreateView,
    TagRetrieveUpdateDestroyView,
    EventListView,
    EventCreateView,
    OrganizerEventListView,
    EventRetrieveUpdateDestroyView,
    AdminEventListView,
)

urlpatterns = [
    # Authentication
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("me/", CurrentUserView.as_view(), name="current_user"),
    # Categories
    path("categories/", CategoryListCreateView.as_view(), name="category-list"),
    path(
        "categories/<int:pk>/",
        CategoryRetrieveUpdateDestroyView.as_view(),
        name="category-detail",
    ),
    # Tags
    path("tags/", TagListCreateView.as_view(), name="tag-list"),
    path("tags/<int:pk>/", TagRetrieveUpdateDestroyView.as_view(), name="tag-detail"),
    # Events
    path("events/", EventListView.as_view(), name="event-list"),
    path("events/create/", EventCreateView.as_view(), name="event-create"),
    path("events/my/", OrganizerEventListView.as_view(), name="organizer-event-list"),
    path(
        "events/<int:pk>/",
        EventRetrieveUpdateDestroyView.as_view(),
        name="event-detail",
    ),
    # Admin
    path("admin/events/", AdminEventListView.as_view(), name="admin-event-list"),
]
