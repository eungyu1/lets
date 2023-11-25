from django.views.generic import View
from django.shortcuts import render,redirect


# Create your views here.
class Index(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)
    
class TagStudy(View):
    template_name = 'tag_study.html'
    
    def get(self, request):
        return render(request, self.template_name)

class NewContent(View):
    template_name = 'upload_form.html'

    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        param = request.POST.get('content','')
        print(f"param:(param)")
        return redirect('edu:tag_study')