from django.shortcuts import render, redirect, reverse
from .models import User


# =================================================
# 						HELPERS
# =================================================

def flash_errors(errors, request):
	for error in errors:
		messages.error(request, error)

def current_user(request):
	return User.objects.get(id=request.session['user_id'])

def user(request, id):
	context={
		'user' : current_user(request),
	}
	return render(request, 'login/index.html', context)

# ==============================================================
# 						RENDER
# ==============================================================

# Create your views here.
def index(request):
	return render(request, 'login/index.html')

# =================================================
#                       PROCESS
# =================================================

