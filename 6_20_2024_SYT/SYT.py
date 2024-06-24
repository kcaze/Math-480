import itertools
import random

def is_valid_SYT(candidate):
  """
  Check if the given candidate tableau is a valid standard Young tableau.

  Parameters:
  - candidate (Tuple[Tuple[int]]): The tableau to be checked.

  Returns:
  - bool: True if the matrix is valid, False otherwise.

  The function checks if the given matrix is a valid SYT matrix by verifying that:
  1. The elements in each column are in strictly increasing order.
  2. The elements in each row are in strictly increasing order.

  Example:
  >>> is_valid_SYT(((1, 2, 3), (4, 5, 6), (7, 8, 9)))
  True
  >>> is_valid_SYT(((1, 2, 3), (5, 4), (6))
  False
  """
  for r in range(len(candidate)):
    for c in range(len(candidate[r])):
      # Not strict increase on columns
      if r < len(candidate)-1 and c < len(candidate[r+1]) and candidate[r+1][c] <= candidate[r][c]:
        return False
      # Not strict increase on rows
      if c < len(candidate[r]) - 1 and candidate[r][c+1] <= candidate[r][c]:
        return False
  return True

def reshape_perm(perm, shape):
  """
  Reshapes a permutation into a tableau based on the given shape.

  Parameters:
  - perm (Tuple[int]): The permutation to be reshaped.
  - shape (Tuple[int]): The shape of the resulting tableau as a weakly decreasing tuple of integers.

  Returns:
  - Tuple[Tuple[int]]: A tuple of tuples representing the reshaped permutation as a tableau.

  Example:
  >>> reshape_perm((1, 2, 3, 4, 5, 6), (3, 2, 1))
  ((1, 2, 3), (4, 5), (6,))
  """
  result = []
  index = 0
  for i in shape:
    result.append(tuple(perm[index:index + i]))
    index += i
  return tuple(result)

def SYTs(shape):
  """
  Generates SYTs (Standard Young Tableaux) of on the given shape.

  Parameters:
  - shape (Tuple[int]): The shape of the resulting SYTs as a tuple of integers.

  Returns:
  - List[Tuple[Tuple[int]]]: A list of valid SYTs generated based on the given shape.

  Example:
  >>> SYTs((2, 1))
  [((1, 2), (3,)), ((1, 3), (2,))]
  """

  n = sum(shape)
  results = []
  for perm in itertools.permutations(range(1, n + 1), n):
    candidate = reshape_perm(perm, shape)
    if is_valid_SYT(candidate):
      results.append(candidate)
  return results

def random_SYT(shape):
  """
  Generates a random Standard Young Tableau (SYT) of the given shape.

  Parameters:
  - shape (Tuple[int]): The shape of the resulting SYT as a tuple of integers.

  Returns:
  - Tuple[Tuple[int]]: A random valid SYT generated based on the given shape.

  This function generates a random permutation of numbers from 1 to n+1, where n is the sum of the elements in the `shape` tuple. It then reshapes the permutation into a tableau using the `reshape_perm` function. If the resulting tableau is not valid, it shuffles the permutation and tries again. The function continues this process until a valid SYT is found, and then returns the reshaped permutation as a tableau.

  Example:
  >>> random_SYT((2, 1))
  ((1, 2), (3,))
  """
  n = sum(shape)
  perm = list(range(1, n + 1))
  random.shuffle(perm)
  while not is_valid_SYT(reshape_perm(perm, shape)):
    random.shuffle(perm)
  return reshape_perm(perm, shape)

def random_SYT_2(shape):
  """
  Generates a random Standard Young Tableau (SYT) of the given shape.

  Parameters:
  - shape (Tuple[int]): The shape of the resulting SYT as a tuple of integers.

  Returns:
  - Tuple[Tuple[int]]: A random valid SYT generated based on the given shape.

  The function generates a random SYT by starting off with the all zeroes tableau and greedily filling in the numbers from 1 to n. The greedy generation is repeated until a valid SYT is produced.

  Example:
  >>> random_SYT_2((2, 1))
  ((1, 2), (3,))
  """
  n = sum(shape)
  syt = [[0 for i in range(c)] for c in shape]
  for i in range(1, n+1):
    spots = []
    for r in range(len(shape)):
      for c in range(shape[r]):
        if syt[r][c] == 0 and (r == 0 or syt[r-1][c] != 0) and (c == 0 or syt[r][c-1] != 0):
          spots.append((r,c))
    (r,c) = random.choice(spots)
    syt[r][c] = i
  return tuple([tuple(row) for row in syt])