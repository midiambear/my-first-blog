from pydoc import text
from re import I
from django.conf import settings
from django.db import models
from django.utils import timezone
#from markdownx.models import MarkdownxField

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default= timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
    #def get_markdown_text_as_html(self):
        #"""MarkDown記法で書かれたtextをHTML形式に変換して返す"""
        #return markdown(self.text)
