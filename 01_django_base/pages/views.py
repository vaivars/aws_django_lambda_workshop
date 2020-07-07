from django.http import HttpResponse

def homePageView(request):
    html = "<html><body>Hello,World!</body></html>"
    return HttpResponse(html)