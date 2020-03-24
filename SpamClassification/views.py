from django.http import HttpResponse
from . import Classifier
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, "enteremail.html")



@csrf_exempt
def classify(request):
    print("request.post is:",request)
    email = request.POST.get('email')
    print("email is:",email)
    pred = Classifier.predict(email)
    if pred == "spam":
        res ={
            "response_code": 1,
            "response_message": pred
        }
    else:
        res = {
            "response_code": 0
        }
    return JsonResponse(res,safe = False)


