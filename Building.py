

class Building:
    def __init__(self, min_floor, max_floor):
        self.min_floor = min_floor
        self.max_floor = max_floor
        self.list_elevators = []

    def __str__(self) -> str:
        for i in self.list_elevators:
            print(i)

        return ""
