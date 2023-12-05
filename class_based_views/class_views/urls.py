from django.urls import path
from .views import ArticleDetailView

urlpatterns = [
    path('<pk>/', ArticleDetailView.as_view()),
]