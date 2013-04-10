import unittest
from bomberman.client import Client

class TestBomberman(unittest.TestCase):  
  def setUp(self):
    self.bomberman = Client()
    
  def test_profane(self):
    corpi = [["hell", True], ["dog", False], ["discombobulate", False]]
    for corpus in corpi:
      self.assertEquals(self.bomberman.is_profane(corpus[0]), corpus[1])
  
  def test_censor(self):
    corpi = [["The quick brown fox jumped over the lazy dog.", "The quick brown fox jumped over the lazy dog."], 
             ["The quick brown fox jumped out of hell over the lazy dog.", "The quick brown fox jumped out of *** over the lazy dog."]]
    for corpus in corpi:
        self.assertEquals(self.bomberman.censor(corpus[0]), corpus[1])
    corpi = [["The quick brown fox jumped out of hell over the lazy dog.", "The quick brown fox jumped out of ||| over the lazy dog."]]
    for corpus in corpi:
        self.assertEquals(self.bomberman.censor(corpus[0], "|||"), corpus[1])

  def test_highlight(self):
    corpi = [["The quick brown fox jumped over the lazy dog.", "The quick brown fox jumped over the lazy dog."], 
             ["The quick brown fox jumped out of hell over the lazy dog.", "The quick brown fox jumped out of <strong>hell</strong> over the lazy dog."]]
    for corpus in corpi:
        self.assertEquals(self.bomberman.highlight(corpus[0]), corpus[1])
    corpi = [["The quick brown fox jumped out of hell over the lazy dog.", "The quick brown fox jumped out of <blink>hell</blink> over the lazy dog."]]
    for corpus in corpi:
        self.assertEquals(self.bomberman.highlight(corpus[0], "<blink>", "</blink>"), corpus[1])
          
def main():
    unittest.main()

if __name__ == '__main__':
    main()
