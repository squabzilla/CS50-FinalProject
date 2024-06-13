@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # Let's get client information
    client_id = session["user_id"]
    client_name = db.execute("SELECT username FROM users WHERE id = ?", client_id)
    client_name = client_name[0]['username']
    client_cash = db.execute("SELECT cash FROM users WHERE id = ?", client_id)
    client_cash = client_cash[0]['cash']

    # Let's make sure this is a number:
    client_cash = float(client_cash)

    # Let's get the stocks they own
    symbols = db.execute("SELECT symbol, amount_owned FROM stock_symbols WHERE user_id = ?", client_id)
    symbols_list_dict = []
    client_net_worth = client_cash
    #dictionary_line = 0
    for symbol in symbols:
        #dictionary_name[key] = value
        value_symbol = symbol['symbol'] #grabs the value of the symbol
        value_amount = int(symbol['amount_owned']) #grabs the amount of this stock owned
        value_price = lookup(value_symbol)
        value_price = float(value_price['price'])
        value_total_price = value_amount * value_price
        client_net_worth += value_total_price
        dictionary_line = {'symbol':value_symbol, 'amount':value_amount, 'price':value_price, 'totalPrice':value_total_price}
        symbols_list_dict.append(dictionary_line)
    # while there might be a better way to just add a dictionary value to each line of the symbols list,
    # if I do it this way I'm confident that it'll actually, you know, WORK

    current_time = db.execute("SELECT time('now')")
    current_time = current_time[0]["time('now')"]
    # The current time is: 22:50:44

    current_date = db.execute("SELECT date('now')") # date('now')
    current_date = current_date[0]["date('now')"]
    # The current date is: 2024-04-24

    #return render_template("index.html", client=client_name, client_cash=client_cash, date=current_date, time=current_time)
    #which stocks the user owns, the numbers of shares owned, the current price of each stock, and the total value of each holding (i.e., shares times price).
        # this is all in symbols_list_dict
    #Also display the user’s current cash balance along with a grand total (i.e., stocks’ total value plus cash).
        # client_cash, client_net_worth
    return render_template("index.html", client=client_name, client_cash=client_cash, client_net_worth=client_net_worth, symbols=symbols_list_dict)
    #return apology("SORRY. Stocks Portfolio: TODO")
