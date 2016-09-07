from django.shortcuts import render, redirect
from ..loginreg.models import User
from .models import Pokes
from django.contrib import messages
from datetime import datetime, date
from django.db.models import Q
from django.core.urlresolvers import reverse
from django.db.models import Count, Sum
# Create your views here.

def pokes(request):
	'''
	counts the number of people who poked you:
		ser.objects.exclude(id=request.session['user']).annotate(counter=Count("receiverspoke__pokes")),
	'''
	context = {
		'user':User.objects.get(id=request.session['user']),
		'total_pokers':User.objects.filter(id=request.session['user']).annotate(counter=Count("receiverspoke__pokes")),
		'opokes':User.objects.exclude(id=request.session['user']).annotate(counter=Sum("receiverspoke__pokes")),
		'my_pokes':Pokes.objects.filter(receiver=request.session['user']),
		}
	return render(request, 'main/pokes.html', context)
def poke_process(request):
	senderid = User.objects.get(id=request.session['user'])
	receiverid = User.objects.get(id=request.POST['receiver'])
	poke_check = Pokes.objects.filter(sender=senderid, receiver=receiverid)
	# print poke_check[0].pokes
	if not poke_check:
		Pokes.objects.create(sender=senderid, receiver=receiverid, pokes=1)
		print poke_check
		return redirect('/pokes')
	else:
		# incrementing the poke column by one each time someone is poked, instead of creating a whole object again
		poke_check[0].pokes += 1
		poke_check[0].save()
		# print poke_check[0].pokes
		# print poke_check
		return redirect('/pokes')
