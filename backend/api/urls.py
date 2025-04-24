from django.urls import path
from .views import MultiDocumentSimilarity

urlpatterns = [
    path('compare/', MultiDocumentSimilarity.as_view()),
]
