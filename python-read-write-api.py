import os
import requests
import json

access_token = 'PUT YOUR ACCESS TOKEN HERE WHEN RUNNING'
base_url = 'https://api.smartsheet.com/2.0'
sheet_id = '2685184902123396'

item_row_id = '2730481699213188'
quantity_row_id = '7234081326583684'
price_row_id = '1604581792370564'
isPurchased_row_id = '6108181419741060'


def get_sheet_by_id(sheet_id):
    # Specify the endpoint you want to call
    endpoint = f'/sheets/{sheet_id}'

    # Create the request URL by combining the base URL and endpoint
    url = base_url + endpoint

    # Create the headers for the API request
    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/json'
    }

    # Make the API request to get a list of sheets
    response = requests.get(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Convert the response to JSON
        data = response.json()
        row_count = len(data['rows'])
        for i in range(row_count):
            id = data['rows'][i]['id']
            name = data['rows'][i]['cells'][0]['value']
            quantity = data['rows'][i]['cells'][1]['value']
            price = data['rows'][i]['cells'][2]['value']
            is_purchased = data['rows'][i]['cells'][3]['value']
            print('|'.join((str(id), name, str(quantity), str(price), str(is_purchased))))
       

def add_row(item, quantity, price):

    # Specify the endpoint for creating rows in the sheet
    endpoint = f'/sheets/{sheet_id}/rows'

    # Create the request URL by combining the base URL and endpoint
    url = base_url + endpoint

    # Create the headers for the API request
    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/json'
    }

    # Specify the data for the new row
    new_row_data = {
        'toTop': True,  # Add the new row at the top of the sheet
        'cells': [
            {
                'columnId': item_row_id,
                'value': item
            },
            {
                'columnId': quantity_row_id,
                'value': str(quantity)
            },
            {
                'columnId': price_row_id,
                'value': str(price)
            },
            {
                'columnId': isPurchased_row_id,
                'value': 'No'
            }
        ]
    }

    # Convert the new row data to JSON
    payload = json.dumps(new_row_data)

    # Make the API request to create a new row
    response = requests.post(url, headers=headers, data=payload)

    # Check if the request was successful
    if response.status_code == 200:
        # Convert the response to JSON
        data = response.json()

        # Process the data as needed
        created_row_id = data['result']['id']
        print('New row created with ID:', created_row_id)
    else:
        print('Error:', response.status_code, response.text)
    
def update_row(row_id, item, quantity, price):

    # Specify the endpoint for creating rows in the sheet
    endpoint = f'/sheets/{sheet_id}/rows'

    # Create the request URL by combining the base URL and endpoint
    url = base_url + endpoint

    # Create the headers for the API request
    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/json'
    }

    # Specify the data for the row to update
    row_to_update = {
        "id": row_id,
        "cells": [
            {
                'columnId': item_row_id,
                'value': item
            },
            {
                'columnId': quantity_row_id,
                'value': str(quantity)
            },
            {
                'columnId': price_row_id,
                'value': str(price)
            },
            {
                'columnId': isPurchased_row_id,
                'value': 'No'
            }
        ]
    }

    # Convert the new row data to JSON
    payload = json.dumps(row_to_update)

    # Make the API request to create a new row
    response = requests.put(url, headers=headers, data=payload)

    # Check if the request was successful
    if response.status_code == 200:
        # Convert the response to JSON
        data = response.json()
    else:
        print('Error:', response.status_code, response.text)


def purchase(row_id):

    # Specify the endpoint for creating rows in the sheet
    endpoint = f'/sheets/{sheet_id}/rows'

    # Create the request URL by combining the base URL and endpoint
    url = base_url + endpoint

    # Create the headers for the API request
    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/json'
    }

    # Specify the data for the row to update
    row_to_update = {
        "id": row_id,
        "cells": [
            {
                'columnId': isPurchased_row_id,
                'value': 'Yes'
            }
        ]
    }

    # Convert the new row data to JSON
    payload = json.dumps(row_to_update)

    # Make the API request to create a new row
    response = requests.put(url, headers=headers, data=payload)

    # Check if the request was successful
    if response.status_code == 200:
        # Convert the response to JSON
        data = response.json()
    else:
        print('Error:', response.status_code, response.text)

def delete_row(row_id):
    
    # Specify the endpoint for creating rows in the sheet
    endpoint = f'/sheets/{sheet_id}/rows?ids={row_id}&ignoreRowsNotFound=true'

    # Create the request URL by combining the base URL and endpoint
    url = base_url + endpoint

    # Create the headers for the API request
    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/json'
    }

    # Make the API request to create a new row
    response = requests.delete(url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Convert the response to JSON
        data = response.json()
    else:
        print('Error:', response.status_code, response.text)


print("Starting ...")
# print(os.environ['SMARTSHEET_ACCESS_TOKEN'])
# print("Calling api ...")

# print('Adding a new row')
# add_row('Apple', 7, 18.0)

# print('Updating row')
# update_row(7725854567911300, 'Coffee', 1, 3.50)

# print('Purchasing an item}')
# purchase(7725854567911300)

print('Deleting an item')
delete_row(5851767600009092)

print('Getting Sheet')
get_sheet_by_id(2685184902123396)

print("Done")