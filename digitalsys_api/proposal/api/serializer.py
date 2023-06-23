from rest_framework import serializers
from proposal.models import Proposal, ProposalFieldValue, ProposalField


class ProposalFieldSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProposalField
        fields = ["unique_id", "name", "required", "field_type"]


class ProposalFieldValueSerializer(serializers.ModelSerializer):
    proposal_field = serializers.SlugRelatedField(slug_field='unique_id', queryset=ProposalField.objects.filter(deleted=False), allow_null=False, required=True)

    class Meta:
        model = ProposalFieldValue
        fields = ["proposal_field", "value"]
        
class ProposalSerializer(serializers.ModelSerializer):
    proposal_field_values = ProposalFieldValueSerializer(many=True, read_only=True)
    
    class Meta:
        model = Proposal
        fields = ["status", "unique_id", "proposal_field_values"]

