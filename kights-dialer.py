keypad = {
  0: (4,6),
  1: (6,8),
  2: (7,9),
  3: (4,8),
  4: (0,3,9),
  5: (),
  6: (0,1,7),
  7: (2,6),
  8: (1,3),
  9: (2,4)
}

def countKeys(start, depth):
  if (depth == 0):
    return 1;

  total = 0;

  for key in keypad[start]:
    total = total + countKeys(key, depth - 1);
  
  return total;

cache = {}

def countKeysMemo(start, depth):

  if (start,depth) in cache.keys():
    return cache[(start,depth)];
  else:
    if (depth == 0):
      cache[(start,depth)] = 1;
      return 1;
    
    total = 0;

    for key in keypad[start]:
      total = total + countKeysMemo(key, depth - 1);
  
  cache[(start,depth)] = total;
  return total;
