from django.shortcuts import render

# Create your views here.
def stockPicker(request):
    
    # return HttpResponse("Hey I am picking stocks")
    return render(request, 'viewer/stockpicker.html')

def stockTracker(request):

    return render(request,'viewer/stocktracker.html')