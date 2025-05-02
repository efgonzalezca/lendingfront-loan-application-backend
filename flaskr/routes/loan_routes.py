from flask import Blueprint, jsonify, request

from flaskr.services.loan_evaluation import evaluate_loan
from flaskr.middlewares.validator_handler import validate_schema

loan_bp = Blueprint('loan', __name__)

@loan_bp.route('/evaluate', methods=['POST'])
@validate_schema('loan_evaluation', request, validate_form=True)
def apply_loan():
    data = request.get_json()
    decision = evaluate_loan(data['amount'])
    return jsonify({
        'tax_id': data['tax_id'],
        'decision': decision,
        'amount': data['amount'],
        'name': data['name']
    }), 200