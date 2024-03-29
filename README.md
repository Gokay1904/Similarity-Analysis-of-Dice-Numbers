# Similarity-Analysis-of-Dice-Numbers
In libraries such as Matplotlib, Numpy, Seaborn, I developed a model that calculates the similarity ratio of a dice with Monte Carlo simulation (with iterations) and draws its linear regression line.

Optionally:

- You can change 
  - the number of dice surfaces
  - You can change iteration amounts.
  - You can change how many dice to roll at once
- **Important: Be careful not to exceed the numpy array capacity.**



<img  src = "https://user-images.githubusercontent.com/25516047/187803254-d154c187-7994-4b23-9975-aed688fc128f.PNG" align="center" height="640" width=auto />

Here, left section means probability factor in each iteration and its regression line.



Right section means probabilities of similarity.
- By increasing the number of iterations, ratios can be shifted to theoretical results.

Probability Factor:
- 0: if every dice is the same.
- 1: if at least 1 is the same.
- and so on...
