start = (0, 0)

class Wire:

    def __init__(self, start, direction, length, number):
        self.x, self.y = start
        self.direction = direction
        self.length = length
        self.nb = number

    def get_end_position(self):
        if self.direction == "R":
            return (self.x + self.length, self.y)
        elif self.direction == "L":
            return (self.x - self.length, self.y)
        elif self.direction == 'U':
            return (self.x, self.y + self.length)
        else:
            return (self.x, self.y - self.length)


def create_circuit(circuit):
    start = (0, 0)
    path = {
        'R': [],
        'L': [],
        'U': [],
        'D': []
    }

    for i, w in enumerate(circuit.split(',')):
        direction, length = w[0], int(w[1:])
        wire = Wire(start, direction, length, i)
        start = wire.get_end_position()

        path[direction].append(wire)
        
    return path

def get_intersection_distances(path1, path2):
    intersection_distances = []

    # On compare les R du premier circuit avec les U du second
    for wH in path1['R']:
        for wV in path2['U']:
            if wH.x < wV.x and wH.x + wH.length > wV.x and wH.y > wV.y and wH.y < wV.y + wV.length:
                intersection_distances.append(abs(wV.x) + abs(wH.y))

    # On compare les L du premier circuit avec les U du second
    for wH in path1['L']:
        for wV in path2['U']:
            if wH.x > wV.x and wH.x - wH.length < wV.x and wH.y > wV.y and wH.y < wV.y + wV.length:
                intersection_distances.append(abs(wV.x) + abs(wH.y))
    
    # On compare les L du premier circuit avec les D du second
    for wH in path1['L']:
        for wV in path2['D']:
            if wH.x > wV.x and wH.x - wH.length < wV.x and wH.y < wV.y and wH.y > wV.y - wV.length:
                intersection_distances.append(abs(wV.x) + abs(wH.y))

    # On compare les R du premier circuit avec les D du second
    for wH in path1['R']:
        for wV in path2['D']:
            if wH.x < wV.x and wH.x + wH.length > wV.x and wH.y < wV.y and wH.y > wV.y - wV.length:
                intersection_distances.append(abs(wV.x) + abs(wH.y))

    # On compare les R du second circuit avec les U du premier
    for wH in path2['R']:
        for wV in path1['U']:
            if wH.x < wV.x and wH.x + wH.length > wV.x and wH.y > wV.y and wH.y < wV.y + wV.length:
                intersection_distances.append(abs(wV.x) + abs(wH.y))

    # On compare les L du second circuit avec les U du premier
    for wH in path2['L']:
        for wV in path1['U']:
            if wH.x > wV.x and wH.x - wH.length < wV.x and wH.y > wV.y and wH.y < wV.y + wV.length:
                intersection_distances.append(abs(wV.x) + abs(wH.y))
    
    # On compare les L du second circuit avec les D du premier
    for wH in path2['L']:
        for wV in path1['D']:
            if wH.x > wV.x and wH.x - wH.length < wV.x and wH.y < wV.y and wH.y > wV.y - wV.length:
                intersection_distances.append(abs(wV.x) + abs(wH.y))

    # On compare les R du second circuit avec les D du premier
    for wH in path2['R']:
        for wV in path1['D']:
            if wH.x < wV.x and wH.x + wH.length > wV.x and wH.y < wV.y and wH.y > wV.y - wV.length:
                intersection_distances.append(abs(wV.x) + abs(wH.y))
            
    return intersection_distances

if __name__ == "__main__":
    with open("input.txt", 'r') as f:
        wire1 = f.readline()
        path1 = create_circuit(wire1)

        wire2 = f.readline()
        path2 = create_circuit(wire2)

    print(f'The Manhattan distance from the central port to the closest intersection is {min(get_intersection_distances(path1, path2))}')