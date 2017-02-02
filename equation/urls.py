""" URLs for Exam Application """
from django.conf.urls import url
from equation.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
app_name = 'equation'

urlpatterns = [
    url(r'^save/$', SaveEquation.as_view()),
    url(r'^data/$', AjaxSaveData.as_view()),
    url(r'^getdata/$', AjaxGetData.as_view()),
    url(r'^upload/$', csrf_exempt(AjaxUpload.as_view())),
    url(r'^image/$', csrf_exempt(AjaxGetImage.as_view())),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	
