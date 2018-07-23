from django.urls import path
from .views import RecordCreateView, RecordDetailView

app_name = 'api'

urlpatterns = [
    path('record', RecordCreateView.as_view(), name='record_create'),
    path('record/<int:pk>', RecordDetailView.as_view(), name='record_details'),
]
