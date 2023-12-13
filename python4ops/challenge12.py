import requests

# Prompt user for destination URL
url = input("Enter the destination URL: ")

# Prompt user to select HTTP method
http_method = input("Select HTTP Method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ").upper()

# Print the entire request to be sent
print(f"\nSending {http_method} request to: {url}")

# Confirm before proceeding
confirmation = input("Do you want to proceed? (yes/no): ").lower()

if confirmation == 'yes':
    # Perform request using requests library
    response = requests.request(http_method, url)

    # Translate status code to plain terms
    status_code = response.status_code
    if status_code == 200:
        status_message = "OK"
    elif status_code == 404:
        status_message = "Not Found"
    else:
        status_message = "Unknown Status"

    # Print status information
    print(f"\nStatus Code: {status_code} - {status_message}")

    # Print response header information
    print("\nResponse Headers:")
    for header, value in response.headers.items():
        print(f"{header}: {value}")
else:
    print("Request aborted.")
