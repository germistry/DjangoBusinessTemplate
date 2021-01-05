#from django import forms
#from .models import Service, Post, Project, Tag, Category

#class SearchForm(forms.Form):
#    q = forms.CharField(label='eg. rewiring')
#    c = forms.ModelChoiceField(
#        queryset=Category.categories.order_by('category'))

#    def __init__(self, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        self.fields['c'].required = False
#        self.fields['q'].widget.attrs['placeholder'] = 'eg. rewiring'


#from django.contrib.auth.forms import AuthenticationForm
#from django.utils.translation import ugettext_lazy as _

#class BootstrapAuthenticationForm(AuthenticationForm):
#    """Authentication form which uses boostrap CSS."""
#    username = forms.CharField(max_length=254,
#                               widget=forms.TextInput({
#                                   'class': 'form-control',
#                                   'placeholder': 'User name'}))
#    password = forms.CharField(label=_("Password"),
#                               widget=forms.PasswordInput({
#                                   'class': 'form-control',
#                                   'placeholder':'Password'}))
