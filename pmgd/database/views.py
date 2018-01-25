from django.shortcuts import render_to_response
from django.views import View

# Create your views here.

class Home(View):
    def get(self,request):
        return render_to_response("database/index.html")

class Genome_browser(View):
    def get(self,request):
        return render_to_response("database/genome_browser.html")

class Tools(View):
    def get(self,request):
        return render_to_response("database/tools.html")

class Tutorial(View):
    def get(self,request):
        return render_to_response("database/tutorial.html")

class Upload(View):
    def get(self,request):
        return render_to_response("database/upload.html")

