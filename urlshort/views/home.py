from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
from urlshort.models.urlshort import Urlshortadd
from urlshort.models.userdetails import UserDetails
from django.core.files import File
from datetime import datetime
import validators
# from bs4 import BeautifulSoup
import socket
# import requests
import random
import string


def index(request):
	if request.method  == 'GET':
		return render(request,'index.html')
	else:
		url = request.POST.get('url')
		error_message = None
		validators.url(url)
		if not validators.url(url):
			error_message = '''URL is not valid ! Try again with Valid URL !'''
			data = {
				'error':error_message
			}
			return render(request,'index.html', data)

		A = string.ascii_lowercase  #lowercase alphabet
		a = string.ascii_uppercase  #uppercase alphabet
		N = string.digits #numeric digits
		list = A+N+a

		keyword = ''.join(random.choices(list, k = 6))

		url_short = "http://127.0.0.1:8000/"+keyword

		# date = datetime.now()
  #     	hostname = socket.gethostname()
  #     	userip = socket.gethostbyname(hostname)
     	
  #    	#Country Scrapper
  #    	site = "https://iplocation.com/"
  #    	r=requests.get(site)
  #     	s=BeautifulSoup(r.text,"html.parser")
  #     	country=s.find("span",class_="country_name")
  #     	country = country.text.strip()
  #     	region = s.find("span",class_="region_name")
  #     	region = region.text.strip()
  #     	city = s.find("td",class_="city")
  #     	city = city.text.strip()

		urlshortadd = Urlshortadd(original_url=url,
									shortend_url=url_short,
									keyword = keyword)

		# userdeatils = UserDetails(date=date,
		# 						hostname=hostname,
		# 						userip = userip,
		# 						country=country,
		# 						region=region,
		# 						city=city)

		# userdeatils.adduserdetails()

		urlshortadd.addtheurl()
		data = {
		'url':url,
		'url_short':url_short
		}

		return render(request,'shortend.html',data)
