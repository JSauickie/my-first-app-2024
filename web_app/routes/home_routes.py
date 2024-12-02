from flask import Blueprint, request, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    print("HOME...")
    return render_template("home.html")  # Serving the home page using a template

@home_routes.route("/about")
def about():
    print("ABOUT...")
    return render_template("about.html")  # Serving the about page using a template

@home_routes.route("/hello")
def hello_world():
    print("HELLO...")

    # Extract URL parameters
    url_params = dict(request.args)
    print("URL PARAMS:", url_params)

    # Use "name" parameter if provided, otherwise default to "World"
    name = url_params.get("name") or "World"
    message = f"Hello, {name}!"

    # Passing values to the template
    x = 5
    y = 20
    return render_template("hello.html", message=message, x=x, y=y)  # Use the template for hello page

