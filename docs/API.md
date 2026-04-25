# API Documentation

This CRM project provides a RESTful API to manage leads and deals.

## Base URL
`http://127.0.0.1:8000/api/`

## Endpoints

### Leads
- **GET** `/leads/`: Retrieve a list of all leads.
- **POST** `/leads/`: Create a new lead.
  - **Request Body:**
    ```json
    {
      "name": "Customer Name",
      "email": "email@example.com",
      "source": "Website"
    }
    ```

### Deals
- **GET** `/deals/`: Retrieve a list of all deals.
- **POST** `/deals/`: Create a new deal.
  - **Request Body:**
    ```json
    {
      "title": "New Deal",
      "amount": 5000,
      "status": "New"
    }
    ```

## Authentication
Currently, the API is open for development purposes. In production, ensure you implement Token-based authentication.