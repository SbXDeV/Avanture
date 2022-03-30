from ckeditor.widgets import CKEditorWidget
from django.contrib import admin
from django import forms
from Index.models import ModelBackForm, IndexPhone, IndexMenu, IndexHowToWork, IndexCases, ArticleImage,\
    IndexFAQ, IndexReview, UserAccept, Police


class ArticleImageInline(admin.TabularInline):
    model = ArticleImage


class PostAdminForm(forms.ModelForm):
    content_left = forms.CharField(label="Особенности", widget=CKEditorWidget())
    content_center = forms.CharField(label="Задачи", widget=CKEditorWidget())
    content_footer = forms.CharField(label="Решения", widget=CKEditorWidget())
    content_footer2 = forms.CharField(label="Результат", widget=CKEditorWidget())

    class Meta:
        model = IndexCases
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    inlines = [
        ArticleImageInline,
    ]


admin.site.register(IndexCases, PostAdmin)

admin.site.register(IndexMenu)
admin.site.register(IndexPhone)
admin.site.register(UserAccept)
admin.site.register(Police)
admin.site.register(IndexFAQ)
admin.site.register(IndexReview)
admin.site.register(IndexHowToWork)
admin.site.register(ModelBackForm)
