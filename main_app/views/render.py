from django.shortcuts import render




def contactpage(request):
    return render(request, 'mainpages/contact.html')

