'''
Write a Python function analyze_ratings(ratings) that takes a list of customer ratings (integers from 1 to 5) and returns another list containing the highest and lowest rating.    
'''

#approach 1
def analyze_ratings(ratings):

  max_rating = float('-inf')  
  lowest_rating = float('inf')

  for rating in ratings:
    if rating > max_rating:
      max_rating = rating
    if rating < lowest_rating :
      lowest_rating  = rating
  return [max_rating, lowest_rating ]
ratings = [4, 2, 5, 3, 1]
result = analyze_ratings(ratings)
print(result)

#approach 2


def analyze_ratings(ratings):
    highest_rating = max(ratings)
    lowest_rating = min(ratings)
    return [highest_rating, lowest_rating]
ratings = [4, 2, 5, 3, 1]
result = analyze_ratings(ratings)
print(result)

#approach 3

def analyze_ratings(ratings):
  sorting_rating = sorted(ratings)
  return [sorting_rating[-1], sorting_rating[0]]

ratings = [4, 2, 5, 3, 1]
result = analyze_ratings(ratings)
print(result)
