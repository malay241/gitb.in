from django.shortcuts import render

def downloader(request):
	if request.method  == 'GET':
		return render(request,'youtube.html')
