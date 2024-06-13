@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    ### IMPORTANT ###
    ### ADDING A TABLE TO FINANCES VIA THIS SQL COMMAND:
    #CREATE TABLE transactions (
        #transaction_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        #transaction_type TEXT, user_id INTEGER,
        #symbol TEXT, quantity INTEGER, price NUMERIC, total_price NUMERIC,
        #year INTEGER, month INTEGER, day INTEGER,
        #hour INTEGER, minute INTEGER, second INTEGER,
        #FOREIGN KEY(user_id) REFERENCES users(id)
    #);
    #"""Buy shares of stock"""
    if request.method == "POST":
        # Grab user-input
        symbol = request.form.get("symbol")
        numberOfShares = request.form.get("shares")

        # Check user-input - symbol exists and is a valid stock symbol, number of stocks to purhcase is positive integer
        if symbol == "":
            return render_template("buy.html", error="Error: Please enter a Stock Symbol."), 400
        symbol = lookup(symbol)
        if (not symbol) or (symbol is None):
            return render_template("buy.html", error="Stock Symbol Not Found"), 400
        # fairly sure both of the things in brackets are biconditionals,
        # meaning they always have equivalent truth values...
        numberOfShares = str(numberOfShares)

        if numberOfShares.isnumeric() == False:
            return render_template("buy.html", error="Invalid Number"), 400
        numberOfShares = int(numberOfShares)
        if numberOfShares < 1:
            return render_template("buy.html", error="Invalid Number"), 400
        # Done checking user-input
        # That is, we've confirmed that the user-entered a valid stock-symbol, and a positive integer of shares to purchase

        # Grab client information
        client_id = session["user_id"]
        client_name = db.execute("SELECT username FROM users WHERE id = ?", client_id)
        client_name = client_name[0]['username']
        client_cash = db.execute("SELECT cash FROM users WHERE id = ?", client_id)
        client_cash = float(client_cash[0]['cash'])

        # Grabbing variables we need for the "transactions" table
        # transaction_type TEXT, user_id INTEGER,
        transaction_type = "buy"
        user_id = session["user_id"]

        # SYMBOL text, quantity INTEGER, price NUMERIC, total_price NUMERIC,
        symbol_text = symbol["symbol"]
        quantity = int(numberOfShares)
        symbol_price = float(symbol["price"])
        total_price = symbol_price * numberOfShares

        ## Let's compare some things before we continue
        if total_price > client_cash:
            return render_template("buy.html", error="Insufficient funds."), 400
        new_client_cash = client_cash - total_price
        #db.execute("UPDATE users SET cash = ? WHERE id = client_id", new_cash)
        # Let's save all the SQL statements for the very end

        current_owned = db.execute("SELECT amount_owned FROM stock_symbols WHERE user_id = ? AND symbol = ?", user_id, symbol_text)
        if len(current_owned) == 0:
            # this means there's no match for this user/symbol combination in our database!
            current_owned = 0
            db.execute("INSERT INTO stock_symbols (symbol, user_id, amount_owned) VALUES(?, ?, ?)", symbol_text, user_id, current_owned)
        else:
            current_owned = current_owned[0]["amount_owned"]
        newAmount_owned = current_owned + quantity

        # db.execute("UPDATE users SET cash = ? WHERE id = client_id", new_cash)
        # Grab the rest of the variables we need
        # source for time&date functions: https://www.sqlite.org/lang_datefunc.html
        # year INTEGER, month INTEGER, day INTEGER,
        current_date = db.execute("SELECT date('now')") # date('now')
        current_date = current_date[0]["date('now')"]
        # The current date is: 2024-04-24
        #######################0123456789
        year = int(current_date[0] + current_date[1] + current_date[2] + current_date[3])
        month = int(current_date[5] + current_date[6])
        day = int(current_date[8] + current_date[9])

        # hour INTEGER, minutes INTEGER, seconds INTEGER,
        current_time = db.execute("SELECT time('now')")
        current_time = current_time[0]["time('now')"]
        # The current time is: 22:50:44
        #######################01234567
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
                   symbol_text, quantity, symbol_price, total_price,
                   year, month, day, hour, minute, second
                   )
        # instructions: Upon completion, redirect the user to the home page.
        return redirect("/")
    else:
        return render_template("buy.html")
