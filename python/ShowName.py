class ShowName:
   'simple for show name '


def __init__(self, firstname , lastname):
  self.firstname = firstname
  self.lastname = lastname

  def get_completename(self):
      print "Your complete name is : " self.firstname


myname = ShowName("Leandro", "Azevedo")
