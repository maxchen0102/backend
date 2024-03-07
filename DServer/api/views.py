from django.shortcuts import render
import json 
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def api_home(request): 
    
    try :
        params = request.GET.dict()
        print(params)
        
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