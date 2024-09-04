from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306228756',
        'name': 'Krisna Putra Purnomo',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
