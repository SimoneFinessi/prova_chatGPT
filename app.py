from flask import Flask, render_template, request
import pandas as pd
import matplotlib.pyplot as plt
import os
app = Flask(__name__)

df = pd.read_excel("https://github.com/wtitze/3E/raw/main/BikeStores.xls", sheet_name="products")
@app.route('/')
def home():
    return render_template("home.html")

# Esercizio 1
@app.route('/category_products')
def category_products():
    category_id = int(request.args.get('category_id'))
    category_df = df[df['category_id'] == category_id].sort_values('product_name')
    return render_template('risultato.html', risultato=category_df)

# Esercizio 2
@app.route('/price_range_products')
def price_range_products():
    min_price = float(request.args.get('min_price'))
    max_price = float(request.args.get('max_price'))
    price_range_df = df[(df['list_price'] >= min_price) & (df['list_price'] <= max_price)].sort_values('list_price', ascending=False)
    return render_template('risultato.html', risultato=price_range_df)

# Esercizio 3
@app.route('/name_contains_products')
def name_contains_products():
    name_contains = request.args.get('name_contains')
    name_contains_df = df[df['product_name'].str.contains(name_contains, case=False)].sort_values('product_name')
    return render_template('risultato.html', risultato=name_contains_df)

# Esercizio 4
@app.route('/category_counts')
def category_counts():
    category_counts_df = df.groupby('category_id')['product_id'].count()
    return render_template('risultato.html', risultato=category_counts_df)

# Esercizio 5
@app.route('/category_counts_chart')
def category_counts_chart():
    category_counts_df = df.groupby('category_id')['product_id'].count()
    plt.bar(category_counts_df.index, category_counts_df.values)
    plt.xlabel('Category ID')
    plt.ylabel('Product Count')
    plt.title('Product Count by Category')
    dir = "static/images"
    file_name = "graf.png"
    save_path = os.path.join(dir, file_name)
    plt.savefig(save_path, dpi = 150)
    return render_template('grafico.html')

if __name__ == '__main__':
    app.run(debug=True)