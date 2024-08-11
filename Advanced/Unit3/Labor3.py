favorite_foods = ["pizza", "sushi", "tacos", "salad", "fruit salad", "sandwich", "chicken parmesan", "spaghetti", "french fries", "ice cream"]

fruits = [food for food in favorite_foods if food.lower().endswith("fruit")]
print(fruits)

fruit_set = set(fruits)
print(fruit_set)

if "pizza" in fruit_set:
    print("Pizza is a fruit!")

veggies = {"carrots", "broccoli", "spinach", "kale"}
combined = veggies.union(set(["potatoes"]))
print(combined)