# DjangoVueConnection/index_view/views.py

# Main view to load the index template
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
  """Loads index.html
  """
  def get_template_names(self):
      template_name = 'index.html'
      return template_name
