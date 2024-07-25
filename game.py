import requests

r = requests.get("https://sudoku-api.vercel.app/api/dosuku?query={newboard(limit:1){grids{value}}}")
print(r.json())
r = requests.get("https://sudoku-api.vercel.app/api/dosuku?query={newboard(limit:1){grids{difficulty}}}")
print(r.json())
print([[set() for i in range(3)] for j in range(3)])