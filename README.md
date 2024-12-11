# Points Management API

## Introduction
This project implements a REST API for managing points and point transactions. The API allows you to add points, spend points, and fetch the current point balance. The implementation is done using Python and Flask.

## Prerequisites
- Python 3.x
- `pip` (Python package installer)

## Setup Instructions

### 1. Install Python
If you don't have Python installed, download and install it from python.org.

### 2. Install Flask
Open your terminal or command prompt and run the following command to install Flask:
```sh
pip install Flask
```

### 3. Download the Project Files
Clone the repository from GitHub and navigate to the project directory:
```bash
git clone <your-repo-url>
cd <your-repo-directory>
```

### 4. Run the API
In your terminal or command prompt, navigate to the directory containing app.py and run the following command:
```bash
python app.py
```
The API will start running on http://localhost:8000.

## API Endpoints
### 1. Add Points
**Endpoint:** /add \
**Method:** POST \
**Description:** Adds points to a payer's balance. \
**Request Body:**
```json
{
  "payer": "DANNON",
  "points": 5000,
  "timestamp": "2020-11-02T14:00:00Z"
}
```
**Response:** Status code 200 if successful.

### 2. Spend Points
**Endpoint:** /spend \
**Method:** POST \
**Description:** Spends points from the user's balance. \
**Request Body:**
```json
{
  "points": 5000
}
```
**Response:** Status code 200 and a list of payer names and the number of points that were subtracted, or status code 400 if there are not enough points.

### 3. Get Balance
**Endpoint:** /balance \
**Method:** GET \
**Description:** Fetches the current balance of points per payer. \
**Response:**
```json
{
  "DANNON": 1000,
  "UNILEVER": 0,
  "MILLER COORS": 5300
}
```

## Testing the API
### Add Points
Use the following curl commands to add points:
```bash
curl -X POST http://localhost:8000/add -H "Content-Type: application/json" -d '{"payer": "DANNON", "points": 300, "timestamp": "2022-10-31T10:00:00Z"}'
curl -X POST http://localhost:8000/add -H "Content-Type: application/json" -d '{"payer": "UNILEVER", "points": 200, "timestamp": "2022-10-31T11:00:00Z"}'
curl -X POST http://localhost:8000/add -H "Content-Type: application/json" -d '{"payer": "DANNON", "points": -200, "timestamp": "2022-10-31T15:00:00Z"}'
curl -X POST http://localhost:8000/add -H "Content-Type: application/json" -d '{"payer": "MILLER COORS", "points": 10000, "timestamp": "2022-11-01T14:00:00Z"}'
curl -X POST http://localhost:8000/add -H "Content-Type: application/json" -d '{"payer": "DANNON", "points": 1000, "timestamp": "2022-11-02T14:00:00Z"}'
```

### Spend Points
Use the following curl command to spend points:
```bash
curl -X POST http://localhost:8000/spend -H "Content-Type: application/json" -d '{"points": 5000}'
```

### Get Balance
Use the following curl command to get the current balance:
```bash
curl http://localhost:8000/balance
```

## Wrapper Program
### menu.py
A separate program, menu.py, is provided to act as a wrapper for the curl commands. This program offers a menu for easier execution of the API endpoints.

Usage
- Ensure the API is running on http://localhost:8000.
- Run the menu.py script:
```bash
python menu.py
```
