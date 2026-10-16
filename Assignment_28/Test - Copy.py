import math

class Circle:
    def __init__(self):
        """Initializes the circle with a default radius of 0."""
        self.radius = 0.0

    def accept_radius(self):
        """Instance method to accept radius input from the user."""
        try:
            user_input = input("Enter the radius of the circle: ")
            self.radius = float(user_input)
            if self.radius < 0:
                print("Warning: Radius cannot be negative. Setting radius to 0.")
                self.radius = 0.0
        except ValueError:
            print("Invalid input! Please enter a valid numerical value.")
            self.radius = 0.0

    def calculate_area(self):
        """Instance method to calculate and return the area of the circle."""
        return math.pi * (self.radius ** 2)

    def display_result(self):
        """Instance method to display the final area."""
        area = self.calculate_area()
        print(f"The area of the circle with radius {self.radius} is: {area:.2f}")


# --- Execution Code ---
if __name__ == "__main__":
    # Create an instance (object) of the Circle class
    my_circle = Circle()
    
    # Call the instance method to accept user input
    my_circle.accept_radius()
    
    # Call the instance method to display the final calculation
    my_circle.display_result()