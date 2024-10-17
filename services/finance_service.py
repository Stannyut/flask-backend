# services/finance_service.py

from models import FinanceReport
from database import db

def get_all_finance_reports():
    return FinanceReport.query.all()

def create_finance_report(data):
    new_report = FinanceReport(
        total_sales=data.get('total_sales', 0.0),
        expenses=data.get('expenses', 0.0),
        profits=data.get('profits', 0.0),
        report_date=data.get('report_date')
    )
    db.session.add(new_report)
    db.session.commit()
    return new_report