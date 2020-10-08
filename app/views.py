from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView,FormView,ListView
from app.forms import *
from django.http import HttpResponse
from app.models import *



class CBV_template(TemplateView):
    template_name='CBV_template.html'



class CBV_contexttemplate(TemplateView):
    template_name='CBV_contexttemplate.html'

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        #context['data']='Hai python'
        #context['data1']='Hai Hello django'
        context['form']=Student()
        return context

    def post(self,request):
        form_data=Student(request.POST)
        if form_data.is_valid():
            return HttpResponse(str(form_data.cleaned_data))



class CBV_formview(FormView):
    form_class=Student
    template_name='CBV_formtemplate.html'


    def form_valid(self,form):
        return HttpResponse(str(form.cleaned_data))



class CBV_modelform(FormView):
    form_class=ProfileForm
    template_name='CBV_modelform.html'


    def form_valid(self,form):
        form.save()
        return HttpResponse('Form data has been saved into databse successfully')


class CBV_listview(ListView):
    model=Profile
    #queryset=Profile.objects.filter(name='Dhoni')
    context_object_name='profiles'
    template_name='CBV_listtemplate.html'
    ordering=['name']
























































