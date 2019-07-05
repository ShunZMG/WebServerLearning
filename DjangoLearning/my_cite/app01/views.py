from django.shortcuts import render,HttpResponse

# Create your views here.

def test_view(request):

    print("执行业务逻辑",request)
    print(dir(request))

    return HttpResponse("500一次够吗")

def login_view(request):
    print("登录")
    # data = """<form method="post">
    # <input type="text" name="username" placeholder="Please input your username">
    # <br/>
    # <input type="password" name="password" placeholder="Please input your password">
    # <br/>
    # <input type="submit" value="提交">
    # </form>"""

    # return HttpResponse(data)

    return render(request,'form.html')

