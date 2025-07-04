from django.forms import ClearableFileInput
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')  # default: "Clear" 
    initial_text = _('Current Image')
    input_text = _('Change Image')
    template_name = (
        'products/custom_widget_templates/custom_clearable_file_input.html'
    )         