# tdd maze by Michael Toth

setMediaPath('/Users/michaeltoth/Documents/tddmaze')
class Maze:
  """ A class which can solve a maze given by maze.jpg """
  def __init__(self):
    self.image=makePicture('maze.jpg')
    self.w = makeWorld(getWidth(self.image),getHeight(self.image))
    self.w.setPicture(self.image)
    self.t=makeTurtle(self.w)



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



