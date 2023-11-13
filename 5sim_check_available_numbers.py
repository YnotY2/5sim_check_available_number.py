import requests

class colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    END = '\033[0m'
    CYAN = '\033[96m'
    BLACK = '\033[30m'

# Specify the operator and service you would like to use:
operator_1 = 'virtual38'
operator_2 = 'virtual4'
country = 'germany'
service = 'openai'


def check_number_availability(operator_1, country, operator_2, service):

    headers = {
        'Accept': 'application/json',
    }

    response = requests.get('https://5sim.net/v1/guest/products/' + country + '/' + operator_1, headers=headers)
    print(f"{colors.BLUE}Currently requesting live available 'bolt' service numbers from 5SIM...")
    print(f"{colors.BLUE}Operator: {operator_1}{colors.END}")
    print(f"{colors.BLUE}Country: {country}{colors.END}")

    # Check if the API call was successful.
    if response.status_code == 200:
        print(f"{colors.RED}Successful API call!{colors.END}")
        
        # Access the service entry in the dictionary.
        data_dict = response.json()
        service_entry = data_dict.get(service)

        if service_entry:
            bolt_qty = service_entry.get("Qty")
            bolt_price = service_entry.get("Price")

            # Print the extracted values.
            print(f"{colors.RED}---------------------{colors.RED}")
            print(f"{colors.GREEN}Bolt Qty:           {bolt_qty}{colors.END}")
            print(f"{colors.GREEN}Bolt Price:         {bolt_price} (0,36$){colors.END}")
            if bolt_qty >= 1:
                sim_numbers_available = True
                return sim_numbers_available, operator_1
    else:
        print(f'no available numbers from; "{operator_1}"')
        response = requests.get('https://5sim.net/v1/guest/products/' + country + '/' + operator_2, headers=headers)
        print(f"{colors.BLUE}Currently requesting live available 'bolt' service numbers from 5SIM...")
        print(f"{colors.BLUE}Operator: {operator_2}{colors.END}")
        print(f"{colors.BLUE}Country: {country}{colors.END}")

        # Check if the API call was successful.
        if response.status_code == 200:
            print(f"{colors.RED}Successful API call!{colors.END}")

            # Define the service you want to extract from the response.
            service = 'openai'

            # Access the service entry in the dictionary.
            data_dict = response.json()
            service_entry = data_dict.get(service)

            if service_entry:
                bolt_qty = service_entry.get("Qty")
                bolt_price = service_entry.get("Price")

                # Print the extracted values.
                print(f"{colors.RED}---------------------{colors.RED}")
                print(f"{colors.GREEN}Bolt Qty:           {bolt_qty}{colors.END}")
                print(f"{colors.GREEN}Bolt Price:         {bolt_price} (0,36$){colors.END}")
                if bolt_qty >= 1:
                    sim_numbers_available = True
                    return sim_numbers_available, operator_2
        else:
            print(f'no available numbers from; "{operator_2} and "{operator_1}""')
            return False

# Call the function and store the result, this way the function only runs when called.
sim_numbers_available = check_number_availability(operator_1, country, operator_2)

if sim_numbers_available:
    for operator in sim_numbers_available:
        print(f"operator is available;    {colors.YELLOW}{operator}{colors.END}")
