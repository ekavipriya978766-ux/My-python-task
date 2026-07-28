class vehical:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def display_car(self):
        print("brand",self.brand)
        print("model",self.model)
class car(vehical):
    def __init__(self,brand,model,fuel_type,seating_capacity):
        super().__init__(brand,model)
        self.fuel_type=fuel_type
        self.seating_capacity=seating_capacity
s1=car("TATA","I3","diasol","5")
print("brand:",s1.brand)
print("model:",s1.model)
print("fuel_type:",s1.fuel_type)
print("seating_capacity:",s1.seating_capacity)