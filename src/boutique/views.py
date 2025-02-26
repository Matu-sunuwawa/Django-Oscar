
# from django.views.generic import ListView, DetailView
# from .models import Boutique  # Assuming you have a Boutique model

# class BoutiqueListView(ListView):
#     model = Boutique
#     template_name = 'boutique/boutique_list.html'  # Adjust the template name as needed

# class BoutiqueDetailView(DetailView):
#     model = Boutique
#     template_name = 'boutique/boutique_detail.html'  # Adjust the template name as needed


from django.views import generic
from oscar.core.loading import get_model

Boutique = get_model('boutique', 'Boutique')

class BoutiqueListView(generic.ListView):
    model = Boutique
    template_name = 'boutique/boutique_list.html'
    context_object_name = 'boutique_list'

class BoutiqueDetailView(generic.DetailView):
    model = Boutique
    template_name = 'boutique/boutique_details.html'
    context_object_name = 'boutique'