from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib  
from sklearn import metrics
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.conf import settings
def homedetail(request):
    try:
        if request.method=="POST":
            n1= request.POST.get('name')
            n2= request.POST.get('email')
        print(n1+n2)
        return HttpResponseRedirect ('test/')
    except:
        pass
        return render(request,"index.html")

def about(request):
    return render(request,"about.html")
def homee(request):
     return render(request,"pricee.html")
def test(request):
     return render(request,"test.html")
def properties(request):
     return render(request,"test.html")
def testimonials(request):
     return render(request,"test.html")
def contact(request):
     return render(request,"contact.html")
def real(request):
     return render(request,"real.html")

def form_login(request):
     try:
          var1=request.GET['username']
          var2=request.GET['lastName']
          print(var1+var2)
     except:
          pass     
     return render(request,"form.html")
def login(request):
     return render(request,"login.html")
def error(request):
     return render(request,"error.html")
# Paths for dataset and model
CSV_PATH = os.path.join(settings.BASE_DIR, "static", "USA_housing.csv")
MODEL_PATH = os.path.join(settings.BASE_DIR, "static", "house_price_model.pkl")

# Train the model
def train_model():
    data = pd.read_csv(CSV_PATH)
    data = data.drop(['Address'], axis=1)

    X = data.drop('Price', axis=1)
    Y = data['Price']

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, Y_train)

    # Save Model
    joblib.dump(model, MODEL_PATH)

if not os.path.exists(MODEL_PATH):
    train_model()

# Home Page
def homee(request):
    return render(request, "pricee.html")

# Predict Function
def result(request):
    try:
        if not all([request.GET.get(f"n{i}") for i in range(1, 6)]):
            return render(request, "predict.html", {"message": "Missing input values!"})

        var1 = float(request.GET.get('n1', 0))
        var2 = float(request.GET.get('n2', 0))
        var3 = float(request.GET.get('n3', 0))
        var4 = float(request.GET.get('n4', 0))
        var5 = float(request.GET.get('n5', 0))

        predicted_price_value = (var1 * 0.5) + (var2 * 10) + (var3 * 5) + (var4 * 2) + (var5 * 20)
        predicted_price = f"Rs {round(predicted_price_value)}"
        
        property_type = request.GET.get('propertyType', '')

        context = {
            "predicted_price": predicted_price,
            "propertyType": property_type,
        }
        return render(request, "pricee.html", context)

    except Exception as e:
        return render(request, "error.html", {"message": f"Invalid Input: {e}"})








#chatbot 
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHATBOT_RESPONSES_FILE = os.path.join(BASE_DIR, "chatbot_responses.json")


def load_chatbot_responses():
    try:
        with open(CHATBOT_RESPONSES_FILE, "r") as file:
            return json.load(file)
    except Exception as e:
        print("Error loading chatbot responses:", e)
        return {}


@csrf_exempt
def chatbot_response(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body) 
            user_message = data.get("message", "").lower()
            chatbot_responses = load_chatbot_responses()  
            response = chatbot_responses.get(user_message, "Sorry, I can only provide basic information about HomeFinder.")
            return JsonResponse({"reply": response})
        except json.JSONDecodeError:
            return JsonResponse({"reply": "Invalid request."}, status=400)

    return JsonResponse({"reply": "Use POST method to interact with the chatbot."})


def chatbot_page(request):
    return render(request, "chat.html")  


def ar_home_view(request):
    return render(request, '360img.html')




# def property_info(request):
#     return render(request, 'display.html')
