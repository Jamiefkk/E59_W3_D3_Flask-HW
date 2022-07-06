from flask import render_template
from app import app
from models.orders import total_orders

@app.route('/orders')
def index():
    return render_template('index.html', total_orders=total_orders)

@app.route('/orders/<int:order_index>')
def get_single_order(order_index):
    return render_template('order.html', order=total_orders[order_index])