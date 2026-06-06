class Cell:
    def __init__(self) -> None:
        """Initialize walls as closed """
        """and mark the cell unvisited."""
        self.north: bool = True
        self.south: bool = True
        self.east: bool = True
        self.west: bool = True
        self.visited: bool = False
