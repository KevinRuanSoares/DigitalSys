from django.urls import path
from proposal.api.views import ProposalViewSet, ProposalFieldViewSet

_READ_ONLY = {"get": "list"}
_ONLY_POST = {"post": "create"}

urlpatterns = [
    path("", ProposalViewSet.as_view(_ONLY_POST), name="proposals"),
    path("fields", ProposalFieldViewSet.as_view(_READ_ONLY), name="proposal-fields")
]
