class Parent():
    def __init__(self, last_name, eye_color):
        self.last_name = last_name
        self.eye_color = eye_color
    
    def show_info(self):
        print "Last Name: " + self.last_name
        print "Eye Color: " + self.eye_color
        return ""
    

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys
    
    def show_info(self):
        Parent.show_info(self)
        print "Number of Toys: " + str(self.number_of_toys)
        return ""
        
john_sr = Parent("Doe", "blue")
print john_sr.show_info()
john_jr = Child("Doe", "brown", 8)
print john_jr.show_info()
