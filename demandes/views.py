from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Demande
import json
from datetime import datetime

@csrf_exempt
def save_application(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Fonction pour parser les dates, en retournant None si la date est vide
            def parse_date(date_str):
                if date_str:
                    try:
                        return datetime.strptime(date_str, '%Y-%m-%d').date()
                    except ValueError:
                        return None
                return None

            # Créez l'instance Demande
            application = Demande.objects.create(
                first_name=data['contact'].get('firstName', ''),
                last_name=data['contact'].get('lastName', ''),
                email=data['contact'].get('email', ''),
                phone=data['contact'].get('phone', ''),
                address=data['contact'].get('address', ''),
                postal_code=data['contact'].get('postalCode', ''),
                city=data['contact'].get('city', ''),
                parking_address=data['contact'].get('parkingAddress', False),
                birth_date=parse_date(data['contact'].get('birthDate', '')),
                selected_option=data['objective'].get('selectedOption', ''),
                moto_option=data['objective'].get('motoOption', ''),
                annulation=data['objective'].get('annulation', False),
                purchase_date=parse_date(data['objective'].get('purchaseDate', '')),
                project_purchase=data['objective'].get('projectPurchase', False),
                vehicle_brand=data['vehicle'].get('vehicleBrand', ''),
                engine_capacity=data['vehicle'].get('engineCapacity', ''),
                model=data['vehicle'].get('model', ''),
                vehicle_type=data['vehicle'].get('type', ''),
                registration_number=data['vehicle'].get('registrationNumber', ''),
                first_registration_date=parse_date(data['vehicle'].get('firstRegistrationDate', '')),
                acquisition_date=parse_date(data['vehicle'].get('acquisitionDate', None)),  # Changez ici
                permis_a1=parse_date(data['permis'].get('permisA1', None)),  # Changez ici
                permis_a2=parse_date(data['permis'].get('permisA2', None)),  # Changez ici
                permis_a=parse_date(data['permis'].get('permisA', None)),  # Changez ici
                permis_b=parse_date(data['permis'].get('permisB', None)),  # Changez ici
                annulation_a1=data['permis'].get('annulationA1', False),
                annulation_a2=data['permis'].get('annulationA2', False),
                annulation_a=data['permis'].get('annulationA', False),
                annulation_b=data['permis'].get('annulationB', False),
                additional_info=data.get('confirmation', {}).get('additionalInfo', ''),
                comment=data.get('confirmation', {}).get('comment', ''),
            )

            return JsonResponse({'status': 'success', 'id': application.id})

        except json.JSONDecodeError:
            return JsonResponse({'status': 'fail', 'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'fail', 'error': str(e)}, status=500)

    return JsonResponse({'status': 'fail', 'error': 'Invalid request method'}, status=400)
