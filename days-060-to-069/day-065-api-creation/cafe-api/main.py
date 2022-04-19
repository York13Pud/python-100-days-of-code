from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from markupsafe import escape
from random import randint

# --- Create the application:
app = Flask(__name__)

# By default, jsonify sorts the keys out before constructing the output. 
# Setting it to False will stop it sorting the keys.
app.config['JSON_SORT_KEYS'] = False

# --- Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# --- Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
    
# --- Define the root route:
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

# --- Define the route to return a query as a JSON response:

# --- Method 1 ---
# --- This method allows for the most flexibility in how the data is returned:
@app.route("/random1", methods=["GET"])
def random_cafe_m1():
    query_db = Cafe.query
    random_cafe_chosen = query_db.get(randint(1, query_db.count()))
    print(random_cafe_chosen.name)
    return jsonify(response={
        "id": random_cafe_chosen.id,
        "name": random_cafe_chosen.name,
        "map_url": random_cafe_chosen.map_url,
        "img_url": random_cafe_chosen.img_url,
        "location": random_cafe_chosen.location,
        
        #Put some properties in a sub-category
        "amenities": {
          "seats": random_cafe_chosen.seats,
          "has_toilet": random_cafe_chosen.has_toilet,
          "has_wifi": random_cafe_chosen.has_wifi,
          "has_sockets": random_cafe_chosen.has_sockets,
          "can_take_calls": random_cafe_chosen.can_take_calls,
          "coffee_price": random_cafe_chosen.coffee_price,
        }
    })

# --- Method 2 ---
# --- This method is quicker to construct but offers less flexibility:
@app.route("/random2", methods=["GET"])
def random_cafe_m2():
    query_db = Cafe.query
    random_cafe_chosen = query_db.get(randint(1, query_db.count()))
    print(random_cafe_chosen.name)
    params = {column.name: random_cafe_chosen.__getattribute__(column.name) for column in Cafe.__table__.columns}
    return jsonify(params), 200


# --- Return all the items in the table:
# --- Method 1: Full control of the data structure:
@app.route("/all1", methods=["GET"])
def all_cafes():
    all_cafes_query = db.session.query(Cafe).all()
    all_cafes_list = []
    for cafe in all_cafes_query:
        all_cafes_list.append({
        "id": cafe.id,
        "name": cafe.name,
        "map_url": cafe.map_url,
        "img_url": cafe.img_url,
        "location": cafe.location,
        
        #Put some properties in a sub-category
        "amenities": {
          "seats": cafe.seats,
          "has_toilet": cafe.has_toilet,
          "has_wifi": cafe.has_wifi,
          "has_sockets": cafe.has_sockets,
          "can_take_calls": cafe.can_take_calls,
          "coffee_price": cafe.coffee_price,
        }})
    all_cafes = {"cafes": all_cafes_list}
    return jsonify(all_cafes), 200


# --- Method 2: Shorter amount of code bu less control of the data structure:
@app.route("/all2", methods=["GET"])
def get_all_cafes():
    cafes = db.session.query(Cafe).all()
    #This uses a List Comprehension but you could also split it into 3 lines.
    return jsonify(cafes=[cafe.to_dict() for cafe in cafes]), 200

@app.route("/search", methods=["GET"])
def search_by_location():
    """This function will search the database for the location passed by the API call and return the results back
    in a JSON formatted response."""
    location_to_find = request.args.get("loc")
    search_db_query = Cafe.query.filter(Cafe.location.like(location_to_find)).all()
    all_cafes_list = []
    for cafe in search_db_query:
        all_cafes_list.append({
        "id": cafe.id,
        "name": cafe.name,
        "map_url": cafe.map_url,
        "img_url": cafe.img_url,
        "location": cafe.location,
        
        #Put some properties in a sub-category
        "amenities": {
          "seats": cafe.seats,
          "has_toilet": cafe.has_toilet,
          "has_wifi": cafe.has_wifi,
          "has_sockets": cafe.has_sockets,
          "can_take_calls": cafe.can_take_calls,
          "coffee_price": cafe.coffee_price,
        }})
    all_cafes = {"cafes": all_cafes_list}
    return jsonify(all_cafes), 200


@app.route("/add", methods=["POST"])
def add_record():
    try:
        add_cafe = Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("location"),
            seats=request.form.get("seats"),
            has_toilet=bool(request.form.get("has_toilets")),
            has_wifi=bool(request.form.get("has_wifi")),
            has_sockets=bool(request.form.get("has_sockets")),
            can_take_calls=bool(request.form.get("can_take_calls")),
            coffee_price=request.form.get("coffee_price")
        )
        db.session.add(add_cafe)
        db.session.commit()
        
    except Exception as error:
        return jsonify(response={"error": (str(error.orig))})
  
    return jsonify(response={"success": "Successfully added the new cafe."}), 200

@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    cafe_id_to_update = cafe_id
    
    try:
        update_coffee_price = db.session.query(Cafe).get(cafe_id_to_update)
        update_coffee_price.coffee_price = request.form.get("coffee_price")
        
        db.session.commit()
    
    except AttributeError as error:
        print("test")
        return jsonify(response={"error": "Record or field does not exist"}), 404
        
    except Exception as error:
        return jsonify(response={"error": (str(error.orig))}), 500
    
    return jsonify(response={"success": f"Successfully updated the new coffee price for {cafe_id}."}), 200

# /<int:cafe_id>/<string:api_key>
# def delete_cafe(cafe_id, api_key):

@app.route("/delete-cafe", methods = ["DELETE"])
def delete_cafe():
    """This function will delete a record from the Cafe database / table, 
    as long as the API key matches and the Id passed is valid."""
    
    cafe_id_to_delete = request.args.get("cafe_id")
    sent_api_key = request.args.get("api_key")
    required_api_key = "password"
    
    if sent_api_key == required_api_key:
        try:
            delete_cafe = db.session.query(Cafe).get(cafe_id_to_delete)
            db.session.delete(delete_cafe)
            db.session.commit()
        
        except:
            return jsonify(response={"error": "Please check the id and api key you provided is correct."}), 500
        
        return jsonify(response={"success": f"Successfully deleted cafe {cafe_id_to_delete}."}), 200
    
    else:
        return jsonify(response={"error": "Invalid API key received."}), 500


    
if __name__ == '__main__':
    app.run(debug=True)
