from django.shortcuts import render

# Create your views here.
def home(request):
    title = 'Concert Wishlist'

    context = {
        'title': title,
    }

    return render(request, 'home.html', context)
