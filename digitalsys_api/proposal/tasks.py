from celery import shared_task
from proposal.models import Proposal
from proposal.services.proposal_service import ProposalService

@shared_task
def proposal_evaluation_task(proposal_id: str):
    proposal = Proposal.objects.get(unique_id=proposal_id)
    ProposalService().proposal_evaluation(proposal)