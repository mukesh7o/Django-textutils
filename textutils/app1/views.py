from django.shortcuts import render
def index(request):
    return render(request,"index.html")
def removepunc(request):
    A = request.GET.get("text",'default')
    print(A)
    removepunc=request.GET.get("remove punctuations","off")
    fullcaps=request.GET.get("capital","off")
    new_line=request.GET.get("new line","off")
    space_remover=request.GET.get("space","off")

    print(removepunc)
    if removepunc == "on":
        analyzed= ""
        punctuations='''!@#$%^&*()_+-=?><,./'"';:[{}]*+-`~'''
        for char in A:
            if char not in punctuations:
                analyzed+=char
        params={'purpose':"Remove Punctuations","Analyzed_text":analyzed}
        return render(request, "rpunc.html", params)
    elif fullcaps == "on":
        analyzed = ""
        for char in A:
            analyzed += char.upper()
        params = {'purpose': "Upper Case", "Analyzed_text": analyzed}
        return render(request, "rpunc.html", params)
    elif new_line == "on":
        analyzed = ""
        for char in A:
            if char!="/n":
                analyzed+=char
        params = {'purpose': "Removed New line", "Analyzed_text": analyzed}
        return render(request, "rpunc.html", params)
    elif space_remover == "on":
        analyzed = ""
        for index, char in enumerate(A):
            if A[index]==" " and A[index+1]==" ":
                pass
            else:
                analyzed+=char
        params = {'purpose': "Extra space remover ", "Analyzed_text": analyzed}
        return render(request, "rpunc.html", params)
    else:
        return ("No idea")









# Create your views here.
