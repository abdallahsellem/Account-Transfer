from decimal import Decimal
import uuid
from django.shortcuts import get_object_or_404, render
from django.urls import NoReverseMatch
from rest_framework.views import APIView
from .models import Account
from rest_framework import status
from rest_framework.response import Response
import pandas as pd
from .serializers import AccountSerializer
from django.db import transaction
# Create your views here.


class ImportAccounts(APIView):
     def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        
        #check if we receive the file correctly 
        if not file:
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Read the CSV file using pandas
        df = pd.read_csv(file)
        

        # Iterate over the DataFrame rows
        for _, row in df.iterrows():
            customer_id = uuid.UUID(row['ID'])
            name = row['Name']
            balance = float(row['Balance'])

            account, created = Account.objects.get_or_create(
                id=customer_id,
                defaults={'owner_name': name, 'balance': balance},
            )
            account.save()
            
            #change account values if it already exist 
            if not created:
                account.owner_name = name
                account.balance = balance
                account.save()

        
        return Response({"message": "Accounts Imported successfully"},status=status.HTTP_201_CREATED)
    
    
    
    
class AccountsListView(APIView):
    def get(self, request, format=None):
        customers = Account.objects.all()
        serializer = AccountSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    
    

class AccountDetailView(APIView):
    def get(self, request, account_id, format=None):
        try:
            account_uuid = account_id
            customer = Account.objects.get(id=account_uuid)
            serializer = AccountSerializer(customer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Account.DoesNotExist:
            return Response({"error": "Customer not found"}, status=status.HTTP_404_NOT_FOUND)

        
        
            
        
class TransferFundsView(APIView):
    def post(self, request, *args, **kwargs):
        request_data = request.data 
        try:
            sender = get_object_or_404(Account, id=request_data["sender_id"])
            receiver = get_object_or_404(Account, id=request_data["receiver_id"])
            
            if sender.balance < request_data['amount']:
                return Response({'error': 'Insufficient funds'}, status=status.HTTP_400_BAD_REQUEST)
            
            with transaction.atomic():
                sender.balance -= Decimal(request_data.get("amount"))
                receiver.balance += Decimal(request_data.get("amount"))
                sender.save()
                receiver.save()
                       
            return Response({"message": "Transfer completed successfully"}, status=status.HTTP_200_OK)
        
        except KeyError:
            return Response({'error': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


            