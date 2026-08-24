class TwoHundredPointVehicleInspectionTransparentPricingClient:
    def generate_spinny_assured_report(self, car_reg_number='DL8CAA1234', odometer_reading_km=28000):
        return {
            'inspection_certificate_id': 'spn_cert_7721',
            'car_reg': car_reg_number,
            'odometer_verified_genuine': True,
            'points_inspected': 200,
            'fixed_no_haggle_price_inr': 645000.0,
            'money_back_guarantee_days': 5,
            'comprehensive_warranty_years': 1,
            'free_home_test_drive_available': True
        }
