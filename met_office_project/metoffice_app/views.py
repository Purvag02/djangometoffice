import requests

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# Define the Swagger schema for query parameters
query_param3 = openapi.Parameter('order', openapi.IN_QUERY, description='Order', type=openapi.TYPE_STRING)
query_param = openapi.Parameter('region', openapi.IN_QUERY, description='Region', type=openapi.TYPE_STRING)
query_param2 = openapi.Parameter('parameter', openapi.IN_QUERY, description='Parameter', type=openapi.TYPE_STRING)

@swagger_auto_schema(method='get', manual_parameters=[query_param, query_param2, query_param3])
@api_view(['GET'])
def get_metoffice_data(request):
    # Get parameters from the request query parameters
    mode = request.query_params.get('order', 'ranked')  # Default to 'ranked' if not provided
    region = request.query_params.get('region', '')
    parameter = request.query_params.get('parameter', '')
    
    valid_modes = ['date', 'ranked']
    if mode not in valid_modes:
        return Response({'error': 'Invalid mode'}, status=status.HTTP_400_BAD_REQUEST)

    # Validate region and parameter values (customize as needed)
    valid_regions = ['UK', 'England', 'Wales', 'Scotland', 'Northern_Ireland', 'England_and_Wales', 'England_N', 'England_S', 'Scotland_N', 'Scotland_E', 'Scotland_W', 'England_E_and_NE', 'Midlands', 'East_Anglia', 'England_NW_and_N_Wales', 'England_SW_and_S_Wales', 'England_SE_and_Central_S']
    valid_parameters = ['Max Temp', 'Min Temp', 'Mean Temp', 'Rainfall', 'Sunshine', 'Days of air frost', 'Raindays1mm']

    if region not in valid_regions or parameter not in valid_parameters:
        return Response({'error': 'Invalid region or parameter'}, status=status.HTTP_400_BAD_REQUEST)

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
        return Response({'data': data})
    except requests.exceptions.RequestException as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
