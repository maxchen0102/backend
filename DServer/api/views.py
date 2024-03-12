from django.shortcuts import render
import json 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from product.models import Product

# Create your views here.


def api_home(request): 
    
    try :
        params = request.GET.dict()
        print(params)
        print("connect success")
        
    except:
        pass
    print(request.POST)
    print(request.GET)

    
   
    return  JsonResponse({"status": "GET success"})

@csrf_exempt
def api_post(request):
    if request.method == 'POST':
        # Handle POST request with JSON data
        try:
            json_data = json.loads(request.body)
            # Process JSON data here
            print(json_data)
            return JsonResponse({'status': 'POST success'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data'}, status=400)
    else:
        # Handle other HTTP methods (e.g., GET)
        return JsonResponse({'error': 'Unsupported method'}, status=405)
    

def get_product(request):
    data=Product.objects.all().values()
    print(data[0])
    print("connect success")
    return JsonResponse(data[0])


@csrf_exempt
def add_product(reqeust): 
    json_data = json.loads(reqeust.body)
    print(json_data)
    try : 
        new_product=Product(**json_data)
        new_product.save()
        return JsonResponse({'status': 'POST success'})
    except : 
        return JsonResponse({'error': 'Invalid JSON data'})
    

def delete_prodcut_by_id(request):
    data=request.GET.dict()
    id=data["id"]
    print(id)
    try : 
        product=Product.objects.get(id=id)
        print(product)
        product.delete()  
        return JsonResponse({'status': 'delete success'})
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Invalid id '})
        

@csrf_exempt
def update_product(request):
    data=json.loads(request.body)
    id=data["id"]
    print(id)
    
    try : 
        product=Product.objects.get(id=id)
        
        product.title=data["title"]
        product.conttne=data['conttne']
        product.price=data['price']
        product.save()
        
        
        return JsonResponse({'status': 'updata success'})
    except : 
        return JsonResponse({'error': 'Invalid id '})