from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import FormInput

# Create your views here.
def submit_form(request):
    if request.method == 'POST':
        # delete old data
        FormInput.objects.all().delete()
        # extract input values
        data = request.POST.copy()
        data.pop('csrfmiddlewaretoken')
        # data from form to model
        new_form_input = FormInput(inputs=data)
        new_form_input.save()
        
        return redirect('data_view')
    else:
        return render(request, 'submit_form.html')


class DataView(ListView):
    model = FormInput
    template_name = 'data_view.html'
