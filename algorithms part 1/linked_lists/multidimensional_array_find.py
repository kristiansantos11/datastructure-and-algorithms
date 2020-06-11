colours = [["red", "blue", "orange"],["green", "black"],["gray"]]
c = "black"

x = next(((i, colour.index(c))
      for i, colour in enumerate(colours)
      if c in colour),
     None)

print(x[0])
