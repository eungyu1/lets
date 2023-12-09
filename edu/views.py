from django.views.generic import View
from django.shortcuts import render,redirect
from .models import feed #현재폴더의 models라는 파일에서 Feed 라는 이름의 class를 가져오세요

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
        param2 = request.FILES.get('up_photo',False)
        print(f"param:(param)")
        f = feed(content=param,photo=param2)
        f.save()
        return redirect('edu:tag_study')