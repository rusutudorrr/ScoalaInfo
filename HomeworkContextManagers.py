import contextlib


class just_some_exceptions:
    def __init__(self):
        self.bike = {'Brand': 'Specialized', 'Model': 'Demo'}

    def __enter__(self):
        return self.bike

    def __exit__(self, exc_type, exc_value, exc_tb):
        try:
            my_bike = bike['Brand']
            print(my_bike)
            my_model = bike['Model']
            print(my_model)
            my_wheel = bike['Wheel']
            print(my_wheel)
        except KeyError as key:
            print("Your", key, "does not exist")
        try:
            my_shifter = list(bike.get('Model'))
            print(my_shifter[5])
        except IndexError as index:
            print(index, "and was not found")
        finally:
            return


with just_some_exceptions() as bike:
    print('*' * 50)
    print(bike)
    print('*' * 50)


@contextlib.contextmanager
def just_some_exceptions2():
    my_bike = {'Brand': 'Specialized', 'Model': 'Demo'}
    yield
    try:
        bike_brand = my_bike['Brand']
        print(bike_brand)
        bike_model = my_bike['Model']
        print(bike_model)
        bike_wheel = my_bike['Wheel']
        print(bike_wheel)
    except KeyError as key:
        print("Your", key, "does not exist")
    try:
        my_shifter = list(my_bike.get('Model'))
        print(my_shifter[5])
    except IndexError as index:
        print(index, "and was not found")

    finally:
        return


with just_some_exceptions() as my_bike:
    print('*' * 50)
    print(my_bike)
    print('*' * 50)

# Stiu ca nu ii cel mai elegant si mai practic dar am vrut musai sa am un singur cod pentru ambele erori.
# Ca sa nu scriu cate o clasa si pentru dictionar si pentru lista.
# De asta nici nu um facut upload pana azi, ca sa ii dau cumva de cap.
# XoXo

