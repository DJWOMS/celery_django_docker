from django.views.generic import CreateView

from .models import Contact
from .forms import ContactForm
from .tasks import write_file


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = '/'
    template_name = 'main/contact.html'

    def form_valid(self, form):
        form.save()
        write_file.delay(form.instance.email)
        return super().form_valid(form)
