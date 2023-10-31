# https://www.bogotobogo.com/python/python_private_attributes_methods.php
class P:
   def __init__(self, name, alias):
      self.name = name       # public
      self.__alias = alias   # private

   def who(self):
      print('name  : ', self.name)
      print('alias : ', self.__alias)


a = P('a','b')
a.who()
print(a.name)           # Allowed
print(a.__alias)        # Raises AttributeError
