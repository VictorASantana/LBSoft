from django.urls import path

from .views import ChairView

urlpatterns = [
    # path chair
    path("chair/", ChairView.as_view(actions={"get" : "list_all"})),
    path("chair/<int:pk>/", ChairView.as_view(actions={"get": "retrieve", "put": "update"})),
]