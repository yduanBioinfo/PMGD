from django.shortcuts import render_to_response
from django.views import View

# Create your views here.

class Home(View):
    def get(self,request):
        return render_to_response("database/index.html")
