# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div


app = Flask(__name__)

# @app.route("/test")
# def test():
#     """ handle request to test server connectivity"""
#     return (f"""test worked""")

@app.route("/")
def root():
    return "root page"

@app.route("/add")
def additon():
    """ handle request to add a and b returns sum of a and b"""
    a = request.args["a"]
    b = request.args["b"]
    a = int(a)
    b = int(b)
    ans =  add(a, b)
    return str(ans)

@app.route("/sub")
def subtract():
    """ handle request to subtract b from a returns difference of a and b"""
    a = request.args["a"]
    b = request.args["b"]
    a = int(a)
    b= int(b)
    ans = sub(a, b)
    return  str(ans)
    
@app.route("/mult")
def multiply():
    """ handle request to multiply a and b returns product of a and b"""
    a = request.args["a"]
    b = request.args["b"]
    a = int(a)
    b= int(b)
    ans = mult(a, b)
    return str(ans)
 
@app.route("/div")
def divide():
    """ handle request to add a and b returns sum of a and b"""
    a = request.args["a"]
    b = request.args["b"]
    a = int(a)
    b= int(b)
    ans = div(a , b)
    return str(ans)

# SOLUTION COPY PASTE
operators = {
        "add": add,
        "sub": sub,
        "mult": mult,
        "div": div,
        }

@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = operators[oper](a, b)

    return str(result)
# FIRST ATTEMPT app.route ==>> /math/<operation> NON WORKING
# @app.route("/math/<operation>")
# def all_math(operation):
#     """ handle request to perform math operation on query string"""
#     a = request.args["a"]
#     b = request.args["b"]
#     a = int(a)
#     b= int(b)
#     operation = request.args["operation"]
#     return operation(a, b)