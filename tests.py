# coding=utf-8
import unittest
from bomberman.client import Client

class TestBomberman(unittest.TestCase):  
  def setUp(self):
    self.bomberman = Client()
    
  def test_profane(self):
    corpi = [["fuck", True], ["dog", False], ["discombobulate", False], [u'\u2206', False], [None, False]]
    for corpus in corpi:
      self.assertEquals(self.bomberman.is_profane(corpus[0]), corpus[1])
  
  def test_censor(self):
    corpi = [["The quick brown fox jumped over the lazy dog.", "The quick brown fox jumped over the lazy dog."], 
             ["The quick brown fox jumped the fuck over the lazy dog.", "The quick brown fox jumped the *** over the lazy dog."]]
    for corpus in corpi:
        self.assertEquals(self.bomberman.censor(corpus[0]), corpus[1])
    corpi = [["The quick brown fox jumped the fuck over the lazy dog.", "The quick brown fox jumped the ||| over the lazy dog."]]
    for corpus in corpi:
        self.assertEquals(self.bomberman.censor(corpus[0], "|||"), corpus[1])
  
  def test_highlight(self):
    corpi = [["The quick brown fox jumped over the lazy dog.", "The quick brown fox jumped over the lazy dog."], 
             ["The quick brown fox jumped the fuck over the lazy dog.", "The quick brown fox jumped the <strong>fuck</strong> over the lazy dog."]]
    for corpus in corpi:
        self.assertEquals(self.bomberman.highlight(corpus[0]), corpus[1])
    corpi = [["The quick brown fox jumped the fuck over the lazy dog.", "The quick brown fox jumped the <blink>fuck</blink> over the lazy dog."]]
    for corpus in corpi:
        self.assertEquals(self.bomberman.highlight(corpus[0], "<blink>", "</blink>"), corpus[1])
          
  def test_japanese_profane(self):
    corpi = [["黒人", True], ["聖パトリックの日", False], ["つくえ", False]]
    for corpus in corpi:
      self.assertEquals(self.bomberman.is_profane(corpus[0], "ja"), corpus[1])
        
  def test_japanese_censor(self):
    corpi = [["くんに紫色のペンギン", unicode("***紫色のペンギン", "utf-8")]]
    for corpus in corpi:
      self.assertEquals(self.bomberman.censor(corpus[0], "***", "ja"), corpus[1])
  
  def test_japanese_highlight(self):
    corpi = [["くんに紫色のペンギン", unicode("<blink>くんに</blink>紫色のペンギン", "utf-8")]]
    for corpus in corpi:
      self.assertEquals(self.bomberman.highlight(corpus[0], "<blink>", "</blink>", "ja"), corpus[1])

def main():
    unittest.main()

if __name__ == '__main__':
    main()
