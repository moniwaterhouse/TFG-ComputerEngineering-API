# Define a function to deposit pheromone
def deposit_pheromone(driver, x_pos, y_pos, pheromone_intensity):
    query = """
    MATCH (c:Cell {xPos: $xPos, yPos: $yPos})
    SET c.pheromoneIntensity = $pheromoneIntensity, c.visited = 'V'
    RETURN c;
    """

    with driver.session() as session:
        result = session.run(query, xPos=x_pos, yPos=y_pos, pheromoneIntensity=pheromone_intensity)
        return result.single()  # Assuming you expect a single result

# Define a function to decrement pheromoneIntensity
def evaporate_pheromones(driver):
    query = """
    MATCH (c:Cell)
    WHERE c.pheromoneIntensity > 0
    SET c.pheromoneIntensity = c.pheromoneIntensity - 1
    RETURN c;
    """

    with driver.session() as session:
        result = session.run(query)
        return result

# Define a function to check the pheromone intensity from the current cell
def check_current_pheromone(driver, x_pos, y_pos):
    query = """
    MATCH (c:Cell {xPos: $xPos, yPos: $yPos})
    RETURN
       c.pheromoneIntensity AS pheromoneIntensity;
    """

    with driver.session() as session:
        result = session.run(query, xPos=x_pos, yPos=y_pos)
        return result.single()

# Define a function to check the north neighbor's pheromone intensity
def check_north_pheromone(driver, x_pos, y_pos):
    query = """
    MATCH (c:Cell {xPos: $xPos, yPos: $yPos})
    OPTIONAL MATCH (northNeighbor:Cell {xPos: c.xPos, yPos: c.yPos - 1})
    RETURN
       northNeighbor.pheromoneIntensity AS northPheromoneIntensity;
    """

    with driver.session() as session:
        result = session.run(query, xPos=x_pos, yPos=y_pos)
        return result.single()

# Define a function to check the south neighbor's pheromone intensity
def check_south_pheromone(driver, x_pos, y_pos):
    query = """
    MATCH (c:Cell {xPos: $xPos, yPos: $yPos})
    OPTIONAL MATCH (southNeighbor:Cell {xPos: c.xPos, yPos: c.yPos + 1})
    RETURN
       southNeighbor.pheromoneIntensity AS southPheromoneIntensity;
    """

    with driver.session() as session:
        result = session.run(query, xPos=x_pos, yPos=y_pos)
        return result.single()

# Define a function to check the east neighbor's pheromone intensity
def check_east_pheromone(driver, x_pos, y_pos):
    query = """
    MATCH (c:Cell {xPos: $xPos, yPos: $yPos})
    OPTIONAL MATCH (eastNeighbor:Cell {xPos: c.xPos + 1, yPos: c.yPos})
    RETURN
       eastNeighbor.pheromoneIntensity AS eastPheromoneIntensity;
    """

    with driver.session() as session:
        result = session.run(query, xPos=x_pos, yPos=y_pos)
        return result.single()

# Define a function to check the west neighbor's pheromone intensity
def check_west_pheromone(driver, x_pos, y_pos):
    query = """
    MATCH (c:Cell {xPos: $xPos, yPos: $yPos})
    OPTIONAL MATCH (westNeighbor:Cell {xPos: c.xPos - 1, yPos: c.yPos})
    RETURN
       westNeighbor.pheromoneIntensity AS westPheromoneIntensity;
    """

    with driver.session() as session:
        result = session.run(query, xPos=x_pos, yPos=y_pos)
        return result.single()

# Define a function to check the north neighbor's type
def check_north_type(driver, x_pos, y_pos):
    query = """
    MATCH (c:Cell {xPos: $xPos, yPos: $yPos})
    OPTIONAL MATCH (northNeighbor:Cell {xPos: c.xPos, yPos: c.yPos - 1})
    RETURN
       northNeighbor.type AS cellType;
    """

    with driver.session() as session:
        result = session.run(query, xPos=x_pos, yPos=y_pos)
        return result.single()

# Define a function to check the south neighbor's type
def check_south_type(driver, x_pos, y_pos):
    query = """
    MATCH (c:Cell {xPos: $xPos, yPos: $yPos})
    OPTIONAL MATCH (southNeighbor:Cell {xPos: c.xPos, yPos: c.yPos + 1})
    RETURN
       southNeighbor.type AS cellType;
    """

    with driver.session() as session:
        result = session.run(query, xPos=x_pos, yPos=y_pos)
        return result.single()

# Define a function to check the east neighbor's type
def check_east_type(driver, x_pos, y_pos):
    query = """
    MATCH (c:Cell {xPos: $xPos, yPos: $yPos})
    OPTIONAL MATCH (eastNeighbor:Cell {xPos: c.xPos + 1, yPos: c.yPos})
    RETURN
       eastNeighbor.type AS cellType;
    """

    with driver.session() as session:
        result = session.run(query, xPos=x_pos, yPos=y_pos)
        return result.single()

# Define a function to check the west neighbor's type
def check_west_type(driver, x_pos, y_pos):
    query = """
    MATCH (c:Cell {xPos: $xPos, yPos: $yPos})
    OPTIONAL MATCH (westNeighbor:Cell {xPos: c.xPos - 1, yPos: c.yPos})
    RETURN
       westNeighbor.type AS cellType;
    """

    with driver.session() as session:
        result = session.run(query, xPos=x_pos, yPos=y_pos)
        return result.single()

# Define a function to check the type of the current cell
def check_current_type(driver, x_pos, y_pos):
    query = """
    MATCH (c:Cell {xPos: $xPos, yPos: $yPos})
    RETURN
       c.type AS cellType;
    """

    with driver.session() as session:
        result = session.run(query, xPos=x_pos, yPos=y_pos)
        return result.single()

# Define a function to check if the current cell has been visited
def is_current_visited(driver, x_pos, y_pos):
    query = """
    MATCH (c:Cell {xPos: $xPos, yPos: $yPos})
    RETURN
       c.visited AS visited;
    """

    with driver.session() as session:
        result = session.run(query, xPos=x_pos, yPos=y_pos)
        return result.single()

# Define a function to set the north neighbor's type
def set_north_type(driver, x_pos, y_pos, type):
    if type == 1:
        query = """
        MATCH (c:Cell {xPos: $xPos, yPos: $yPos})
        OPTIONAL MATCH (northNeighbor:Cell {xPos: c.xPos, yPos: c.yPos - 1})
        SET  northNeighbor.type = 1, northNeighbor.pheromoneIntensity = null, northNeighbor.visited = null
        RETURN northNeighbor;
        """
    else:
        query = """
        MATCH (c:Cell {xPos: $xPos, yPos: $yPos})
        OPTIONAL MATCH (northNeighbor:Cell {xPos: c.xPos, yPos: c.yPos - 1})
        SET  northNeighbor.type = 0, northNeighbor.pheromoneIntensity = 0, northNeighbor.visited = 'F'
        RETURN northNeighbor;
        """

    with driver.session() as session:
        result = session.run(query, xPos=x_pos, yPos=y_pos)
        return result.single()

# Define a function to set the south neighbor's type
def set_south_type(driver, x_pos, y_pos, type):
    if type == 1:
        query = """
        MATCH (c:Cell {xPos: $xPos, yPos: $yPos})
        OPTIONAL MATCH (southNeighbor:Cell {xPos: c.xPos, yPos: c.yPos + 1})
        SET  southNeighbor.type = 1, southNeighbor.pheromoneIntensity = null, southNeighbor.visited = null
        RETURN southNeighbor;
        """
    else:
        query = """
        MATCH (c:Cell {xPos: $xPos, yPos: $yPos})
        OPTIONAL MATCH (southNeighbor:Cell {xPos: c.xPos, yPos: c.yPos + 1})
        SET  southNeighbor.type = 0, southNeighbor.pheromoneIntensity = 0, southNeighbor.visited = 'F'
        RETURN southNeighbor;
        """

    with driver.session() as session:
        result = session.run(query, xPos=x_pos, yPos=y_pos)
        return result.single()

# Define a function to set the east neighbor's type
def set_east_type(driver, x_pos, y_pos, type):
    if type == 1:
        query = """
        MATCH (c:Cell {xPos: $xPos, yPos: $yPos})
        OPTIONAL MATCH (eastNeighbor:Cell {xPos: c.xPos + 1, yPos: c.yPos})
        SET  eastNeighbor.type = 1, eastNeighbor.pheromoneIntensity = null, eastNeighbor.visited = null
        RETURN eastNeighbor;
        """
    else:
        query = """
        MATCH (c:Cell {xPos: $xPos, yPos: $yPos})
        OPTIONAL MATCH (eastNeighbor:Cell {xPos: c.xPos + 1, yPos: c.yPos})
        SET  eastNeighbor.type = 0, eastNeighbor.pheromoneIntensity = 0, eastNeighbor.visited = 'F'
        RETURN eastNeighbor;
        """

    with driver.session() as session:
        result = session.run(query, xPos=x_pos, yPos=y_pos)
        return result.single()

# Define a function to set the west neighbor's type
def set_west_type(driver, x_pos, y_pos, type):
    if type == 1:
        query = """
        MATCH (c:Cell {xPos: $xPos, yPos: $yPos})
        OPTIONAL MATCH (westNeighbor:Cell {xPos: c.xPos - 1, yPos: c.yPos})
        SET  westNeighbor.type = 1, westNeighbor.pheromoneIntensity = null, westNeighbor.visited = null
        RETURN westNeighbor;
        """
    else:
        query = """
        MATCH (c:Cell {xPos: $xPos, yPos: $yPos})
        OPTIONAL MATCH (westNeighbor:Cell {xPos: c.xPos - 1, yPos: c.yPos})
        SET  westNeighbor.type = 0, westNeighbor.pheromoneIntensity = 0, westNeighbor.visited = 'F'
        RETURN westNeighbor;
        """

    with driver.session() as session:
        result = session.run(query, xPos=x_pos, yPos=y_pos)
        return result.single()