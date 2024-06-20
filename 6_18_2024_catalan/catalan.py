import itertools
def parenthesizations(n):
  """
  Returns a set of all possible parenthesizations of length n.

  Parameters:
    n (int): The length of the parenthesizations.
  """
  """
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
      for left in parenthesizations(i):
          for right in parenthesizations(n - 1 - i):
              result.add('(' + left + ')' + right)
    return result


def product_orders(n):
  """
  Returns a set of all possible ways to multiply of n elements.

  Parameters:
    n (int):  The number of elements multiplied.
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
    for i in range(1, n):
      for left in product_orders(i):
          for right in product_orders(n - i):
              if left == '?':
                result.add(left+ '*(' + right + ')')
              elif right == '?':
                result.add('(' + left + ')*' + right)
              else:
                result.add('('+ left +')*('+ right+')')
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
  if n < 3:
    return set(itertools.permutations(range(1, n+1)))
  else:
    result = set()
    
    for i in set(itertools.permutations(range(1, n+1))):
      result.add(i)  
      for j in range(2, n):
          for k in range(j):
              if i[k] > i[j]:
                  for l in range(k+1, j):
                      if i[l] > i[j] and i[l] > i[k]:
                          result.add(i)
                          result.remove(i)
                        
    return result  



# Recording the time taken for each call
time_3 = end_time_3 - start_time_3
time_6 = end_time_6 - start_time_6
time_7 = end_time_7 - start_time_7
print(f"Time taken for permutations_avoiding_231(3): {time_3} seconds")
print(f"Time taken for permutations_avoiding_231(6): {time_6} seconds")
print(f"Time taken for permutations_avoiding_231(7): {time_7} seconds")
def triangulations(n):
  """
  Returns a set of all possible triangulations of an n-sided polygon. A triangulation
  is represented as a tuple of internal edges. Vertices are labeled 0 through n-1 clockwise.

  Parameters:
    n (int): The number of sides of the polygon.

  Returns:
    A set of tuple of pairs, where each pair represents an internal edge in the triangulation.
  
  Example:
  >>> triangulations(5)
  {((0, 3), (1, 3)), ((1, 4), (2, 4)), ((1, 3), (1, 4)), ((0, 2), (2, 4)), ((0, 2), (0, 3))}
  Note: wasn't able to get this to 100% work, but it is pretty close.
  """
  if n < 3:
    return set()
  elif n == 3:
    return {tuple()}
  else:
    result = set()
    for i in range(n-2):
      for j in range(i+2, n):
        if i != 0 or j != n-1:
          edge = (i, j)
          polygon1_size = j-i+1
          polygon2_size = n-(j-i)+1
          for polygon1 in triangulations(polygon1_size):
            for polygon2 in triangulations(polygon2_size):
              modfied_polygon2 = tuple()
              for (k,l) in polygon2:
                k= (i-k)%n
                l= (i-l)%n
                smaller = min(k,l)
                larger = max(k,l)
                modfied_polygon2 += ((smaller,larger),)
                result.add(tuple(sorted(polygon1 + (edge,) + ((smaller,larger),))))
          result.add(tuple(sorted(polygon1 + modfied_polygon2 + (edge,))))
    return result


