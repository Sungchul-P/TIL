from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    print("path : ", request.path)
    print("요청방식 : ", request.method)
    return HttpResponse("Scoops App.. Response")

def test1(request, word):
    print(word)
    return HttpResponse("test1 메서드." + word)

def test2(request, word):
    print(word)
    return HttpResponse("test2 메서드." + word)

def test3(request, word, second):
    print(word + "/" + second)
    return HttpResponse("test3 메서드." + word + "/" + second)

def test4(request, word, second):
    print(word + "/" + second)
    return HttpResponse("test4 메서드." + word + "/" + second)

def test6(request, year, month, myname):
    print(str(year) + "/" + str(month) + "/" + myname)
    return HttpResponse("test6 메서드.{} / {} / {}".format(year, month, myname))

def func7(request, num):
    print(num, type(num))
    return HttpResponse("응답7 .. param:{}".format(num))