"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
 from django.conf.urls import url
  def method_to_run(request):
      print "Whatever route that was hit by an HTTP request (by the wayt) decided to invoke me!"
      print "By the way, here's the request object that Django automatically passes us:", request
      print "By the by, we still aren't delivering anything to the browser, so you should see 'ValueError at /'"
  urlpatterns = [
      url(r'^$', method_to_run)
  ]