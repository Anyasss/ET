from django.shortcuts import render

def lista_compra(request):
    return render(request, 'compra/lista_compra.html', {})
