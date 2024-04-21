from flask import Flask, request, render_template, send_file
from blackscholes import blackScholes
from math import log, sqrt, exp

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import io
import numpy as np
import os
import base64

app = Flask(__name__)

@app.route('/generate_plot', methods=['POST'])


def generate_plot():
    parameter = request.form['parameter']
    S = float(request.form['S_fixed']) if parameter != 'S' else 100  # Use reasonable defaults
    K = float(request.form['K_fixed']) if parameter != 'K' else 100
    T = float(request.form['T_fixed']) if parameter != 'T' else 1
    r = float(request.form['r_fixed']) if parameter != 'r' else 0.05
    sigma = float(request.form['sigma_fixed']) if parameter != 'sigma' else 0.2

    # Define ranges for the selected parameter
    if parameter == 'S':
        values = np.linspace(50, 150, 100)
        plt.figure(figsize=(10, 6))
        call_prices = [blackScholes(value, K, T, r, sigma, type='call') for value in values]
        put_prices = [blackScholes(value, K, T, r, sigma, type='put') for value in values]
        plt.plot(values, call_prices, label='Call Option Price')
        plt.plot(values, put_prices, label='Put Option Price')
        plt.xlabel('Stock Price (S)')
    elif parameter == 'K':
        values = np.linspace(80, 120, 100)
        plt.figure(figsize=(10, 6))
        call_prices = [blackScholes(S, value, T, r, sigma, type='call') for value in values]
        put_prices = [blackScholes(S, value, T, r, sigma, type='put') for value in values]
        plt.plot(values, call_prices, label='Call Option Price')
        plt.plot(values, put_prices, label='Put Option Price')
        plt.xlabel('Strike Price (K)')
    elif parameter == 'T':
        values = np.linspace(0.1, 2, 100)
        plt.figure(figsize=(10, 6))
        call_prices = [blackScholes(S, K, value, r, sigma, type='call') for value in values]
        put_prices = [blackScholes(S, K, value, r, sigma, type='put') for value in values]
        plt.plot(values, call_prices, label='Call Option Price')
        plt.plot(values, put_prices, label='Put Option Price')
        plt.xlabel('Time to Maturity (T)')
    elif parameter == 'r':
        values = np.linspace(0, 0.1, 100)
        plt.figure(figsize=(10, 6))
        call_prices = [blackScholes(S, K, T, value, sigma, type='call') for value in values]
        put_prices = [blackScholes(S, K, T, value, sigma, type='put') for value in values]
        plt.plot(values, call_prices, label='Call Option Price')
        plt.plot(values, put_prices, label='Put Option Price')
        plt.xlabel('Risk-Free Rate (r)')

    plt.ylabel('Option Price')
    plt.legend()
    plt.grid(True)

    plot_path = os.path.join('static', 'figure.png')
    plt.savefig(plot_path)
    plt.close()
    return plot_path






@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == "POST":
        S = float(request.form.get('S', 100))
        K = float(request.form.get('K', 100))
        T = float(request.form.get('T', 1))
        r = float(request.form.get('r', 0.05))
        sigma = float(request.form.get('sigma', 0.2))
        parameter = request.form.get('parameter', 'S')

        file_path = generate_plot(S, K, T, r, sigma, parameter)
    # Since the file is always named 'figure.png' and stored in '/static', it's easy to refer to it
        return render_template('results.html', image_path='/static/figure.png')
    else:

        return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)
