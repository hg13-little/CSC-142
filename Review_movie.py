import random 

class  Review: 
    def  __init__(self, rating, text):
        self.rating = rating
        self.text = text
        
    def pretty_print(self): 
        return f"Rating:  {self.rating}/5 - {self.text}"
    

class Movie: 
    def __init__(self, title,): 
        self.title = title 
        self.reviews = []

def add_review(self, review):
    self.reviews.append(review)

def average_rating(self): 
    if not self.reviews:
        return 0 
    total = sum(review.rating for review in self.reviews)
    return total / len(self.reviews)

def display_reviews(self):
    if not self.reviews:
        print("no reviews yet")
        return
    for review in self.reviews: 
        print(review.pretty_print())

def best_review(self):
        if not self.reviews:
            return None
        max_rating = max(review.rating for review in self.reviews)
        best = [r for r in self.reviews if r.rating == max_rating]
        return random.choice(best)

def worst_review(self):
        if not self.reviews:
            return None
        min_rating = min(review.rating for review in self.reviews)
        worst = [r for r in self.reviews if r.rating == min_rating]
        return random.choice(worst)

#driver code

movie = Movie("The Matrix")

movie.add_review(Review(5, "Mind-bending and visually stunning."))
movie.add_review(Review(4, "Great movie, but confusing at times."))
movie.add_review(Review(5, "Amazing concept and execution."))
movie.add_review(Review(2, "Too hard to follow but a cool style"))

print(f"Movie: {movie.title}")
print(f"Average Rating: {movie.average_rating():.2f}")

print("\nAll Reviews:")
movie.display_reviews()

best = movie.best_review()
worst = movie.worst_review()

print("\nBest Review:")
if best:
    print(best.pretty_print())

print("\nWorst Review:")
if worst:
    print(worst.pretty_print())