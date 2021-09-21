from django.shortcuts import render


def page_not_found(request, exeption):
    return render(request, '404.html', status=404)
