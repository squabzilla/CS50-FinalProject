#########################################################################################
### below: copied login_required function from: CS50 Week 9 C$50 Finance app.py (that was provided to us by CS50)

def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/latest/patterns/viewdecorators/
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function
### above: copied login_required function from: CS50 Week 9 C$50 Finance app.py (that was provided to us by CS50)
#########################################################################################