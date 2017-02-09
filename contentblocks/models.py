import markdown

from django.db import models
from django.core.urlresolvers import reverse

from jmbo.models import ModelBase
from .constants import infoblock_layouts
from simplemde.fields import SimpleMDEField


class ContentBlock(ModelBase):
    autosave_fields = ("markdown",)

    markdown = SimpleMDEField(null=True, blank=True)

    layout = models.CharField(
        max_length=50, default="plain",
        help_text="The layout of this block",
        choices=infoblock_layouts
        )

    extra_classes = models.CharField(
        max_length=150,
        blank=True,
        help_text="Extra css classes to apply to the block.\
            Separate with spaces.",
        )

    link = models.Foreignkey(
        "Link",
        models.SET_NULL,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Content Block"
        verbose_name_plural = "Content Blocks"

    @property
    def content(self):
        if not self.markdown:
            return ""
        return markdown.markdown(self.markdown)
