# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader, Context, RequestContext
from django.contrib import messages
from django.views.generic.edit import FormView, CreateView, DeleteView, UpdateView
from django.core.urlresolvers import reverse_lazy, reverse
from django.views.generic.edit import FormView
from biblioteca.forms import registrar_form


class registrar_view(CreateView):
    
    template_name= 'registro.template.html'
    form_class = registrar_form
    success_url = reverse_lazy('biblioteca:subir')
   
    def registrar_valid(request):
        if request.method == 'POST':
            form = registrar_form(request.POST)
            var = form.cleaned_data['cargar_app']
            print(form)
            if form.is_valid():
                form.save()
                
                return HttpResponseRedirect('biblioteca:subir')
        else:
            form = registrar_form()
        return render(request, 'registro.template.html',{'form':form}, context_instance=RequestContext(request))

