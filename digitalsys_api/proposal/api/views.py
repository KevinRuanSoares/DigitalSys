from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from proposal.models import ProposalField
from proposal.api.serializer import ProposalSerializer, ProposalFieldValueSerializer, ProposalFieldSerializer
from proposal.services.proposal_service import ProposalService
from proposal.tasks import proposal_evaluation_task

class ProposalViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    
    def create(self, request):
        proposal_field_value_serializer = ProposalFieldValueSerializer(many=True, data=request.data)
        if proposal_field_value_serializer.is_valid(raise_exception=True):
            proposal = ProposalService().create_proposal(proposal_field_value_serializer.validated_data)
            proposal_evaluation_task.delay(str(proposal.unique_id))
            return Response(
                ProposalSerializer(proposal).data
            )

class ProposalFieldViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = ProposalFieldSerializer
    queryset = ProposalField.objects.filter(deleted=False).order_by('order')