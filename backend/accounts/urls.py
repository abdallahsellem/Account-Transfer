from django.urls import path

from .views import ImportAccounts,AccountsListView,AccountDetailView,TransferFundsView

urlpatterns = [
    path("import-accounts", ImportAccounts.as_view(),name='imports-accounts'),
    path("accounts", AccountsListView.as_view(),name='accounts'),
    path("accounts/<uuid:account_id>/", AccountDetailView.as_view(), name='account-detail'),
    path('accounts/transfer/', TransferFundsView.as_view(), name='transfer_funds'),
]
