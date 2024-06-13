import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd, usd_to_variables, month_number_and_text

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Complete the implementation of index in such a way that it displays an HTML table summarizing, (for the user currently logged in):
# which stocks the user owns, the numbers of shares owned, the current price of each stock, and the total value of each holding (i.e., shares times price).
# Also display the user’s current cash balance along with a grand total (i.e., stocks’ total value plus cash).


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # Let's get client information
    client_id = session["user_id"]
    client_name = db.execute(
        "SELECT username FROM users WHERE id = ?", client_id)
    client_name = client_name[0]['username']
    client_cash = db.execute(
        "SELECT cash FROM users WHERE id = ?", client_id)
    client_cash = client_cash[0]['cash']

    # Let's make sure this is a number:
    client_cash = float(client_cash)

    # Let's get the stocks they own
    symbols = db.execute(
        "SELECT symbol, amount_owned FROM stock_symbols WHERE user_id = ?", client_id)
    symbols_list_dict = []
    client_net_worth = client_cash
    for symbol in symbols:
        # Remember: dictionary_name[key] = value
        value_symbol = symbol['symbol']  # grabs the value of the symbol
        value_amount = int(symbol['amount_owned'])  # grabs the amount of this stock owned
        value_price = lookup(value_symbol)
        value_price = float(value_price['price'])
        value_total_price = value_amount * value_price
        client_net_worth += value_total_price
        dictionary_line = {'symbol': value_symbol, 'amount': value_amount,
                           'price': value_price, 'totalPrice': value_total_price}
        symbols_list_dict.append(dictionary_line)
    return render_template("index.html", client=client_name, client_cash=client_cash, client_net_worth=client_net_worth, symbols=symbols_list_dict)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        # Grab user-input
        symbol = request.form.get("symbol")
        buy_quantity = request.form.get("shares")

        # Check user-input: symbol exists and is a valid stock symbol\
        # Whoops, I gotta use the apology function
        if symbol == "":
            # return render_template("buy.html", error="Error: Please enter a Stock Symbol."), 400
            return apology("Error: Please enter a stock symbol")
        symbol = lookup(symbol)
        if (not symbol) or (symbol is None):
            # return render_template("buy.html", error="Stock Symbol Not Found"), 400
            return apology("Error: Stock Symbol Not found")
        # fairly sure both of the things in brackets are biconditionals, meaning they always have equivalent truth values...
        buy_quantity = str(buy_quantity)

        # Check user-input: number of stocks to purchase is a positive integer
        if buy_quantity.isnumeric() == False:
            # return render_template("buy.html", error="Invalid Number of Shares"), 400
            return apology("Error: Invalid number of shares")
        buy_quantity = int(buy_quantity)
        if buy_quantity < 1:
            # return render_template("buy.html", error="Invalid Number of Shares"), 400
            return apology("Error: Invalid number of shares")
        # Done checking user-input - That is, we've confirmed a valid stock-symbol, and a positive integer of shares to purchase

        # Grab client information
        client_id = session["user_id"]
        client_name = db.execute("SELECT username FROM users WHERE id = ?", client_id)
        client_name = client_name[0]['username']
        client_cash = db.execute("SELECT cash FROM users WHERE id = ?", client_id)
        client_cash = float(client_cash[0]['cash'])

        # Grabbing variables we need for the "transactions" table:
        # transaction_type TEXT, user_id INTEGER,
        transaction_type = "buy"
        user_id = client_id
        # Yes this is redundant, no I don't care.

        # Grabbing variables we need for the "transactions" table
        # SYMBOL text, quantity INTEGER, price NUMERIC, total_price NUMERIC,
        symbol_text = symbol["symbol"]
        buy_quantity = int(buy_quantity)
        symbol_price = float(symbol["price"])
        total_price = symbol_price * buy_quantity

        # We can now compare the total price to the clients total funds.
        # Also, need to use apology function
        if total_price > client_cash:
            # return render_template("buy.html", error="Insufficient funds."), 400
            return apology("Error: Insufficient funds")
        new_client_cash = client_cash - total_price

        # We will be updating the quantity of stocks of this type that the client owns
        # But first, we need to ensure that a table for this kind of stock exists in the database.
        current_owned = db.execute(
            "SELECT amount_owned FROM stock_symbols WHERE user_id = ? AND symbol = ?", user_id, symbol_text)
        if len(current_owned) == 0:
            # this means there's no match for this user/symbol combination in our database!
            current_owned = 0
            db.execute("INSERT INTO stock_symbols (symbol, user_id, amount_owned) VALUES(?, ?, ?)",
                       symbol_text, user_id, current_owned)
        else:
            current_owned = current_owned[0]["amount_owned"]
        newAmount_owned = current_owned + buy_quantity

        # Grabbing date-time variables:
        # source for time&date functions: https://www.sqlite.org/lang_datefunc.html
        # year INTEGER, month INTEGER, day INTEGER,
        current_date = db.execute("SELECT date('now')")  # date('now')
        current_date = current_date[0]["date('now')"]
        # The current date is: 2024-04-24
        # #####################0123456789
        year = int(current_date[0] + current_date[1] + current_date[2] + current_date[3])
        month = int(current_date[5] + current_date[6])
        day = int(current_date[8] + current_date[9])

        # hour INTEGER, minutes INTEGER, seconds INTEGER,
        current_time = db.execute("SELECT time('now')")
        current_time = current_time[0]["time('now')"]
        # The current time is: 22:50:44
        # #####################01234567
        hour = int(current_time[0] + current_time[1])
        minute = int(current_time[3] + current_time[4])
        second = int(current_time[6] + current_time[7])

        db.execute("UPDATE users SET cash = ? WHERE id = ?", new_client_cash, client_id)
        db.execute("UPDATE stock_symbols SET amount_owned = ? WHERE user_id = ? AND symbol = ?",
                   newAmount_owned, user_id, symbol_text)
        db.execute("INSERT INTO transactions (\
                   transaction_type, user_id,\
                   symbol, quantity, price, total_price,\
                   year, month, day, hour, minute, second)\
                   VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   transaction_type, user_id,
                   symbol_text, buy_quantity, symbol_price, total_price,
                   year, month, day, hour, minute, second
                   )

        # instructions:
        # Upon completion, redirect the user to the home page.
        return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    # Let's grab list of transactions for this client
    client_id = session["user_id"]
    client_history = db.execute("SELECT * FROM transactions WHERE user_id = ?", client_id)

    # Let's also grab the client name
    client_name = db.execute("SELECT username FROM users WHERE id = ?", client_id)
    client_name = client_name[0]['username']

    for i in range(len(client_history)):
        # A function to chage the month format to NNAAA,
        # where NN is the month's number and AAA is 3 letter abbreviation
        month_int = client_history[i]['month']
        month = month_number_and_text(month_int)
        client_history[i]['month'] = month
        # I like my months to be REALLY obvious okay
    return render_template("history.html", client_name=client_name, client_history=client_history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
            # check_password_hash:
            # parameters:
            # pwhash (str) – The hashed password.
            # password (str) – The plaintext password.
            # boolean functions, returns TRUE or FALSE depending on whether or not they match
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    # Let's actually go over what the fuck a stock symbol IS:
    #
    # According to CS50 Duck Debugger:
    # A stock symbol, also known as a ticker symbol,
    # is a unique series of letters representing a particular publicly traded company's stock.
    # For example, the symbol for Apple is AAPL, and for Microsoft, it's MSFT.
    # In the context of the CS50 Finance problem, you'll be using these symbols to look up stock prices.
    #
    # How long is a stock symbol?
    # According to CS50 Duck Debugger:
    # A stock symbol typically consists of one to five letters.
    # The length can vary depending on the stock exchange.
    # For example, symbols on the New York Stock Exchange (NYSE) can be 1-3 letters long,
    # while those on the NASDAQ can be up to 5 letters long.

    if request.method == "POST":
        symbol = request.form.get("symbol")
        # The documentation doesn't specifically say we need an apology here for invalid input here,
        # but for consistency and matching CS50's Staff Solution, we'll do that

        # Check iin case symbol is blank or null-string
        if symbol == "":
            # return render_template("quote.html", error="Error: Please enter a Stock Symbol."), 400
            return apology("Error: Please enter a Stock Symbol")

        symbol = lookup(symbol)
        # Check that the lookup function didn't explode or something
        # Use apology if something breaks
        if not symbol:
            # return render_template("quote.html", error="Stock Symbol Not Found"), 400
            return apology("Error: Stock Symbol Not Found")
        if symbol is None:
            # return render_template("quote.html", error="Stock Symbol Not Found"), 400
            return apology("Error: Stock Symbol Not Found")
        # I am becoming VERY certain that these two lines do the same thing, are logically equivalent...
        return render_template("quoted.html", symbol=symbol)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":

        # Input validation: acquire input and validate that it exists:
        register_username = request.form.get("username")
        # Whoops, I gotta use the apology function
        if not register_username:
            # return render_template("register.html", error="No username entered."), 400
            return apology("Error: no username entered")
        register_password_1 = request.form.get("password")
        if not register_password_1:
            # return render_template("register.html", error="Password cannot be empty"), 400
            return apology("Error: password cannot be empty")
        register_password_2 = request.form.get("confirmation")
        if not register_password_2:
            # return render_template("register.html", error="Please confirm your password"), 400
            return apology("Error: need to confirm password")
        # In case we somehow have accepted blank input, reject that
        if register_username == "" or register_password_1 == "" or register_password_2 == "":
            # return render_template("register.html", error="Input cannot be blank.")
            return apology("Error: Input cannot be blank")

        # Check that username does not already exist
        existing_usernames = db.execute("SELECT username FROM users")
        for existing_username in existing_usernames:
            if register_username == existing_username['username']:
                # return render_template("register.html", error="Existing username."), 400
                return apology("Error: Username already exists")
        # Check that passwords match
        if register_password_1 != register_password_2:
            # return render_template("register.html", error="Passwords do not match."), 400
            return apology("Error: Passwords do not match")

        # Create password hash - now that we've checked that they match
        password_hash = generate_password_hash(register_password_1)
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)",
                   register_username, password_hash)
        # Make my username: William
        # Make my password: password
        # Yes, google keeps telling me this is insecure,
        # but for testing purposes for something never to be hosted on a real server, it works
        return render_template("login.html")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    # Grab client-id, I'll need it eventually
    client_id = session["user_id"]

    if request.method == "POST":
        # Grab user-input
        symbol = request.form.get("symbol")
        sell_quantity = request.form.get("shares")

        # Check user input 1: Check that symbol exists
        if symbol == "":
            # Whoops, I gotta use the apology function
            # return render_template("sell.html", error="Invalid Stock Symbol."), 400
            return apology("Error: Invalid Stock Symbol")
        symbol = lookup(symbol)
        if (not symbol) or (symbol is None):
            symbols_list = symbolsClientOwns()
            # return render_template("sell.html", error="Stock Symbol Not Found"), 400
            return apology("Error: Stock Symbol Not Found")
        # fairly sure both of the things in brackets are biconditionals,
        # meaning they always have equivalent truth values...
        symbol_text = symbol["symbol"]
        symbol_price = float(symbol["price"])
        # Anyways, now that we've confirmed that symbol exists, we also grabbed the name and price

        # Check user input 2: check that they own this stock
        current_quantity = db.execute("SELECT amount_owned FROM stock_symbols WHERE user_id = ? and symbol = ?",
                                      client_id, symbol_text)
        if len(current_quantity) == 0:
            # this means there's no match for this user/symbol combination in our database!
            # return render_template("sell.html", error="You don't own any of these shares."), 400
            return apology("Error: You don't own any shares of this type")
        # we confirm that the entry exists in the DB before this step, otherwise the following line might fail
        current_quantity = int(current_quantity[0]['amount_owned'])
        # extracting just the quantity here
        if current_quantity <= 0:
            # return render_template("sell.html", error="You don't own any of these shares."), 400
            return apology("Error: You don't own any shares of this type")

        # Check user input 3: Check that the sell quantity is valid
        sell_quantity = str(sell_quantity)
        if sell_quantity.isnumeric() == False:
            # return render_template("sell.html", error="Invalid Number"), 400
            return apology("Error: Invalid Number")
        # this confirms that it's a positive integer
        sell_quantity = int(sell_quantity)
        current_quantity = int(current_quantity)
        if sell_quantity < 1:
            # return render_template("sell.html", error="Cannot Sell 0 or Less Shares"), 400
            return apology("Error: Cannot sell 0 or less shares")
        if sell_quantity > current_quantity:
            # return render_template("sell.html", error="Sell Quantity Exceeds Owned Quantity"), 400
            return apology("Error: Sell Quantity Exceeds Owned Quantity")
        # Everything SHOULD be valid at this point, now to generate some values to enter in the database

        # Grab client information
        client_id = session["user_id"]
        client_name = db.execute("SELECT username FROM users WHERE id = ?", client_id)
        client_name = client_name[0]['username']
        client_cash = db.execute("SELECT cash FROM users WHERE id = ?", client_id)
        client_cash = float(client_cash[0]['cash'])
        # Yes some of this is redundant, but it makes it easier for me to wrap my head around

        # Grabbing variables we need for the "transactions" table
        # transaction_type TEXT, user_id INTEGER,
        transaction_type = "sell"
        user_id = session["user_id"]

        # SYMBOL text, quantity INTEGER, price NUMERIC, total_price NUMERIC,
        symbol_text = symbol["symbol"]
        sell_quantity = int(sell_quantity)  # reminder that this is here
        newAmount_owned = current_quantity - sell_quantity
        symbol_price = float(symbol["price"])
        total_price = symbol_price * sell_quantity
        new_client_cash = client_cash + total_price

        # Grab the rest of the variables we need - all the time variables
        # source for time&date functions: https://www.sqlite.org/lang_datefunc.html
        # year INTEGER, month INTEGER, day INTEGER,
        current_date = db.execute("SELECT date('now')")
        current_date = current_date[0]["date('now')"]
        # quotations were tricky here...
        # The current date is: 2024-04-24
        # #####################0123456789
        year = int(current_date[0] + current_date[1] + current_date[2] + current_date[3])
        month = int(current_date[5] + current_date[6])
        day = int(current_date[8] + current_date[9])

        # hour INTEGER, minutes INTEGER, seconds INTEGER,
        current_time = db.execute("SELECT time('now')")
        current_time = current_time[0]["time('now')"]
        # The current time is: 22:50:44
        # #####################01234567
        hour = int(current_time[0] + current_time[1])
        minute = int(current_time[3] + current_time[4])
        second = int(current_time[6] + current_time[7])

        dontUpdate = False
        if dontUpdate == True:
            return render_template("sell.html", error="We're not selling stuff quite yet."), 400

        db.execute("UPDATE users SET cash = ? WHERE id = ?", new_client_cash, client_id)
        db.execute("UPDATE stock_symbols SET amount_owned = ? WHERE user_id = ? AND symbol = ?",
                   newAmount_owned, user_id, symbol_text)
        db.execute("INSERT INTO transactions (\
                   transaction_type, user_id,\
                   symbol, quantity, price, total_price,\
                   year, month, day, hour, minute, second)\
                   VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                   transaction_type, user_id,
                   symbol_text, sell_quantity, symbol_price, total_price,
                   year, month, day, hour, minute, second
                   )  # Gah this is one hell of an SQL-statement

        # instructions: Upon completion, redirect the user to the home page.
        return redirect("/")
    else:
        return render_template("sell.html")


@app.route("/getPrice")
def getPrice():
    # Custom function to get the price of a stock.
    # To be called from a page on the web application.
    # Used to dynamically show the price of stocks we wish to sell
    return_price = []
    q = request.args.get("q")
    if q:
        price = lookup(q)
        price = ((price['price']))
        price = usd_to_variables(price)
        return_price.append(price)
    return jsonify(return_price)


@app.route("/getStockQuantity")
def getStockQuantity():
    # Custom function to get the quantity owned of a stock.
    # To be called from a page on the web application.
    # Used to dynamically show the quantity of stocks you can sell
    client_id = session["user_id"]
    return_number = []
    q = request.args.get("q")
    if q:
        quantity = db.execute(
            "SELECT amount_owned FROM stock_symbols WHERE user_id = ? and symbol = ?", client_id, q)
        quantity = quantity[0]['amount_owned']
        return_number.append(quantity)
    return jsonify(return_number)


@app.route("/getStocksOwned")
def symbolsClientOwns():
    # Custom function to a list of different stocks a client has.
    # To be called from a page on the web application.
    # Used to dynamically show quantity of stocks a user is considering selling.
    client_id = session["user_id"]
    symbols_list = []
    symbols = db.execute(
        "SELECT symbol, amount_owned FROM stock_symbols WHERE user_id = ? AND amount_owned > 0", client_id)
    for item in symbols:
        symbol = item['symbol']
        print(f"value of symbol is: {symbol}")
        symbols_list.append(symbol)
    print("we are in getStocksOwned, about to print the list")
    for item in symbols_list:
        print(item)
    return jsonify(symbols_list)
