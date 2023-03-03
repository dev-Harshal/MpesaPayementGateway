# import requests

# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# @api_view(['POST'])
# def make_payment(request):
#     # Get the payment details from the request data
#     amount = request.data.get('amount')
#     phone_number = request.data.get('phone_number')
#     # Other necessary payment details can be added here

#     # Build the payment request headers
#     api_key = 'your_api_key'
#     api_secret = 'your_api_secret'
#     headers = {
#         'Content-Type': 'application/json',
#         'Authorization': f'Bearer {api_key}:{api_secret}'
#     }

#     # Build the payment request payload
#     payload = {
#         'BusinessShortCode': 'your_short_code',
#         'Password': 'your_password',
#         'Timestamp': 'your_timestamp',
#         'TransactionType': 'CustomerPayBillOnline',
#         'Amount': amount,
#         'PartyA': phone_number,
#         'PartyB': 'your_short_code',
#         'PhoneNumber': phone_number,
#         'CallBackURL': 'your_callback_url',
#         'AccountReference': 'your_account_reference',
#         'TransactionDesc': 'your_transaction_description'
#     }

#     # Send the payment request
#     url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'
#     response = requests.post(url, headers=headers, json=payload)

#     # Handle the response
#     if response.status_code == 200:
#         # Payment was successful
#         transaction_id = response.json().get('CheckoutRequestID')
#         return Response({'message': f'Payment successful. Transaction ID: {transaction_id}'})
#     else:
#         # Payment failed
#         error_message = response.json().get('errorMessage')
#         return Response({'error': f'Payment failed. Error message: {error_message}'})
