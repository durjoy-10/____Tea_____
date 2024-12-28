
from django.urls import path
from .import views 
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
  
    path('',views.all_chai,name='all_chai'),
    
    path('<int:chai_id>/',views.chai_details,name='Chai_details'),
    
    path('chai_stores/',views.chai_store_view,name='Chai_stores'),
    
    path('buy_tea/',views.buy_tea,name='buy_tea'),
    
    path('reviews/', views.reviews_page, name='reviews_page'),
    
    path('upload_video/',views.upload_video,name='upload_video'),
    
    path('video_list/',views.video_list,name='video_list'),
    
    path('thank_you/', TemplateView.as_view(template_name='chai/thank_you.html'), name='thank_you'),
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  