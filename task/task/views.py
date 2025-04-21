from django.shortcuts import render

def func(request):
    c = ''
    data = {}
    try:
        if request.method == 'POST':
            n1 = float(request.POST.get('val1'))
            n2 = float(request.POST.get('val2'))
            answer = request.POST.get('opr')
            if answer == '+':
                c = n1 + n2
            elif answer == '-':
                c = n1 - n2
            elif answer == '*':
                c = n1 * n2
            elif answer == '/':
                c = n1 / n2
        data = {
                'n1' : n1,
                'n2' : n2,
                'answer' : answer,
                'c' : c
            }
    except:
        c = 'Invalid Input'

    return render(request , 'index.html' , data)