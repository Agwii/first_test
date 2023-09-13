from django.shortcuts import render

def index(request):

    context = {
        'click': 'click'
    }

    return render(request, 'articles/index.html', context)

def catch(request, name, number):
    # url에서 변수로 들어오는 값을 구분해서 사용하기 위해 받아와야한다
    context = {
        'name': name,
        'number': number,
    }
    return render(request, 'articles/catch.html', context)

# Create your views here.
