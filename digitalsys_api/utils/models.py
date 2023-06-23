import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _

class BaseModel(models.Model):
    unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, verbose_name=_('Unique Id'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation Date'))
    date_updated = models.DateTimeField(auto_now=True, verbose_name=_('Update Date'))
    deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
