from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secret123"

# Sample food data (like menu)
menu = [
    {"id": 1, "name": "Pizza", "price": 250},
    {"id": 2, "name": "Burger", "price": 120},
    {"id": 3, "name": "Pasta", "price": 180},
    {"id": 4, "name": "Biryani", "price": 220}
]

@app.route('/')
def home():
    return render_template('index.html', menu=menu)

@app.route('/add/<int:item_id>')
def add_to_cart(item_id):
    if "cart" not in session:
        session["cart"] = []

    for item in menu:
        if item["id"] == item_id:
            session["cart"].append(item)

    session.modified = True
    return redirect('/cart')

@app.route('/cart')
def cart():
    cart = session.get("cart", [])
    total = sum(item["price"] for item in cart)
    return render_template('cart.html', cart=cart, total=total)

@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        name = request.form.get("name")
        address = request.form.get("address")
        session.pop("cart", None)
        return render_template('order.html', success=True, name=name)
    return render_template('order.html', success=False)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
