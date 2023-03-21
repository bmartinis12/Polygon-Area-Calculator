class Rectangle:
  def __init__(self, width, heigth):
    self.width = width
    self.height = heigth

  def __str__(self):
    string = f"Rectangle(width={self.width}, height={self.height})"
    return string 

  def set_width(self, newWidth):
    self.width = newWidth

  def set_height(self, newHeight):
    self.height = newHeight 

  def get_area(self):
    area = self.width * self.height 
    return area 

  def get_perimeter(self):
    perimeter = (2 * self.width) + (2 * self.height)
    return perimeter

  def get_diagonal(self):
    diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
    return diagonal

  def get_picture(self):
    if(self.width > 50 or self.height > 50):
      return "Too big for picture."

    picture = ""
    i = self.height
    while i > 0:
      l = self.width
      while l > 0:
        picture += "*"
        l -= 1
      picture += "\n"
      i -= 1
    print(picture)
    return picture
    
  def get_amount_inside(self, shape):
    amount = self.get_area() / shape.get_area()
    return int(amount)
    

class Square(Rectangle):
  def __init__(self, side):
    self.width = side
    self.height = side 

  def __str__(self):
    string = f"Square(side={self.width})"
    return string 

  def set_side(self, newSide):
    self.width = newSide
    self.height = newSide 

  def set_width(self, newSide):
    self.width = newSide

  def set_height(self, newSide):
    self.height = newSide
