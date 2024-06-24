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
    result = set()
    for i in range(n):
      for c in parenthesizations(i):
        for d in parenthesizations(n - i - 1):
          result.add("(" + c + ")" + d)
    return result

def product_orders(n):
  """
  Returns a set of all possible ways to multiply of n elements.

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
    result = set()
    for i in range(2,n-1):
      for c in product_orders(i):
        for d in product_orders(n - i):
          left = c if i == 1 else "(" + c + ")"
          right = d if n - i - 1 == 1 else "(" + d + ")"
          result.add(left + "*" + right)
    for c in product_orders(n-1):
      if n-1 == 1:
        result.add(c + "*?")
        result.add("?*" + c)
      else:
        result.add("?*(" + c+ ")")
        result.add("(" + c + ")*?")
    return result

def permutations_avoiding_231(n):
  """
  Returns a set of permutations of length n avoiding the pattern 2-3-1.
  
  Parameters:
    n (int): The length of the permutation.
  
  Returns:
    A set of permutations of length n that do not contain the pattern 2-3-1.
  
  Example:
  >>> permutations_avoiding_231(4)
  {(1, 2, 3, 4), (1, 2, 4, 3), (1, 3, 2, 4), (1, 4, 2, 3), (1, 4, 3, 2), (2, 1, 3, 4), (2, 1, 4, 3), (3, 1, 2, 4), (3, 2, 1, 4), (4, 1, 2, 3), (4, 1, 3, 2), (4, 2, 1, 3), (4, 3, 1, 2), (4, 3, 2, 1)}
  """
  return [p for p in itertools.permutations(range(1, n + 1), n)
    if not any(p[k] < p[i] < p[j] for i,j,k in itertools.combinations(range(n),3))]

def triangulations(n):
  """
  Returns a set of all possible triangulations of an n-sided polygon. A triangulation
  is represented as a tuple of internal edges. Vertices are labeled 0 through n-1 clockwise.

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
  
  result = set()
  # Case 1: There is an edge of the form (0,i).
  for i in range(2, n-1):
    for T in triangulations(i+1):
      for S in triangulations(n-i+1):
        triangulation = [(0,i)] + list(T) + [(j+(i-1) if j > 0 else 0, (k+(i-1))) for (j,k) in S]
        result.add(tuple(sorted(triangulation)))
  # Case 2: There is no edge of the form (0,i) so there must be an edge (1,n-1).
  for T in triangulations(n-1):
    triangulation = [(1,n-1)] + [(j+1,k+1) for (j,k) in T]
    result.add(tuple(sorted(triangulation)))
  return result