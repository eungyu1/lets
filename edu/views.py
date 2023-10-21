from django.views.generic import View
from django.shortcuts import render

# Create your views here.
class Index(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)