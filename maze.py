# tdd maze by Michael Toth

setMediaPath('/Users/michaeltoth/Documents/tddmaze')
class Maze:
  """ A class which can solve a maze given by maze.jpg """
  def __init__(self):
    self.image=makePicture('maze.jpg')
    self.w = makeWorld(getWidth(self.image),getHeight(self.image))
    self.w.setPicture(self.image)
    self.t=makeTurtle(self.w)
    penUp(self.t)
    moveTo(self.t,30,190)
    self.t.setHeading(90)

  def colorInFront(self):
    if getHeading(self.t) == 90:
      px = getPixelAt(self.image,self.t.getXPos()+20,self.t.getYPos())
    if getHeading(self.t) == 180: 
      px = getPixelAt(self.image,self.t.getXPos(),self.t.getYPos()+20)
    if getHeading(self.t) == 270:
      px = getPixelAt(self.image,self.t.getXPos()-20,self.t.getYPos())
    if getHeading(self.t) == 0: 
      px = getPixelAt(self.image,self.t.getXPos(),self.t.getYPos()-20)
    c = getColor(px)
    if distance(c,white)<150:
      return white
    if distance(c,blue)<150:
      return blue
    return blue



# tests

if 1:
    # test for existance of maze
    m = Maze()
    # test for image
    assert m.image.__class__==Picture
    # test for world 
    assert m.w.__class__==World
    # test for picture
    p = m.w.getPicture()
    assert p.getFileName() != 'None'
    # test for turtle
    assert m.t.__class__ == Turtle
    # test for turtle position
    assert m.t.getXPos()==30
    assert m.t.getYPos()==190
    # test for color in front
    assert m.colorInFront()==white
    # point down
    m.t.setHeading(180)
    assert m.colorInFront()==blue
    # check the other two directions
    m.t.setHeading(270)
    assert m.colorInFront()==blue
    m.t.setHeading(0)
    assert m.colorInFront()==white



