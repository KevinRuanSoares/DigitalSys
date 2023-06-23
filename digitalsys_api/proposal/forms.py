from django import forms
from proposal.models import ProposalField

class ProposalFieldForm(forms.ModelForm):

    class Meta:
        model = ProposalField
        fields = ["name", 'required', 'field_type', 'order']