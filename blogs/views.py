from django.shortcuts import render

# Create your views here.
def blogs_index(request):
	blogs = [
		{'name': 'Мой первый блог', 'author': {'name': 'admin'}, 'publication_date': '16.04.2022'},
		{'name': 'Мой второй блог', 'author': {'name': 'admin'}, 'publication_date': '17.04.2022'},
		{'name': 'Мой третий блог', 'author': {'name': 'admin'}, 'publication_date': '18.04.2022'},	
	]
	context = {
		'blogs': blogs,
	}
	return render(request, 'blogs/index.html', context)

def user_page(request):
	# как передовать переменные
	user_data = {
		'user_name': 'Mirlan',
		'user_age': 17,
	}
	context = {
		'user_data': user_data,
	}
	return render(request, 'blogs/user.html', context)

def friend_page(request):
	# как передовать переменные
	friend_data = {
		'friend_name': 'Rasim',
		'friend_age': 17
	}
	context = {
		'friend_data': friend_data,
	}
	return render(request, 'blogs/friend.html', context)

def first_page(request):
	first_data = {
		'first_name': 'Mirlan',
	}
	context = {
		'first_data': first_data,
	}
	return render(request, 'blogs/first.html', context)

def piramyda_page(request):
	piramyda_data = {
		'piramyda_name': 'Mika',
	}
	context = {
		'piramyda_data': piramyda_data,
	}
	return render(request, 'blogs/piramyda.html', context)
