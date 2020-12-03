#from datetime import datetime
#from django.http import HttpRequest

from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {})

#def contact(request):
#    """Renders the contact page."""
#    assert isinstance(request, HttpRequest)
#    return render(
#        request,
#        'app/contact.html',
#        {
#            'title':'Contact',
#            'message':'Your contact page.',
#            'year':datetime.now().year,
#        }
#    )

#def about(request):
#    """Renders the about page."""
#    assert isinstance(request, HttpRequest)
#    return render(
#        request,
#        'app/about.html',
#        {
#            'title':'About',
#            'message':'Your application description page.',
#            'year':datetime.now().year,
#        }
#    )
