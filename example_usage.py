from client import TwoHundredPointVehicleInspectionTransparentPricingClient

def main():
    client = TwoHundredPointVehicleInspectionTransparentPricingClient()
    res = client.generate_spinny_assured_report('KA05MC9900', 31000)
    print('Certificate: ' + res['inspection_certificate_id'] + ' for ' + res['car_reg'])
    print('No-Haggle Price: INR ' + str(res['fixed_no_haggle_price_inr']) + ' (Inspected: ' + str(res['points_inspected']) + ' points)')
    print('Assurance: ' + str(res['money_back_guarantee_days']) + '-day return, Home test drive: ' + str(res['free_home_test_drive_available']))

if __name__ == '__main__':
    main()
