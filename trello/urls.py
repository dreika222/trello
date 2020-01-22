from django.urls import include, path
from rest_framework import routers
from trello.quickstart import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('trello/board', views.BoardView.as_view()),
    path('trello/organization', views.OrganizationView.as_view()),
    path('trello/list', views.ListView.as_view()),
    path('trello/card/create', views.CreateCardView.as_view()),
]