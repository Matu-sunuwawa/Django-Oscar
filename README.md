# 🚀 Django-Oscar
introducing django-oscar what can it do?

## Basic Setup
RUN:
```
pipenv shell
```
Install the dependencies
RUN:
```
pip install -r requirements.txt
```
or
```
pip install django-oscar
pip install sorl-thumbnail
```
create directory <mark>src</mark> 
RUN:
```
django-admin startproject myoscarproject
mv myoscarproject src
```
#### Configure `settings.py` and `urls.py`
edit `settings.py`:
+ import all of Oscar’s default settings
```
from oscar.defaults import *
```
Now add Oscar’s context processors to the template settings, listed below:
```
...
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'oscar.apps.search.context_processors.search_form',
                'oscar.apps.checkout.context_processors.checkout',
                'oscar.apps.communication.notifications.context_processors.notifications',
                'oscar.core.context_processors.metadata',
            ],
        },
    },
]
```
update `INSTALLED APPS`:
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Added
    'django.contrib.sites',
    'django.contrib.flatpages',

    'oscar.config.Shop',
    'oscar.apps.analytics.apps.AnalyticsConfig',
    'oscar.apps.checkout.apps.CheckoutConfig',
    'oscar.apps.address.apps.AddressConfig',
    'oscar.apps.shipping.apps.ShippingConfig',
    'oscar.apps.catalogue.apps.CatalogueConfig',
    'oscar.apps.catalogue.reviews.apps.CatalogueReviewsConfig',
    'oscar.apps.communication.apps.CommunicationConfig',
    'oscar.apps.partner.apps.PartnerConfig',
    'oscar.apps.basket.apps.BasketConfig',
    'oscar.apps.payment.apps.PaymentConfig',
    'oscar.apps.offer.apps.OfferConfig',
    'oscar.apps.order.apps.OrderConfig',
    'oscar.apps.customer.apps.CustomerConfig',
    'oscar.apps.search.apps.SearchConfig',
    'oscar.apps.voucher.apps.VoucherConfig',
    'oscar.apps.wishlists.apps.WishlistsConfig',
    'oscar.apps.dashboard.apps.DashboardConfig',
    'oscar.apps.dashboard.reports.apps.ReportsDashboardConfig',
    'oscar.apps.dashboard.users.apps.UsersDashboardConfig',
    'oscar.apps.dashboard.orders.apps.OrdersDashboardConfig',
    'oscar.apps.dashboard.catalogue.apps.CatalogueDashboardConfig',
    'oscar.apps.dashboard.offers.apps.OffersDashboardConfig',
    'oscar.apps.dashboard.partners.apps.PartnersDashboardConfig',
    'oscar.apps.dashboard.pages.apps.PagesDashboardConfig',
    'oscar.apps.dashboard.ranges.apps.RangesDashboardConfig',
    'oscar.apps.dashboard.reviews.apps.ReviewsDashboardConfig',
    'oscar.apps.dashboard.vouchers.apps.VouchersDashboardConfig',
    'oscar.apps.dashboard.communications.apps.CommunicationsDashboardConfig',
    'oscar.apps.dashboard.shipping.apps.ShippingDashboardConfig',

    # 3rd-party apps that oscar depends on
    'widget_tweaks',
    'haystack',
    'treebeard',
    'sorl.thumbnail',   # Default thumbnail backend, can be replaced
    'django_tables2',
]

SITE_ID = 1
```
update `MIDDLEWARE` and Add `AUTHENTICATION_BACKENDS`:
```
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
]

AUTHENTICATION_BACKENDS = (
    'oscar.apps.customer.auth_backends.EmailBackend',
    'django.contrib.auth.backends.ModelBackend',
)
```
#### Configure `settings.py` and `urls.py`[ Search backend ]
If you’re happy with basic search for now, you can just add Haystack’s simple backend to the HAYSTACK_CONNECTIONS option in your Django settings:
```
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.simple_backend.SimpleEngine',
    },
}
```
Oscar uses Haystack to abstract away from different search backends.Your Haystack config could look something like this:
```
HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
        'URL': 'http://127.0.0.1:8983/solr',
        'INCLUDE_SPELLING': True,
    },
}
```
Oscar includes a sample schema to get started with Solr. More information can be found in the recipe on getting Solr up and running.
https://django-oscar.readthedocs.io/en/latest/howto/how_to_setup_solr.html

#### Configure `settings.py` and `urls.py`[ Database ]
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'ATOMIC_REQUESTS': True,
    }
}
```
#### Configure `settings.py` and `urls.py`[ URLs ]
edit `myoscarproject/urls.py`:
```
from django.apps import apps
from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),

    # The Django admin is not officially supported; expect breakage.
    # Nonetheless, it's often useful for debugging.

    path('admin/', admin.site.urls),

    path('', include(apps.get_app_config('oscar').urls[0])),
]
```

RUN:
```
python manage.py migrate
python manage.py runserver
```
Test The Website:
```
python manage.py runserver
```

#### Creating “boutique” app
RUN:
```
python manage.py startapp boutique
```
edit `settings.py`:
```


INSTALLED_APPS = [
    ...

    'boutique.apps.BoutiqueConfig',
]
```
edit `urls.py`:
```
from django.apps import apps
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),

    path('admin/', admin.site.urls),

    # path('dashboard/boutique/', apps.get_app_config('boutique_dashboard').urls),
    path('boutique/', apps.get_app_config('boutique').urls),
    path('', include(apps.get_app_config('oscar').urls[0])),

]
```
+ until Oscar's dashboard app is forked comment out `boutique_dashboard`.

#### Models for “boutique” app
edit `boutique/models.py`:
```

from django.db import models

class Boutique(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    manager = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
            app_label = 'boutique'
```
RUN:
```
python manage.py makemigrations
python manage.py migrate
```
edit `boutique/apps.py`:
```
from oscar.core.application import OscarConfig
from django.urls import path, re_path
from oscar.core.loading import get_class

class BoutiqueConfig(OscarConfig):
    name = 'boutique'
    namespace = 'boutique'
    
    def ready(self):
            super().ready()
            self.boutique_list_view = get_class('boutique.views', 'BoutiqueListView')
            self.boutique_detail_view = get_class('boutique.views', 'BoutiqueDetailView')
    def get_urls(self):
            urls = super().get_urls()
            urls += [
                path('', self.boutique_list_view.as_view(), name='index'),
                re_path(r'^view/(?P<pk>\d+)/$',self.boutique_detail_view.as_view(), name='details'),
            ]
            return self.post_process_urls(urls)
```
edit `boutique/admin.py`:
```
from django.contrib import admin
from oscar.core.loading import get_model

Boutique = get_model('boutique', 'Boutique')

class BoutiqueAdmin(admin.ModelAdmin):
    pass

admin.site.register(Boutique, BoutiqueAdmin)
```
create <mark>superuser</mark>
```
python manage.py createsuperuser
```
edit `boutique/views.py`:
```
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
```
#### Front-end templates for “boutique” views
edit `settings.py`:
```

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # Add this one
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        ...
    },
]
```
+ create `templates` under `src` directory
+ inside `templates` create `oscar/partials/nav_primary.html`
edit `nav_primary.html`:
```
{% extends "oscar/partials/nav_primary.html" %}
{% load i18n %}
{% block nav_items %}
{{ block.super }}
<li class="nav-item dropdown">
    <a class="nav-link" href="#" role="button">
    {% trans "Boutiques" %}
    </a>
</li>
{% endblock %}
```
RUN:
```
python manage.py runserver
```
Restart the server and You should see something on browser
<br>

create `templates/boutique/boutique_list.html`:
```

{% extends "oscar/layout.html" %}
{% load i18n %}
{% load product_tags %}
{% block title %}
{% trans "Boutiques" %} | {{ block.super }}
{% endblock %}
{% block breadcrumbs %}
    <nav aria-label="breadcrumb">
        <ol class="breadcrumb">
            <li class="breadcrumb-item">
                <a href="{{ homepage_url }}">{% trans "Home" %}</a>
            </li>
            <li class="breadcrumb-item active" aria-current="page">{% trans "Boutiques" %}</li>
        </ol>
    </nav>
{% endblock %}
{% block headertext %}
    {% trans "Boutique" %}
{% endblock %}
{% block content %}
    {% if not boutique_list %}
        <p>{% trans "There are no boutique at the moment." %}</p>
    {% else %}
        {% for boutique in boutique_list %}
        <p>
          <h2><a href="{% url 'boutique:details' boutique.pk %}">{{ boutique.name }}</a></h2>
          The boutique is in: {{ boutique.city }}
        </p> <hr/>
        {% endfor %}
    {% endif %}
{% endblock content %}
```
You should have to see something new in browser
<br>

create `/src/templates/boutique/boutique_details.html`:
```

{% extends "oscar/layout.html" %}
{% load i18n %}
{% load product_tags %}
{% block title %}
{% trans "Boutiques" %} | {{ block.super }}
{% endblock %}
{% block breadcrumbs %}
    <nav aria-label="breadcrumb">
        <ol class="breadcrumb">
            <li class="breadcrumb-item">
                <a href="{{ homepage_url }}">{% trans "Home" %}</a>
            </li>
            <li class="breadcrumb-item" aria-current="page">
              <a href="{% url 'boutique:index' %}">{% trans "Boutiques" %}</a>
            </li>
            <li class="breadcrumb-item active" aria-current="page">{{ boutique.name }}</li>
        </ol>
    </nav>
{% endblock %}
{% block headertext %}
    {% trans "Boutique" %}
{% endblock %}
{% block content %}
    <p>
      <h2>{{ boutique.name }}</h2> <br>
      The boutique is in: {{ boutique.city }} <br>
      The boutique's manager is Mr/Mrs: <strong>{{ boutique.manager }} </strong>
    </p>
{% endblock content %}
```
create directory called `boutique/dashboard` 
```
mkdir boutique/dashboard
```
RUN:
```
python manage.py startapp dashboard boutique/dashboard
```
edit `settings.py`:
```
INSTALLED_APPS = [
    ...

    'boutique.apps.BoutiqueConfig',
    # Add this one
    'boutique.dashboard.apps.DashboardConfig',
]
```
edit `myoscarproject/urls.py`:
+ comment out the `boutique_dashboard`
```
urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),

    path('admin/', admin.site.urls),

    # Comment Out
    path('dashboard/boutique/', apps.get_app_config('boutique_dashboard').urls),
    path('boutique/', apps.get_app_config('boutique').urls),
    path('', include(apps.get_app_config('oscar').urls[0])),

]
```
edit `boutique/dashboard/apps.py`:
```
from django.urls import path
from oscar.core.application import OscarDashboardConfig
from oscar.core.loading import get_class

class DashboardConfig(OscarDashboardConfig):
    name = 'boutique.dashboard'
    label = 'boutique_dashboard'
    namespace = 'boutique-dashboard'
    default_permissions = ['is_staff']

    def ready(self):
        self.boutique_list_view = get_class('boutique.dashboard.views', 'DashboardBoutiqueListView')
        self.boutique_create_view = get_class('boutique.dashboard.views', 'DashboardBoutiqueCreateView')
        self.boutique_update_view = get_class('boutique.dashboard.views', 'DashboardBoutiqueUpdateView')
        self.boutique_delete_view = get_class('boutique.dashboard.views', 'DashboardBoutiqueDeleteView')

    def get_urls(self):
        urls = [
            path('', self.boutique_list_view.as_view(), name='boutique-list'),
            path('create/', self.boutique_create_view.as_view(),name='boutique-create'),
            path('update/<int:pk>/', self.boutique_update_view.as_view(),name='boutique-update'),
            path('delete/<int:pk>/', self.boutique_delete_view.as_view(),name='boutique-delete'),
        ]
        return self.post_process_urls(urls)
```
create `forms.py` inside `boutique/dashboard`
edit `forms.py`:
```
from django import forms
from django.db.models import Q
from django.utils.translation import gettext_lazy as _
from oscar.core.loading import get_model

Boutique = get_model('boutique', 'Boutique')

class DashboardBoutiqueSearchForm(forms.Form):
    name = forms.CharField(label=_('Boutique name'), required=False)
    city = forms.CharField(label=_('City'), required=False)

    def is_empty(self):
        d = getattr(self, 'cleaned_data', {})
        def empty(key): return not d.get(key, None)
        return empty('name') and empty('city')
    
    def apply_city_filter(self, qs, value):
        words = value.replace(',', ' ').split()
        q = [Q(city__icontains=word) for word in words]
        return qs.filter(*q)
    
    def apply_name_filter(self, qs, value):
        return qs.filter(name__icontains=value)
    
    def apply_filters(self, qs):
        for key, value in self.cleaned_data.items():
            if value:
                qs = getattr(self, 'apply_%s_filter' % key)(qs, value)
        return qs
    
class DashboardBoutiqueCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Boutique
        fields = ('name', 'manager', 'city')
```

edit `boutique/dashboard/views.py`:
```
from django.contrib import messages
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.utils.translation import gettext
from django.utils.translation import gettext_lazy as _
from django.views import generic
from oscar.core.loading import get_class, get_model

Boutique = get_model('boutique', 'Boutique')
BoutiqueCreateUpdateForm = get_class('boutique.dashboard.forms', 'DashboardBoutiqueCreateUpdateForm')
DashboardBoutiqueSearchForm = get_class('boutique.dashboard.forms', 'DashboardBoutiqueSearchForm')
```
#### Listing Boutique instances in the dashboard
edit `views.py`:
```
...

class DashboardBoutiqueListView(generic.ListView):
    model = Boutique
    template_name = "dashboard/boutique/boutique_list.html"
    context_object_name = "boutique_list"
    paginate_by = 20
    filterform_class = DashboardBoutiqueSearchForm

    def get_title(self):
        data = getattr(self.filterform, 'cleaned_data', {})
        name = data.get('name', None)
        city = data.get('city', None)
        if name and not city:
            return gettext('Boutiques matching "%s"') % (name)
        elif name and city:
            return gettext('Boutiques matching "%s" near "%s"') % (name, city)
        elif city:
            return gettext('Boutiques near "%s"') % (city)
        else:
            return gettext('Boutiques')
        
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['filterform'] = self.filterform
        data['queryset_description'] = self.get_title()
        return data
    
    def get_queryset(self):
        qs = self.model.objects.all()
        self.filterform = self.filterform_class(self.request.GET)
        if self.filterform.is_valid():
            qs = self.filterform.apply_filters(qs)
        return qs
```
Creating Boutique instances in the dashboard
edit `views.py`:
```
...

class DashboardBoutiqueCreateView(generic.CreateView):
    model = Boutique
    template_name = 'dashboard/boutique/boutique_update.html'
    form_class = BoutiqueCreateUpdateForm
    success_url = reverse_lazy('boutique-dashboard:boutique-list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = _('Create new boutique')
        return ctx
    
    def forms_invalid(self, form, inlines):
        messages.error(
            self.request,
            "Your submitted data was not valid - please correct the below errors")
        return super().forms_invalid(form, inlines)
    
    def forms_valid(self, form, inlines):
        response = super().forms_valid(form, inlines)
        msg = render_to_string('dashboard/boutique/messages/boutique_saved.html',
                               {'boutique': self.object})
        messages.success(self.request, msg, extra_tags='safe')
        return response

```
Updating Boutique instances in the dashboard
edit `vies.py`:
```
...

class DashboardBoutiqueUpdateView(generic.UpdateView):
    model = Boutique
    template_name = "dashboard/boutique/boutique_update.html"
    form_class = BoutiqueCreateUpdateForm
    success_url = reverse_lazy('boutique-dashboard:boutique-list')

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['title'] = self.object.name
        return ctx
    
    def forms_invalid(self, form, inlines):
        messages.error(
            self.request,
            "Your submitted data was not valid - please correct the below errors")
        return super().forms_invalid(form, inlines)
    
    def forms_valid(self, form, inlines):
        msg = render_to_string('dashboard/boutique/messages/boutique_saved.html',
                               {'boutique': self.object})
        messages.success(self.request, msg, extrforms_valida_tags='safe')
        return super().forms_valid(form, inlines)
```
Deleting Boutique instances from the dashboard
edit `views.py`:
```
...

class DashboardBoutiqueDeleteView(generic.DeleteView):
    model = Boutique
    template_name = "dashboard/boutique/boutique_delete.html"
    success_url = reverse_lazy('boutique-dashboard:boutique-list')
```

#### Templates for the Boutique’s dashboard app

You can access the codes from above repo:
+ Template for list view: /dashboard/boutique/boutique_list.html
+ Template for update view: /dashboard/boutique/boutique_update.html
+ Template for delete view: /dashboard/boutique/boutique_delete.html
+ Message template: /dashboard/boutique/messages/boutique_saved.html

Adding “Boutiques” navigation item to Django-Oscar’s dashboard
```
from django.utils.translation import gettext_lazy as _
... # Django's Other Settings
from oscar.defaults import *
OSCAR_DASHBOARD_NAVIGATION.append({
    'label': _('Boutiques'),
    'icon': 'fas fa-store',
    'url_name': 'boutique-dashboard:boutique-list',
})
```

Author:
+ Matyas Sina Adugna
+ matyassinaadugna@gmail.com
+ Software Engineer

Reference:
https://hackernoon.com/a-guide-on-building-a-django-oscar-application-with-a-dashboard-bb1533at