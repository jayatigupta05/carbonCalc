from django.shortcuts import render
from .forms import ActivityForm
from .models import EmissionFactor

# Create your views here.
def home(request):
    form = ActivityForm()
    emission_result = None
    category = ''

    # If the form is submitted
    if request.method == 'POST':
        form = ActivityForm(request.POST)
        if form.is_valid():
            # Extract category and value from the form
            category = form.cleaned_data['category']
            value = form.cleaned_data['value']
            
            # Try to get the emission factor for this category
            try:
                factor = EmissionFactor.objects.get(category=category)
                emission_result = value * factor.co2_per_unit  # Calculate emissions
            except EmissionFactor.DoesNotExist:
                emission_result = "No emission factor found for this category."

    return render(request, 'home.html', {
        'form': form,
        'result': emission_result,
        'category': category,
    })