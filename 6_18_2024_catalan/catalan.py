import itertools

def parenthesizations(n):
  """
  Returns a set of all possible parenthesizations of length n.

  Parameters:
    n (int): The length of the parenthesizations.

  Returns:
    A set of strings, where each inner string represents a valid parenthesization of length n.
  
  Example:
  >>> parenthesizations(3)
  {'((()))', '(()())', '(())()', '()(())', '()()()'}
  """
  if n == 0:
    return {""}
  else:
    output = set()
    parenthesizations_helper("", n, n, output)
    return output

"""
res - result string
open - number of open parenthesis
close - number of close parenthesis
output - output set
"""
def parenthesizations_helper(res, open, close, output):
  if open == 0 and close == 0:
    output.add(res)
  else:
    if open > 0:
      parenthesizations_helper(res + "(", open - 1, close, output)
    if close != open:
      parenthesizations_helper(res + ")", open, close - 1, output)             
      
def product_orders(n):
  """
  Returns a list of all possible ways to multiply of n elements.

  Parameters:
    n (int): The number of elements multiplied.

  Returns:
    A set of strings where each string represents a way to multiply n elements.
  
  Example:
  >>> product_orders(4)
  {'((?*?)*?)*?', '(?*(?*?))*?', '(?*?)*(?*?)', '?*((?*?)*?)', '?*(?*(?*?))'}
  """
  if n == 0:
    return {""}
  elif n == 1:
    return {"?"}
  elif n == 2:
    return {"?*?"}
  else:
    output = set()
    return product_orders_helper(n, n)
    

def product_orders_helper(n, overall_length):
  if n == 1:
    return {"?"}
  output = set()
  for i in range(1, n):
    for j in product_orders_helper(i, overall_length):
      for k in product_orders_helper(n - i, overall_length):
        new_string = j + "*" + k
        if new_string[0] == "?" or new_string[len(new_string) - 1] == "?":
          if n < overall_length:
            new_string = "(" + new_string + ")"
        output.add(new_string)
  return output

def permutations_avoiding_231(n):
  """
  Returns a list of permutations of length n avoiding the pattern 2-3-1.
  
  Parameters:
    n (int): The length of the permutation.
  
  Returns:
    A list of permutations of length n that do not contain the pattern 2-3-1.
  
  Example:
  >>> permutations_avoiding_231(4)
  {(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (3, 1, 2, 4), (3, 2, 1, 4), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 3, 1, 2), (4, 3, 2, 1)}
  """
  
  if n < 3:
    return set(itertools.permutations(range(1, n+1)))
  else:
    perms = itertools.permutations(range(1, n+1))
    output = set()
    found = False
    for perm in perms:
      found = False
      for i in range(n - 2):
        first = perm[i]
        for j in range(i + 1, n - 1):
          second = perm[j]
          for k in range(j + 1, n):
            third = perm[k]
            if second > first and first > third:
              found = True
              break
          if found:
            break
        if found:
          break
      if not found:
        output.add(perm)
    return output     
    

def triangulations(n):
  """
  Returns a list of all possible triangulations of an n-sided polygon. A triangulation
  is represented as a list of internal edges. Vertices are labeled 0 through n-1 clockwise.

  Parameters:
    n (int): The number of sides of the polygon.

  Returns:
    A set of tuple of pairs, where each pair represents an internal edge in the triangulation.
  
  Example:
  >>> triangulations(3)
  {((0, 3), (1, 3)), ((1, 4), (2, 4)), ((1, 3), (1, 4)), ((0, 2), (2, 4)), ((0, 2), (0, 3))}
  """
  if n < 3:
    return set()
  elif n == 3:
    return {tuple()}
  else:
    vertices = list(range(n - 1))
    output = set()
    for i in range (n - 2):
      output = output.union(triangulation_helper(i, vertices))
    return output


def triangulation_helper(start, vertices):
  length = len(vertices)
  vertices = sorted(vertices)
  output = set()
  if len(vertices) == 3:
    return {((vertices[(start) % length], vertices[(start + 1) % length]), (vertices[start % length], vertices[(start + 2) % length]))}
  else:
    triangle = ((vertices[(start) % length], vertices[(start + 1) % length]), (vertices[start % length], vertices[(start + 2) % length]))
    del vertices[(start + 1) % length]
    output.add(triangle)
    return output.union(triangulation_helper(start, vertices))
  
    