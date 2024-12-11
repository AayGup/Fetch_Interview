import requests
import json

class PointsAPI:
    """
    A class to interact with the Points API.

    Parameters
    ----------
    base_url : str
        The base URL of the Points API.
    """

    def __init__(self, base_url):
        """
        Initialize the PointsAPI object.

        Parameters
        ----------
        base_url : str
            The base URL of the Points API.
        """
        self.base_url = base_url

    def add_points(self, payer, points, timestamp):
        """
        Add points for a specific payer.

        Parameters
        ----------
        payer : str
            The name of the payer.
        points : int
            The number of points to add.
        timestamp : str
            The timestamp of the transaction in ISO 8601 format.

        Returns
        -------
        int
            The status code of the API response.
        """
        # Construct the URL for the add points API endpoint
        url = f"{self.base_url}/add"
        
        # Prepare the data payload for the POST request
        data = {
            "payer": payer,
            "points": points,
            "timestamp": timestamp
        }
        
        # Send the POST request to the API
        response = requests.post(url, json=data)
        
        # Return the status code of the response
        return response.status_code

    def spend_points(self, points):
        """
        Spend points from one or more payers.

        Parameters
        ----------
        points : int
            The number of points to spend.

        Returns
        -------
        tuple
            The status code of the API response and the JSON of the response
        """
        # Construct the URL for the spend points API endpoint
        url = f"{self.base_url}/spend"
        
        # Prepare the data payload for the POST request
        data = {"points": points}
        
        # Send the POST request to the API
        response = requests.post(url, json=data)
        
        # Return the status code and JSON of the response
        return response.status_code, response.json()

    def get_balance(self):
        """
        Get the current balance for all payers.

        Returns
        -------
        tuple
            The status code of the API response and the JSON of the response
        """
        # Construct the URL for the get balance API endpoint
        url = f"{self.base_url}/balance"
        
        # Send the GET request to the API
        response = requests.get(url)
        
        # Return the status code and JSON of the response
        return response.status_code, response.json()

if __name__ == "__main__":
    api = PointsAPI("http://localhost:8000")

    while True:
        print("\nChoose an action:")
        print("1. Add points")
        print("2. Spend points")
        print("3. Get balance")
        print("4. Exit")
        choice = input("Enter the number of your choice: ")

        if choice == '1':
            payer = input("Enter payer name: ")
            points = int(input("Enter points: "))
            timestamp = input("Enter timestamp (YYYY-MM-DDTHH:MM:SSZ): ")
            status = api.add_points(payer, points, timestamp)
            print()
            print(f"Add points status: {status}")

        elif choice == '2':
            points = int(input("Enter points to spend: "))
            status, spent_points = api.spend_points(points)
            print()
            print(f"Spend points status: {status}")
            if status == 200:
                print("Spent points:", spent_points)
            else:
                print("Error:", spent_points)

        elif choice == '3':
            status, balance = api.get_balance()
            print()
            print(f"Get balance status: {status}")
            print("Current balance:", balance)

        elif choice == '4':
            break

        else:
            print()
            print("Invalid choice. Please try again.")