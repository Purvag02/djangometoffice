from django.shortcuts import render
from django.http import HttpResponse
import requests
from django.shortcuts import render

def metoffice_data_ui(request):
    return render(request, 'metoffice_data_ui.html')

def get_metoffice_data(request):
    if request.method == 'GET':
        # Get parameters from the request query parameters
        mode = request.GET.get('order', 'ranked')  # Default to 'ranked' if not provided
        region = request.GET.get('region', '')
        parameter = request.GET.get('parameter', '')

        valid_modes = ['date', 'ranked']
        if mode not in valid_modes:
            return HttpResponse('Invalid mode', status=400)

        # Validate region and parameter values (customize as needed)
        valid_regions = ['UK', 'England', 'Wales', 'Scotland', 'Northern_Ireland', 'England_and_Wales', 'England_N', 'England_S', 'Scotland_N', 'Scotland_E', 'Scotland_W', 'England_E_and_NE', 'Midlands', 'East_Anglia', 'England_NW_and_N_Wales', 'England_SW_and_S_Wales', 'England_SE_and_Central_S']
        valid_parameters = ['Max Temp', 'Min Temp', 'Mean Temp', 'Rainfall', 'Sunshine', 'Days of air frost', 'Raindays1mm']

        if region not in valid_regions or parameter not in valid_parameters:
            return HttpResponse('Invalid region or parameter', status=400)

        # Map parameter values to the expected MetOffice API values
        parameter_mapping = {
            'Max Temp': 'Tmax',
            'Min Temp': 'Tmin',
            'Mean Temp': 'Tmean',
            'Rainfall': 'Rainfall',
            'Sunshine': 'Sunshine',
            'Days of air frost': 'AirFrost',
            'Raindays1mm': 'Raindays1mm'
        }

        # Construct the dynamic MetOffice API URL based on the selected mode
        if mode == 'date':
            metoffice_api_url = f"https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/{parameter_mapping.get(parameter)}/date/{region}.txt"
        elif mode == 'ranked':
            metoffice_api_url = f"https://www.metoffice.gov.uk/pub/data/weather/uk/climate/datasets/{parameter_mapping.get(parameter)}/ranked/{region}.txt"

        # Example: Make a request to the MetOffice API
        try:
            response = requests.get(metoffice_api_url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            data = response.text  # Use response.text to get the content
            return HttpResponse(data)
        except requests.exceptions.RequestException as e:
            return HttpResponse(str(e), status=500)
