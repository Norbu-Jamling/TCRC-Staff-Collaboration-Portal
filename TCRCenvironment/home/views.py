from django.views.generic import TemplateView  
from home.forms import  HomeForm
from django.shortcuts import render, redirect  
from home.models import Post
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class HomeView(TemplateView):
    template_name='home/home.html'

    def get(self,request):
        form=HomeForm() 
        posts= Post.objects.all().order_by('-created')
        args={'form':form,'posts':posts}
        return render(request, self.template_name,args)
    
    def post(self,request):
        form=HomeForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.user=request.user
            post.save()
            text = form.cleaned_data['post']
            form = HomeForm()
            return redirect("home")
        
        args={'form':form, 'text':text}
        return render(request, self.template_name,args)
