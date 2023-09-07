from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Ardhika Satria Narendra',
        'class': 'Platform-Based Development KKI'
    }

    return render(request, 'main.html', context)