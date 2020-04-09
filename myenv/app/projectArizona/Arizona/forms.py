from django import forms
from .models import Tag
"""пользовательский класс для создания удаления редактирования постов связывается с базой данных"""
class TagForm(forms.Form):
	title = forms.CharField(max_length=50)
	slug = forms.CharField(max_length=50)


	def save(self):
		new_tag = Tag.object.create(title=self.cleaned_data['title'],
			slug=self.cleaned_data['slug'])
		return new_tag