class Plates:
    def __init__(self):
        self.plates = []

    def populatePlates(self):
        for i in range(10):
            self.plates.append({
                'id': str(i + 1),
                'color': 'red',
                'type': 'bowl',
                'material': 'ceramic',
                'price': 4500,
                'dimensions': '40x40cm'
            })

    def updateAtId(self, id, newPlate):
        if id > len(self.plates):
            return False

        a = self.plates[:(id - 1)] # 0 -> the number less than id
        b = self.plates[id:] # the number after the id -> the end of the list
        self.plates = a + b
        newPlate['id'] = str(id)
        self.plates.append(newPlate)
        
        return True



plates = Plates()