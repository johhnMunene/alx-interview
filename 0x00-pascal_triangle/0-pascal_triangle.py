def pascal_triangle(n):
  """
  Generates Pascal's Triangle of size n.

  Args:
      n: The number of rows in the Pascal's Triangle.

  Returns:
      A list of lists representing the Pascal's Triangle.
      Returns an empty list if n <= 0.
  """

  if n <= 0:
    return []

  triangle = []
  # First row is always [1]
  triangle.append([1])

  # Iterate for subsequent rows (up to n-1)
  for i in range(1, n):
    prev_row = triangle[i-1]  # Get the previous row
    current_row = []
    # First and last element of each row are always 1
    current_row.append(1)
    # Calculate elements in the middle using previous row
    for j in range(1, i):
      current_row.append(prev_row[j-1] + prev_row[j])
    current_row.append(1)  # Last element is always 1
    triangle.append(current_row)

  return triangle
