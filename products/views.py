from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'products/home.html')


from django.shortcuts import render
from .forms import BikeFilterForm
from .models import Accessory,BikeBrand, BikeModel

def product_filter_view(request):
    from .models import BikeModel, BikeBrand  # Ensure these are imported

    form = BikeFilterForm(request.GET or None)
    products = None

    # Dynamically set company list
    form.fields['company'].queryset = BikeBrand.objects.all()  # ✅ Important
    print("Set company choices")

    if 'company' in request.GET:
        company_id = request.GET.get('company')
        form.fields['model'].queryset = BikeModel.objects.filter(brand_id=company_id)
        print("Updated model choices dynamically")

    if form.is_valid():
        print("Form is valid")
        model = form.cleaned_data.get('model')
        print("Selected model:", model)
        products = Accessory.objects.filter(bike_model=model)
        print("Products found:", products)
    else:
        print("Form errors:", form.errors)

    return render(request, 'products/filter.html', {'form': form, 'products': products})


from django.http import JsonResponse
from .models import BikeModel

def load_models(request):
    company_id = request.GET.get('company_id')
    if not company_id:
        return JsonResponse({'error': 'Missing company_id'}, status=400)
    company_id = int(company_id)
    try:
        models = BikeModel.objects.filter(brand_id=company_id).values('id', 'model_name')
        
        return JsonResponse(list(models), safe=False)
    except Exception as e:
        print("ERROR:", e)
        return JsonResponse({'error': str(e)}, status=500)
    





def cart_func(request):
    
    return render(request, 'products/cart.html')

    