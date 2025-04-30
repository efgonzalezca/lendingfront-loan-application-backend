from flask import Blueprint, jsonify

loan_bp = Blueprint('loan', __name__)

@loan_bp.route('', methods=['POST'])
def apply_loan():
    return jsonify({'status': 'ok'})