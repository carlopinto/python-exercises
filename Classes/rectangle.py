### Write a class to represent a rectangle which is located somewhere in the XY plane.
### A conventional choice is to specify the upper-left corner of the rectangle, and the size.
### To specify the upper-left corner, we have embedded a Point object.

class Point:
    """ Point class represents and manipulates x,y coords. """
    
    def __init__(self, x=0, y=0):
        """ Create a new point at x,y """
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)
    
    def halfway(self, target):
        """ Return the halfway point between myself and the target """
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)
    
    def slope_from_origin(self):
        """ Returns the slope of the line joining the origin to the point"""
        if self.x != 0:
            return self.y / self.x 
        else:
            return None
        
    def slope_from_target(self, target):
        """ Returns the slope of the line joining the origin to the target point"""
        if self.x - target.x != 0:
            return (self.y - target.y) / (self.x  - target.x)
        else:
            return None
        
    def get_line_to(self, target):
        """ Given another point, it will compute the equation of the straight line joining the two points
            Returns the two coefficients as a tuple of two values"""
        a = self.slope_from_target(target)
        if a != None:
            b = self.y - a * self.x
            return a, b
        else:
            return None

class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn # upper left corner
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)
    
    def grow(self, delta_width, delta_height):
        """ Grow (or shrink) this object by the deltas """
        self.width += delta_width
        self.height += delta_height

    def move(self, dx, dy):
        """ Move this object by the deltas """
        self.corner.x += dx
        self.corner.y += dy

    def area(self):
        """ Returns the area of any instance"""
        return self.width * self.height
    
    def perimeter(self):
        """ Returns the perimeter of any rectangle instance"""
        return self.width * 2 + self.height * 2
    
    def flip(self):
        """ Swaps the width and the height of any rectangle instance"""
        temp = self.width
        self.width = self.height
        self.height = temp

    def contains(self, p):
        """ Test if a Point falls within the rectangle """
        if p.x >= self.corner.x and p.x < self.corner.x + self.width and p.y >= self.corner.y and p.y < self.corner.y + self.height:
             return True
        else:
            return False

    def rectangles_overlap(self, rect2):
        """ Determine whether two rectangles collide """
        # Check if rect1 is to the left of rect2
        if self.corner.x + self.width <= rect2.corner.x:
            return False

        # Check if rect1 is to the right of rect2
        if self.corner.x >= rect2.corner.x + rect2.width:
            return False

        # Check if rect1 is above rect2
        if self.corner.y >= rect2.corner.y + rect2.height:
            return False

        # Check if rect1 is below rect2
        if self.corner.y + self.height <= rect2.corner.y:
            return False

        # If none of the above conditions are met, the rectangles collide
        return True