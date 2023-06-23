from django.db import models
from utils.models import BaseModel
from django.utils.translation import ugettext_lazy as _

STATUS_CHOICES = (
    ('APPROVED', _('Approved')),
    ('DENIED', _('Denied')),
    ('PENDING', _('Pending')),
)

TYPE_CHOICES = (
    ('NUMBER', _('Number')),
    ('TEXT', _('Text')),
    ('DATE', _('Date')),
)

class Proposal(BaseModel):
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='PENDING', verbose_name='Status')

    class Meta:
        db_table = 'proposals'
        verbose_name = _("Proposal")
        verbose_name_plural = _("Proposals")


class ProposalField(BaseModel):
    name = models.CharField(max_length=50, verbose_name=_('Name'))
    required = models.BooleanField(default=False, verbose_name=_('Required'))
    field_type = models.CharField(max_length=12, choices=TYPE_CHOICES, default='TEXT', verbose_name=_('Field Type'))
    order = models.PositiveIntegerField(default=0, verbose_name=_('Order'))

    class Meta:
        db_table = 'proposal_fields'
        verbose_name = _("Proposal Field")
        verbose_name_plural = _("Proposal Fields")


class ProposalFieldValue(BaseModel):
    proposal = models.ForeignKey(Proposal, on_delete=models.CASCADE, related_name='proposal_proposal_field_value')
    proposal_field = models.ForeignKey(ProposalField, on_delete=models.CASCADE, related_name='proposal_field_proposal_field_value')
    value = models.CharField(max_length=255)

    class Meta:
        db_table = 'proposal_field_values'