import markdown

from django.db import models
from django.core.urlresolvers import reverse

from ckeditor.fields import RichTextField

from jmbo.models import ModelBase


class ContentBlock(ModelBase):
    autosave_fields = ("markdown",)

    markdown = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Content Block"
        verbose_name_plural = "Content Blocks"

    @property
    def content(self):
        if not self.markdown:
            return ""
        return markdown.markdown(self.markdown)
