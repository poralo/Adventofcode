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
        'D': [],
        'all': []
    }

    for i, w in enumerate(circuit.split(',')):
        direction, length = w[0], int(w[1:])
        wire = Wire(start, direction, length, i)
        start = wire.get_end_position()

        path[direction].append(wire)
        path['all'].append(wire)
        
    return path

def get_intersection_steps(path1, path2):
    intersection_number = []
    
    # On compare les R du premier circuit avec les U du second
    for wH in path1['R']:
        for wV in path2['U']:
            if wH.x < wV.x and wH.x + wH.length > wV.x and wH.y > wV.y and wH.y < wV.y + wV.length:
                intersection_number.append((wH.nb, wV.nb))

    # On compare les L du premier circuit avec les U du second
    for wH in path1['L']:
        for wV in path2['U']:
            if wH.x > wV.x and wH.x - wH.length < wV.x and wH.y > wV.y and wH.y < wV.y + wV.length:
                intersection_number.append((wH.nb, wV.nb))
    
    # On compare les L du premier circuit avec les D du second
    for wH in path1['L']:
        for wV in path2['D']:
            if wH.x > wV.x and wH.x - wH.length < wV.x and wH.y < wV.y and wH.y > wV.y - wV.length:
                intersection_number.append((wH.nb, wV.nb))

    # On compare les R du premier circuit avec les D du second
    for wH in path1['R']:
        for wV in path2['D']:
            if wH.x < wV.x and wH.x + wH.length > wV.x and wH.y < wV.y and wH.y > wV.y - wV.length:
                intersection_number.append((wH.nb, wV.nb))

    # On compare les R du second circuit avec les U du premier
    for wH in path2['R']:
        for wV in path1['U']:
            if wH.x < wV.x and wH.x + wH.length > wV.x and wH.y > wV.y and wH.y < wV.y + wV.length:
                intersection_number.append((wH.nb, wV.nb))

    # On compare les L du second circuit avec les U du premier
    for wH in path2['L']:
        for wV in path1['U']:
            if wH.x > wV.x and wH.x - wH.length < wV.x and wH.y > wV.y and wH.y < wV.y + wV.length:
                intersection_number.append((wH.nb, wV.nb))
    
    # On compare les L du second circuit avec les D du premier
    for wH in path2['L']:
        for wV in path1['D']:
            if wH.x > wV.x and wH.x - wH.length < wV.x and wH.y < wV.y and wH.y > wV.y - wV.length:
                intersection_number.append((wH.nb, wV.nb))

    # On compare les R du second circuit avec les D du premier
    for wH in path2['R']:
        for wV in path1['D']:
            if wH.x < wV.x and wH.x + wH.length > wV.x and wH.y < wV.y and wH.y > wV.y - wV.length:
                intersection_number.append((wH.nb, wV.nb))
    
    steps = []
    for d in intersection_number:
        s = 0
        for i in range(d[0]):
            s += path1['all'][i].length

        for j in range(d[1]):
            s += path2['all'][j].length

        s += abs(path1['all'][d[0]].x - path2['all'][d[1]].x)
        s += abs(path1['all'][d[0]].y - path2['all'][d[1]].y)

        steps.append(s)

    return steps
    
if __name__ == "__main__":
    with open("input.txt", 'r') as f:
        wire1 = f.readline()
        path1 = create_circuit(wire1)

        wire2 = f.readline()
        path2 = create_circuit(wire2)

    print(f'The fewest combined steps the wires must take to reach an intersection is {min(get_intersection_steps(path1, path2))}')