from flask import Flask, request, jsonify
from collections import defaultdict, deque
from datetime import datetime

app = Flask(__name__)

# Store transactions and balances
transactions = deque()
balances = defaultdict(int)

@app.route('/add', methods=['POST'])
def add_points():
    """
    Add points for a specific payer. 

    Expects a JSON payload with 'payer', 'points', and 'timestamp'.
    Updates the transactions and balances accordingly.
    """
    data = request.get_json()
    payer = data['payer']
    points = data['points']

    # Convert ISO 8601 timestamp to a datetime object
    timestamp = datetime.fromisoformat(data['timestamp'].replace('Z', '+00:00'))
    
    # Append the transaction details to the transactions deque
    transactions.append({'payer': payer, 'points': points, 'timestamp': timestamp})

    # Update the payer's balance
    balances[payer] += points
    
    return '', 200

@app.route('/spend', methods=['POST'])
def spend_points():
    """
    Spend points from one or more payers.

    Expects a JSON payload with 'points' to spend.
    Updates the transactions and balances accordingly.
    """
    data = request.get_json()
    points_to_spend = data['points']
    
    if sum(balances.values()) < points_to_spend:
        return 'Not enough points', 400
    
    spent_points = defaultdict(int)
    
    # Sort the transactions by timestamp
    transactions_sorted = sorted(transactions, key=lambda x: x['timestamp'])
    
    # Iterate over the sorted transactions
    for transaction in transactions_sorted:
        if points_to_spend <= 0:
            break
        
        # Get the payer and points for this transaction
        payer = transaction['payer']
        points = transaction['points']
        
        # If the points for this transaction are negative, skip it
        if points <= 0:
            continue
        
        # Calculate the spend for this transaction
        spend = min(points, points_to_spend)
        
        # Update the transaction and balances
        transaction['points'] -= spend
        points_to_spend -= spend
        spent_points[payer] -= spend
        balances[payer] -= spend
    
    # Return the spent points
    return jsonify([{'payer': payer, 'points': points} for payer, points in spent_points.items()]), 200

@app.route('/balance', methods=['GET'])
def get_balance():
    """
    Get the current balance for all payers.

    Returns a JSON object with the payer and their balance.
    """
    # Return the balances as a JSON object
    return jsonify(balances), 200

if __name__ == '__main__':
    app.run(port=8000)