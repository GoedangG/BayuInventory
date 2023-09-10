from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Bayu',
        'Amount': '99',
        'Description' : 'Halo!'
    }

    return render(request, "main.html", context)