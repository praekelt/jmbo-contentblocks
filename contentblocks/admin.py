from django.contrib import admin

from jmbo.admin import ModelBaseAdmin
from contentblocks.models import ContentBlock


admin.site.register(ContentBlock, ModelBaseAdmin)
