import random
from proposal.models import Proposal, ProposalFieldValue


class ProposalService:
    
    @staticmethod
    def create_proposal(validated_data):
        proposal = Proposal()
        proposal_field_values = []
        for proposal_field_value in validated_data:
            proposal_field_values.append(
                ProposalFieldValue(
                    proposal=proposal,
                    **proposal_field_value
                )
            )
        proposal.save()
        created_proposal_field_values = ProposalFieldValue.objects.bulk_create(proposal_field_values)
        proposal.proposal_field_values = created_proposal_field_values
        return proposal

    @staticmethod
    def proposal_evaluation(proposal: Proposal):
        status = ['DENIED', 'APPROVED']
        proposal.status = status[random.randrange(2)]
        proposal.save()