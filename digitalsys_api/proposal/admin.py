from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from proposal.models import Proposal, ProposalField
from proposal.forms import ProposalFieldForm

@admin.register(Proposal)
class Proposal(admin.ModelAdmin):
    list_display = ("unique_id", 'date_created', "status", "get_proposal_identifier")

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def get_proposal_identifier(self, obj):
        identifier = obj.proposal_proposal_field_value.filter(deleted=False).order_by('proposal_field__order').first()
        if identifier:
            return identifier.value
        return ''
    get_proposal_identifier.short_description = _('Proposal Identifier')

    def get_queryset(self, request):
        return super(Proposal, self).get_queryset(
            request).filter(deleted=False).order_by('-date_created')

@admin.register(ProposalField)
class ProposalField(admin.ModelAdmin):
    form = ProposalFieldForm
    list_display = ("unique_id", "name", "required", 'field_type', 'order')
    
    def get_queryset(self, request):
        return super(ProposalField, self).get_queryset(
            request).filter(deleted=False)
    
    def delete_model(self, request, obj):
        obj.deleted = True
        obj.save()