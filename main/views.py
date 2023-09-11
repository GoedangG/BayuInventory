from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'Inventory_Owner': 'Bayu',
        'NPM': '2206826330',
        'Amount': '99',
        'Description' : 'Halo!'
    }

    return render(request, "main.html", context)