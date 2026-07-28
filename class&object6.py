class laptop():
    def __init__(self,brand,RAM):
        self.brand=brand
        self.RAM=RAM
    def display(self):
        print("brand",self.brand)
        print("RAM",self.RAM)
l1=laptop("AUSU Vivobook","i3")
l2=laptop("lenovo","i5")
l1.display()
l2.display()







class movie():
    def __init__(self,movie_name,director,rating):
        self.movie_name=movie_name
        self.director=director
        self.rating=rating
    def display(self):
        print("movie_name",self.movie_name)
        print("director",self.director)
        print("rating",self.rating)
m1=movie("love oh love","dhunush",5.5)
m2=movie(28,"kavipriya",3.5)
m1.display()
m2.display()
