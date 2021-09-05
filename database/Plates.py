plates = []


def populatePlates():
    for i in range(10):
        params = {
            'id': str(i + 1),
            'color': 'red',
            'type': 'bowl',
            'material': 'ceramic',
            'dimensions': '40x40in',
            'price': 4500
        }
        plates.append(params)
