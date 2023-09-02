
def first_repeated_value(list):
  # create a Set to keep track of values we've seen
  number_set = set()
  # iterate over each element from the list
  for i in range (0, len(list)):

    # if we've already seen a value, we've found the duplicate!
    if list[i] in number_set:
        return list[i]
    # otherwise, add the value to our set
    number_set.add(list[i])
  # return None if we reach the end and haven't found our value
  return None

print(first_repeated_value([1,2,3,3,4,4]))


#LETS BUILD A MY SET CLASS 
class MySet:
    def __init__(self, enumerable = None):
        if enumerable is None:
            enumerable = []
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True
        
    
    #This method checks if the value is already included in the set, and returns true if so, and false if not
    def has(self,value):
        return value in self.dictionary
    
    #This method needs to add a value to the set if it isn't already present, and return the updated set.
    def add (self, value):
        self.dictionary[value] = True
        return self  #return the updated set
    
    #removes a value from the set, and returns the updated set
    def delete (self, value):
        self.dictionary.pop(value, None) 
        return self
    
    #return the number of elements in the set
    def size(self):
        return len(self.dictionary)