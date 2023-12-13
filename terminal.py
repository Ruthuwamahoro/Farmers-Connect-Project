import requests
from urllib.parse import quote

class FarmerTerminal:
    """
    The FarmerTerminal class represents the main interface for the Farmers Connect application.
    It includes methods for user authentication, accessing features, and interacting with external APIs.
    """

    def __init__(self):
        """
        Initializes the FarmerTerminal object with user credentials and marketplace products.
        """
        self.user_credentials = {}
        self.logged_in_user = None
        self.marketplace_products = []

    def display_welcome(self):
        """
        Displays the welcome menu for the Farmers Connect application.
        """
        print("Welcome to Farmers Connect!")
        print("1. Login")
        print("2. Signup")
        print("3. Help")
        print("4. Exit")

    def login(self):
        """
        Allows a user to log in by providing their username and password.
        """
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username in self.user_credentials and self.user_credentials[username] == password:
            self.logged_in_user = username
            print("Login successful. Welcome, {}!".format(username))
            return True
        else:
            print("Invalid credentials. Please try again.")
            return False

    def signup(self):
        """
        Allows a new user to sign up by choosing a username and password.
        """
        username = input("Choose a username: ")
        password = input("Choose a password: ")

        if username not in self.user_credentials:
            self.user_credentials[username] = password
            self.logged_in_user = username
            print("Signup successful. Welcome, {}!".format(username))
            return True
        else:
            print("Username already exists. Please choose a different one.")
            return False

    def help_menu(self):
        """
        Displays the help menu for Farmers Connect.
        """
        print("Farmers Connect Help:")
        print("- Login: If you already signed up, you can log in.")
        print("- Signup: New users can create an account.")
        print("- Exit: Close Farmers Connect.")

    def interact(self):
        """
        Manages the interaction with the Farmers Connect application.
        """
        while True:
            self.display_welcome()
            choice = input("Enter your choice: ")

            if choice == '1':
                if self.login():
                    self.access_features()
            elif choice == '2':
                if self.signup():
                    self.access_features()
            elif choice == '3':
                self.help_menu()
            elif choice == '4':
                print("Exiting Farmers Connect. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def marketplace(self):
        """
        Displays the marketplace features for the logged-in user.
        """
        print("\nMarketplace:")
        print("1. You have 500 Kilograms of maize on the market.")
        print("2. You have 300 Kilograms of rice on the market.")

    def expert_advice(self):
        """
        Provides expert advice to the user based on their input.
        """
        print("\nExpert Advice:")
        district = input("Enter your district: ")

        # Simulate a list of experts in the district (replace with real data)
        available_experts = ["Kaidatu", "Musa", "Hawa", "Aminata", "Alhaji"]

        print("Available Experts in {}: ".format(district))
        for i, expert in enumerate(available_experts, 1):
            print(f"{i}. {expert}")

        # Let the farmer choose an expert
        expert_choice = input("Choose an expert by number to message: ")

        try:
            expert_choice = int(expert_choice)
            if 1 <= expert_choice <= len(available_experts):
                chosen_expert = available_experts[expert_choice - 1]
                message = input("Write your message to {}:".format(chosen_expert))
                print("Message sent to {}. They will respond soon!".format(chosen_expert))
            else:
                print("Invalid expert choice. Please select a number from the available experts.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def weather_information(self):
        """
        Retrieves and displays weather information based on the user's input.
        """
        print("\nWeather Information:")

        city_name = input("Enter your city name: ")

        # Make a request to the MetaWeather API
        encoded_city_name = quote(city_name)
        endpoint = f"https://www.metaweather.com/api/location/search/?query={encoded_city_name}"

        response = requests.get(endpoint)

        try:
            response.raise_for_status()
            data = response.json()

            # Display weather information
            if data and isinstance(data, list) and 'woeid' in data[0]:
                woeid = data[0]['woeid']
                weather_endpoint = f"https://www.metaweather.com/api/location/{woeid}/"

                weather_response = requests.get(weather_endpoint)
                weather_data = weather_response.json()

                if weather_response.status_code == 200 and 'consolidated_weather' in weather_data:
                    temperature = weather_data['consolidated_weather'][0]['the_temp']
                    condition = weather_data['consolidated_weather'][0]['weather_state_name']

                    print("Current Weather:")
                    print(f"Temperature: {temperature:.2f}°C")
                    print(f"Condition: {condition}")
                else:
                    print("Error retrieving weather information. Please try again later.")
            else:
                print("City not found or error retrieving weather information. Please enter a valid city name.")

        except requests.exceptions.HTTPError as errh:
            print("HTTP Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)
        except requests.exceptions.RequestException as err:
            print("Something went wrong:", err)

    def access_features(self):
        """
        Manages access to additional features for the logged-in user.
        """
        print("\nWelcome to Farmers Connect! You now have access to additional features.")
        while True:
            print("\nWelcome, {}! Choose an option:".format(self.logged_in_user))
            print("1. Marketplace")
            print("2. Expert Advice")
            print("3. Weather Information")
            print("4. Logout")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.marketplace()
            elif choice == '2':
                self.expert_advice()
            elif choice == '3':
                self.weather_information()
            elif choice == '4':
                print("Logging out. Goodbye, {}!".format(self.logged_in_user))
                break
            else:
                print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    terminal = FarmerTerminal()
    terminal.interact()
