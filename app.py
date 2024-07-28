from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def calculate_rent_per_room(rent, num_rooms, room_dimensions, bills=None):
    room_areas = [dimension[0] * dimension[1] for dimension in room_dimensions]
    total_area = sum(room_areas)
    rent_per_area = rent / total_area
    rent_per_room = [round(area * rent_per_area, 2) for area in room_areas]
    if bills is not None:
        total_rent_per_room = [round(rent_room + bills / num_rooms, 2) for rent_room in rent_per_room]
        return total_rent_per_room
    else:
        return rent_per_room

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    rent = float(data['rent'])
    num_rooms = int(data['num_rooms'])
    room_dimensions = [list(map(float, dims.split(','))) for dims in data['room_dimensions']]
    bills = float(data['bills']) if data['bills'] else None

    rent_per_room = calculate_rent_per_room(rent, num_rooms, room_dimensions, bills)
    return jsonify(rent_per_room)

if __name__ == '__main__':
    app.run(debug=True)
