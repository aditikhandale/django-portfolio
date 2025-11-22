from django.shortcuts import render
import requests  
from django.contrib import messages
GOOGLE_SHEET_URL = "https://script.google.com/macros/s/AKfycbyUfBUpM-dEd3t893KC3K3DL6MR3eO1wyBimo730vtT0waZohmEcnIDGSrqekPzD0AC/exec"
# Create your views here.
def home(request):
   
    return render (request,'index.html')

def portfolio(request):
    return render (request,'portfolio.html')

def contact(request):
    if request.method == "POST":
        data = {
            "name": request.POST.get("name"),
            "email": request.POST.get("email"),
            "subject": request.POST.get("subject"),
            "message": request.POST.get("message"),
        }

        # Google Sheet ला POST
        try:
            r = requests.post(GOOGLE_SHEET_URL, data=data)
            if r.status_code == 200:
                messages.success(request, "Message sent successfully!")
            else:
                messages.error(request, "Failed to send message. Try again.")
        except:
            messages.error(request, "Server error. Try again.")

    return render(request, 'contact.html')


def services(request):
    return render (request,'services.html')
    