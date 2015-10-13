from django.shortcuts import render
import random
from excuse.models import Excuse
from excuse.models import Emp
from excuse.models import Emp2


# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
'''
def home1(request):

	excuses = [
		"Hail Hydra!!!!!",
		"QQQQQQQQQ",
		"SSSSSSSSSSSSSSSS",
		"Apple & Sheng",
	]

	excuse = random.choice(excuses)
	

	return render(request,'QQ.html',{'excuse': excuse })
'''
	
def home2(request):
	#excuse = random.choice(Excuse.objects.all())
	#SS=	request.is_secure()
	#excuse2 = Emp.objects.all()
	excuse2  = request.is_ajax()

	if excuse2:
		dic={}
		excuse = Emp.objects.all()	
		list = []
		for ele in excuse:
		    #Empno = ele.Empno
			list = [ele.Ename,ele.Job, ele.Mgr,ele.HireDate,ele.Sal,ele.Deptno]
			dic[ele.Empno] = list
			# Ename = 
			# Job   = ele.Job
			# Mgr   = ele.Mgr
			# HireDate = ele.HireDate
			# Sal = ele.Sal
			# Deptno = ele.Deptno

		#response = JsonResponse({'foo':'bar'})
		
		response = JsonResponse(dic) # package a Json file
		#response = JsonResponse({'QQ':['SS','AA',1,'BB',2]})

		return response
	else:
		return render(request,'QQ2.html',{'excuse': excuse2 })
		
	#excuse2  = request.is_ajax()
	#excuse2  = request.get_host()
	
	
	
def home3(request):
	excuse2 = Emp.objects.get(Empno=7839)
	#pathQQ  = request.is_ajax()
	#response = HttpResponse("The test is succeed!!!!")
	response = HttpResponse(excuse2)
	return response
	
	
	
def homeQQ(request):
	excuses = [
	'It\'s my first time to build a web',
	'With the Django24 !!',
	'Hail Hydra!!',
	'Hello World!!',
	]
	
	#excuse_dj = random.choice(excuses)
	if request.is_ajax():
		if request.method == 'GET':
		
			return HttpResponse('QQQQSSSSQ')
			
		elif request.method == 'POST':
		
			num = request.POST['Empno']
			employee = Emp.objects.get(Empno=num)
			
			name = employee.Ename
			number = employee.Empno
			sal = employee.Sal
			job = employee.Job
			comm = employee.Comm
			
			return JsonResponse({
			'ename':name,
			'empno':number,
			'Job':job,
			'Sal':sal,
			'Comm':comm
			})
	
	else:
		
		return render(request,'QQ2.html',{'excuse_html':excuses})
	
	# return HttpResponse(random.choice(excuses))
	
	