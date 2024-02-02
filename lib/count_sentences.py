#!/usr/bin/env python3

class MyString:
  pass
  def __init__(self, value=""):
    self._value = value
  
  def getValue(self):
    return self._value

  def setValue(self, value):
    if (type(value) == (str)):
      self._value = value
    else:
      print("The value must be a string.")
  
  value = property(getValue, setValue)

  def is_sentence(self):
    x = self._value.find(".")
    if x != -1:
      return True
    else:
      return False
  
  def is_question(self):
    x = self._value.find("?")
    if x != -1:
      return True
    else:
      return False
    
  def is_exclamation(self):
    x = self._value.find("!")
    if x != -1:
      return True
    else:
      return False
  
  def count_sentences(self):
    pass
    x = self._value.replace("?", ".")
    # self._value.replace("!", ".")
    y = x.replace("!", ".")
    z = y.split(".")
    
    count = 0
    for word in z:
      if len(word)>1:
        count +=1
    return count