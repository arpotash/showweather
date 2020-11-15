from django import forms

from mainapp.models import City


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'