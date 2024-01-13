def best_score(a_dictionary):
    if not a_dictionary:
        return (None)
    biggest = 0
    biggest_key = ""
    for key, value in a_dictionary.items():
        if value > biggest:
            biggest = value
            biggest_key = key
    return (biggest_key)

a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))