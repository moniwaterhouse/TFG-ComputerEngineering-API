from flask import Blueprint, jsonify, request
from app import driver
from app.models.territory import create_cells, create_relations, delete_territory, check_missing_exploration

territory_bp = Blueprint('territory', __name__)

# Define a route to create the territory in the data base
@territory_bp.route('/initiate', methods=['POST'])
def initiate_territory():
    try:
         # Get the territory_file_path from the request URL parameters
        territory_file_path = request.args.get('territory_file_path')

        if territory_file_path:
            # Read and process the .txt file
            with open(territory_file_path, "r") as file:
                lines = file.readlines()

        # Create the Neo4j driver session outside of the loop
        with driver.session() as session:
            # Loop through the lines
            for y, line in enumerate(lines):
                line = line.strip()
                # Loop through the characters in each line
                for x, value in enumerate(line):
                    # Use the session to create nodes here
                    session.execute_write(create_cells, x, y, value)

        # Create relationships
        with driver.session() as session:
            session.execute_write(create_relations)

        return "Territory successfully created!", 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Define a route to reset the territory to its original values
@territory_bp.route('/reset', methods=['POST'])
def reset_territory():
    try:

        delete_territory(driver)
        result_initiation = initiate_territory()
        if result_initiation:
            return "Territory successfully reset!", 200
        else:
            return jsonify({"Error": "There has been an error resetting the territory."}), 404
        
    except Exception as e:
        return jsonify({"Error": str(e)}), 500

# Define a route to delete the territory from the data base
@territory_bp.route('/remove', methods=['POST'])
def remove_territory():
    try:
        # Call the function to run the Neo4j query
        delete_territory(driver)
        return "Territory successfully deleted!", 200
        
    except Exception as e:
        return jsonify({"Error": str(e)}), 500

# Define a route to check if all cells are visited
@territory_bp.route('/check-exploration', methods=['GET'])
def check_exploration():
    try:
        result = check_missing_exploration(driver)
        if result:
            return result, 200
        else:
            return jsonify({"error": "No missing cells to explore."}), 404
    except Exception as e:
        return jsonify({"Error": str(e)}), 500