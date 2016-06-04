from django.shortcuts import render


def site_index(request):
    return render(request, 'index.html', {})
