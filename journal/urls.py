from django.urls import path
from .views import JournalList, JournalCreate, JournalUpdate, JournalDelete

urlpatterns = [
    path('', JournalList.as_view(), name='diary_list'), 
    path('create/', JournalCreate.as_view(), name='diary_create'),
    path('<int:pk>/update/', JournalUpdate.as_view()), 
    path('<int:pk>/delete/', JournalDelete.as_view()),
]