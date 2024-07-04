import itertools


def parenthesizations(n):
    """
    Returns a set of all possible parenthesizations with n pairs of parentheses.

    Parameters:
        n (int): The number of pairs of parentheses.

    Returns:
        A set of strings, where each inner string represents a valid parenthesization of n pairs of parentheses.
    
    Example:
    >>> parenthesizations(3)
    {'((()))', '(()())', '(())()', '()(())', '()()()'}
    """
    if n == 0:
        return {""}
    elif n == 1:
        return {"()"}
    else:
        result = set()
        for i in range(n):
            for left in parenthesizations(i):
                for right in parenthesizations(n - 1 - i):
                    result.add(f"({left}){right}")
        return result

#print(parenthesizations(3))

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
  else:
    result = set()
    for i in range(1,n):
      left_orders = product_orders(i)
      right_orders = product_orders(n-i)
      for left in left_orders:
        for right in right_orders:
          if i == 1 and (n - i) == 1:
            result.add(f"{left}*{right}")
          elif i == 1:
            result.add(f"{left}*({right})")
          elif (n - i) == 1:
            result.add(f"({left})*{right}")
          else:
            result.add(f"({left})*({right})")
                           
    return result               
#print(product_orders(4))

def contains_perm_231(perm):
  """
  Returns True if the given permutation contains the pattern 2-3-1, False otherwise.
  
  Parameters:
    perm (list): A list representing a permutation.
  
  Returns:
    bool: True if the permutation contains the pattern 2-3-1, False otherwise.
  """
  n = len(perm)

  if n < 3:
    return False

  for i in range(n - 2):
    for j in range(i + 1, n - 1):
      for k in range(j + 1, n):
        if perm[i] < perm[j] and perm[k] < perm[i] and perm[k] < perm[j]:
          return True
  
  return False

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
  
  result = set()
  for perm in itertools.permutations(range(1,n+1)):
   if not contains_perm_231(perm): 
    result.add(perm)
  
  return result

#print(permutations_avoiding_231(4))


"I tried using your suggestions to improve the funcion, but the output ended up being"
"worse than what I initially had so I am submitting the code that I had emailed to you," 
"the code produces the correct triangulations, but is missing "
"(1,4)(2,4) for n = 5 the code produces the correct triangulations for n = 4 though."
def triangulations(n):
    """
    Returns a set of all possible triangulations of an n-sided polygon. A triangulation
    is represented as a tuple of internal edges. Vertices are labeled 0 through n-1 clockwise.

    Parameters:
        n (int): The number of sides of the polygon.

    Returns:
        A set of tuple of pairs, where each pair represents an internal edge in the triangulation.
    """
    if n < 3:
        return set()
    elif n == 3:
        return {tuple()}

    def edges_intersect(e1, e2):
        """
        Check if two edges (e1, e2) intersect.
        Edges are tuples of vertex indices, e.g., (i, j).
        """
        (a, b), (c, d) = e1, e2
        if a > b:
            a, b = b, a
        if c > d:
            c, d = d, c
        return (a < c < b and (d < a or d > b)) or (c < a < d and (b < c or b > d))

    triangulations_set = set()
    for i in range(n):
        for j in range(i + 1, n):
            if i + 1 == j or (i ==0 and j == n - 1):
                continue
            for t in triangulations(n - 1):
                new_edges = ((i, j),) + t
                valid = True
                for k in range(len(new_edges)):
                    for l in range(k + 1, len(new_edges)):
                        if edges_intersect(new_edges[k], new_edges[l]) or new_edges[k] == new_edges[l]:
                            valid = False
                            break
                    if not valid:
                        break
                if valid:
                    triangulations_set.add(new_edges)
    return triangulations_set

#print(triangulations(5))


print(parenthesizations(3))

print(product_orders(4))

print(permutations_avoiding_231(4))

print(triangulations(5))


import time
import matplotlib.pyplot as plt

def measure_time(func, n_values):
    times = []
    for n in n_values:
        start_time = time.time()
        func(n)
        end_time = time.time()
        times.append((n, end_time - start_time))
    return times

def plot_time_graph(times_list, titles):
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))

    for i, ax in enumerate(axs.flat):
        n_values, time_values = zip(*times_list[i])
        ax.plot(n_values, time_values)
        ax.set_xlabel('n')
        ax.set_ylabel('Time (seconds)')
        ax.set_title(titles[i])

    plt.tight_layout()
    plt.show()

n_values = range(1, 11)

# Measure the time it takes to generate the objects for each function
times_triangulations = measure_time(triangulations, n_values)
times_product_orders = measure_time(product_orders, n_values)
times_parenthesizations = measure_time(parenthesizations, n_values)
times_permutations_avoiding_231 = measure_time(permutations_avoiding_231, n_values)

# List of times and titles for each function
times_list = [times_triangulations, times_product_orders, times_parenthesizations, times_permutations_avoiding_231]
titles = [
    'Time required for triangulations',
    'Time required for product_orders',
    'Time required for parenthesizations',
    'Time required for permutations_avoiding_231'
]

# Plot the time graph for each function

plot_time_graph(times_list, titles)





