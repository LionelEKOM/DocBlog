from django import forms
from blogModels.models import BlogPost

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        #Pour exclure certains champs
        #exclude = ('title',)
        fields = [
            "category",
            "title",
            "author",
            "date",
            "description",
        ]
        labels = {
            "title" : "Titre",
            "category" : "Categories"
        }
        
        widgets = {
            "date": forms.SelectDateWidget(years=range(1990, 2050))
        }