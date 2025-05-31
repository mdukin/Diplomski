import importlib
import os

def myfactory(module_name):
    module = importlib.import_module(f'plugins.{module_name}')
    return getattr(module, module_name)

def printGreeting(pet):
    print(f"{pet.name()} pozdravlja: {pet.greet()}")

def printMenu(pet):
    print(f"{pet.name()} voli {pet.menu()}")


def test():
    pets = []
    # Obiđi svaku datoteku kazala plugins 
    for mymodule in os.listdir('plugins'):
        moduleName, moduleExt = os.path.splitext(mymodule)
        # Ako se radi o datoteci s Pythonskim kodom ...
        if moduleExt == '.py':
            # Instanciraj ljubimca ...
            ljubimac = myfactory(moduleName)('Ljubimac ' + str(len(pets)))
            # ... i dodaj ga u listu ljubimaca
            pets.append(ljubimac)

    # Ispiši ljubimce
    for pet in pets:
        printGreeting(pet)
        printMenu(pet)

test()
