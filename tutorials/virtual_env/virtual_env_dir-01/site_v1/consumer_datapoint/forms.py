from django.forms import ModelForm
from .models import DataPoint
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Submit

class DataPointForm(ModelForm):
    class Meta:
        model = DataPoint
        fields = ('datapoint','answer_type','options')
    #
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     self.helper = FormHelper
    #     self.helper.form_method = 'post'
    #     self.helper.layout = Layout(
    #         'datapoint',
    #         'answer_type',
    #         'options',
    #         Submit('submit','Submit')
    #     )
