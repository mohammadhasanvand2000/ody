from django.shortcuts import render,redirect
from .models import Medicine,MedicationBox
from django.http import HttpResponse
# Create your views here.
from django.db.models import *
from django.core.exceptions import SuspiciousOperation
from django.shortcuts import get_object_or_404
from django.http import Http404


def index (request):
    
    return render (request,'index.html')


def all_medicine(request):
    if request.method == "GET":
        all=Medicine.objects.all()
        context={'all':all}
        return render(request,"medicine/medicine_list.html",context)









def add(request, med_id):
    buy = None
    
    
    if request.method == "GET":
        try:
            med = Medicine.objects.get(id=med_id)
            split2 = med.title
            
            
                
            drug = MedicationBox.objects.filter(selected_medicines__drug_interactions__icontains=split2).exists()
            if drug :
                conflicting_med = MedicationBox.objects.filter(selected_medicines__drug_interactions__icontains=split2).first()
                if conflicting_med:

                    context = {'h': conflicting_med.selected_medicines, 'med': med}
                    return render(request, 'drug.html', context)
                

            else:
                buy = MedicationBox.objects.create(selected_medicines_id=med_id)
                context = {'buy': buy}
                return redirect('all')
            
        except SuspiciousOperation as e:
            return HttpResponse(e, status=400)
        

    context = {'buy': buy}
    return render(request, 'mebox.html', context)







def delete_cart(request, d_id):
    try:
        medication_box = MedicationBox.objects.get(id=d_id)
        medication_box.delete()
        return redirect('cart')
    except MedicationBox.DoesNotExist:
        raise Http404("MedicationBox does not exist")                
        
    



def cart(request):

    if request.method =="GET":
        f=MedicationBox.objects.all() 
        
       
         
                
        return render(request, 'mebox.html', {'f': f}) 



