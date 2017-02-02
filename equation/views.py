from django.shortcuts import render
from django.views import generic
from django.http import JsonResponse, HttpResponse
from equation.models import *

# Create your views here.
class SaveEquation(generic.View):
	def get(self, request):
		return render(request, 'equation/prueba.html')


class AjaxSaveData(generic.View):
	def get(self, request):
		print('ewewewewewew')
		head = request.GET['head']
		eq = request.GET['equation']

		print(head + ' ' + eq)

		quest = TextEquation(head=head, equation=eq)
		quest.save()

	
		return JsonResponse({'head': 'qwe'})


class AjaxGetData(generic.View):
	def get(self, request):

		questions = TextEquation.objects.last()

		return JsonResponse({'questions': questions.equation})

class AjaxUpload(generic.View):
	def get(self, request, *args, **kwargs):
		print("get")
		print(args)
		print(kwargs)
		print(request.FILES)
		return JsonResponse({
		    'uploaded': 1,
		    'fileName': 'question.png',
		    'url': 'http://www.mundoperro.net/wp-content/uploads/consejos-perro-feliz-verano-400x300.jpg',
		})

	def post(self, request, *args, **kwargs):
		print("post")
		print(args)
		print(kwargs)
		print(request.FILES)
		print(request.FILES['upload'])
		#file = request.FILES['upload']
		#image = Image(file=file)
		#image.save()
		#print(str(file))
		#print(image.file.url)
		#return JsonResponse({
		#    'uploaded': 1,
		#    'fileName': str(file),
		#    'url': image.file.url,
		#})
		return JsonResponse({
		    'uploaded': 1,
		    'fileName': 'question.png',
		    'url': 'http://www.mundoperro.net/wp-content/uploads/consejos-perro-feliz-verano-400x300.jpg',
		})

class AjaxGetImage(generic.View):
	def get(self, request, *args, **kwargs):
		print("get")
		print(args)
		print(kwargs)
		print(request.FILES)
		return JsonResponse({
		    'uploaded': 1,
		    'fileName': 'question.png',
		    'url': 'http://www.mundoperro.net/wp-content/uploads/consejos-perro-feliz-verano-400x300.jpg',
		})

	def post(self, request, *args, **kwargs):
		print("post")
		print(args)
		print(kwargs)
		print(request.FILES)
		print(request.FILES['upload'])
		return JsonResponse({
		    'uploaded': 1,
		    'fileName': 'question.png',
		    'url': 'http://www.mundoperro.net/wp-content/uploads/consejos-perro-feliz-verano-400x300.jpg',
		})