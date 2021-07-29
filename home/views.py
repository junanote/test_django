from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def index(request):
    path = request.path
    resultstr = ''
    if path == '/home':
        resultstr = '<h1>여기는 home입니다.</h1>'
    else :
        resultstr = '<h1>여기는 주나노트입니다.</h1>'

    return HttpResponse(resultstr)

def index01(request):
    result = {'first':'juna','second':'you'}
    return render(request, 'index.html', context=result)

def index02(request):
    # request.GET['first']
    # result = {'first':request.GET['first'],'second':request.GET['second']}
    # first = request.GET[first']
    # second = request.GET['second']
    # pd.read_csv('../static/ratings-20m.csv')

    return render(request, 'index.html', context=result)




