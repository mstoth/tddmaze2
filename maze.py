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
    if getHeading(self.t) == 90 or getHeading(self.t) == -270:
      px = getPixelAt(self.image,self.t.getXPos()+20,self.t.getYPos())
    if getHeading(self.t) == 180 or getHeading(self.t) == -180: 
      px = getPixelAt(self.image,self.t.getXPos(),self.t.getYPos()+20)
    if getHeading(self.t) == 270 or getHeading(self.t) == -90:
      px = getPixelAt(self.image,self.t.getXPos()-20,self.t.getYPos())
    if getHeading(self.t) == 0: 
      px = getPixelAt(self.image,self.t.getXPos(),self.t.getYPos()-20)
    c = getColor(px)
    if distance(c,white)<150:
      return white
    if distance(c,blue)<150:
      return blue
    return blue
  
  def travel2BranchOrWall(self):
    starting = true
    while self.colorInFront() == white:
      turn(self.t,90)
      r=self.colorInFront()
      turn(self.t,180)
      l=self.colorInFront()
      turn(self.t,90)
      if r==white or l==white: 
        # we have found a branch
        print "found branch at %d,%d" % (getXPos(self.t),getYPos(self.t))
        if starting:
          starting = false
          forward(self.t,10)
        else:
          while getXPos(self.t)%10 or getYPos(self.t)%10:
            forward(self.t,1)
          return
      forward(self.t,1)
    forward(self.t,11)
      


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
    # test travel2branchOrWall
    m.t.setHeading(90)
    moveTo(m.t,30,190)
    m.travel2BranchOrWall()
    assert getXPos(m.t)==110
    assert getYPos(m.t)==190
    # test going north
    moveTo(m.t,30,190)
    m.t.setHeading(0)
    m.travel2BranchOrWall()
    assert getXPos(m.t)==30
    assert getYPos(m.t)==110
    # more tests
    m.t.setHeading(90)
    m.travel2BranchOrWall()
    assert getXPos(m.t)==110
    assert getYPos(m.t)==110
    turn(m.t,90)
    m.travel2BranchOrWall()
    assert getXPos(m.t)==110
    assert getYPos(m.t)==150
    # trail test
    moveTo(m.t,30,190)
    m.t.setHeading(90)
    m.travel2BranchOrWall()
    turn(m.t,180)
    assert m.colorInFront()==green
    
