flight_data = {
    'meta': {
        'count': 10,
        'links': {
            'self': 'https://test.api.amadeus.com/v2/shopping/flight-offers?originLocationCode=LON&destinationLocationCode=YYZ&departureDate=2024-09-19&returnDate=2025-03-17&nonStop=true&adults=1&currencyCode=GBP&max=10'
        }
    },
    'data': [
        {
            'type': 'flight-offer',
            'id': '1',
            'source': 'GDS',
            'instantTicketingRequired': False,
            'nonHomogeneous': False,
            'oneWay': False,
            'isUpsellOffer': False,
            'lastTicketingDate': '2024-09-18',
            'numberOfBookableSeats': 9,
            'itineraries': [
                {
                    'duration': 'PT7H55M',
                    'segments': [
                        {
                            'departure': {
                                'iataCode': 'LGW',
                                'terminal': 'N',
                                'at': '2024-09-19T10:05:00'
                            },
                            'arrival': {
                                'iataCode': 'YYZ',
                                'terminal': '3',
                                'at': '2024-09-19T13:00:00'
                            },
                            'carrierCode': 'TS',
                            'number': '283',
                            'aircraft': {
                                'code': '332'
                            },
                            'operating': {
                                'carrierCode': 'TS'
                            },
                            'duration': 'PT7H55M',
                            'id': '6',
                            'numberOfStops': 0,
                            'blacklistedInEU': False
                        }
                    ]
                },
                {
                    'duration': 'PT7H10M',
                    'segments': [
                        {
                            'departure': {
                                'iataCode': 'YYZ',
                                'terminal': '3',
                                'at': '2025-03-17T22:35:00'
                            },
                            'arrival': {
                                'iataCode': 'LGW',
                                'terminal': 'N',
                                'at': '2025-03-18T09:45:00'
                            },
                            'carrierCode': 'TS',
                            'number': '122',
                            'aircraft': {
                                'code': '32Q'
                            },
                            'operating': {
                                'carrierCode': 'TS'
                            },
                            'duration': 'PT7H10M',
                            'id': '11',
                            'numberOfStops': 0,
                            'blacklistedInEU': False
                        }
                    ]
                }
            ],
            'price': {
                'currency': 'GBP',
                'total': '390.88',
                'base': '41.00',
                'fees': [
                    {'amount': '0.00', 'type': 'SUPPLIER'},
                    {'amount': '0.00', 'type': 'TICKETING'}
                ],
                'grandTotal': '390.88',
                'additionalServices': [
                    {'amount': '101.40', 'type': 'CHECKED_BAGS'}
                ],
                'pricingOptions': {
                    'fareType': ['PUBLISHED'],
                    'includedCheckedBagsOnly': False
                },
                'validatingAirlineCodes': ['TS'],
                'travelerPricings': [
                    {
                        'travelerId': '1',
                        'fareOption': 'STANDARD',
                        'travelerType': 'ADULT',
                        'price': {
                            'currency': 'GBP',
                            'total': '390.88',
                            'base': '41.00'
                        },
                        'fareDetailsBySegment': [
                            {
                                'segmentId': '6',
                                'cabin': 'ECONOMY',
                                'fareBasis': 'Q0BGT3E',
                                'brandedFare': 'BGT',
                                'brandedFareLabel': 'ECO BUDGET',
                                'class': 'Q',
                                'includedCheckedBags': {'quantity': 0},
                                'amenities': [
                                    {'description': 'UPTO50LB 23KG AND62LI 158LCM', 'isChargeable': True, 'amenityType': 'BAGGAGE', 'amenityProvider': {'name': 'BrandedFare'}},
                                    {'description': 'CARRY ON HAND BAGGAGE', 'isChargeable': False, 'amenityType': 'BAGGAGE', 'amenityProvider': {'name': 'BrandedFare'}},
                                    {'description': 'PRE RESERVED SEAT ASSIGNMENT', 'isChargeable': True, 'amenityType': 'PRE_RESERVED_SEAT', 'amenityProvider': {'name': 'BrandedFare'}},
                                    {'description': 'COMPLEMENTARY MEAL', 'isChargeable': False, 'amenityType': 'MEAL', 'amenityProvider': {'name': 'BrandedFare'}},
                                    {'description': 'BASIC SEAT', 'isChargeable': True, 'amenityType': 'BRANDED_FARES', 'amenityProvider': {'name': 'BrandedFare'}}
                                ]
                            },
                            {
                                'segmentId': '11',
                                'cabin': 'ECONOMY',
                                'fareBasis': 'Q0BGT3E',
                                'brandedFare': 'BGT',
                                'brandedFareLabel': 'ECO BUDGET',
                                'class': 'Q',
                                'includedCheckedBags': {'quantity': 0},
                                'amenities': [
                                    {'description': 'UPTO50LB 23KG AND62LI 158LCM', 'isChargeable': True, 'amenityType': 'BAGGAGE', 'amenityProvider': {'name': 'BrandedFare'}},
                                    {'description': 'CARRY ON HAND BAGGAGE', 'isChargeable': False, 'amenityType': 'BAGGAGE', 'amenityProvider': {'name': 'BrandedFare'}},
                                    {'description': 'PRE RESERVED SEAT ASSIGNMENT', 'isChargeable': True, 'amenityType': 'PRE_RESERVED_SEAT', 'amenityProvider': {'name': 'BrandedFare'}},
                                    {'description': 'COMPLEMENTARY MEAL', 'isChargeable': False, 'amenityType': 'MEAL', 'amenityProvider': {'name': 'BrandedFare'}},
                                    {'description': 'BASIC SEAT', 'isChargeable': True, 'amenityType': 'BRANDED_FARES', 'amenityProvider': {'name': 'BrandedFare'}}
                                ]
                            }
                        ]
                    }
                ]
            }
        }
    ]
}
