from django.shortcuts import render



def base(request):
	return render(request, 'base.html') 


def reverse(request):
	user_text = request.GET['usertext']
	rev_ut = user_text[::-1]
	return render(request, 'reverse.html', {'usertext': rev_ut}) 