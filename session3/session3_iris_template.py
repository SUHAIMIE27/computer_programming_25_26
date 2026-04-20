<<<<<<< Updated upstream


# Session 2 continuity variables (Rule settings). Do not change these.
THRESHOLD = 2.0
FEATURE_NAME = "petal_length"
POSITIVE_LABEL = "setosa"
NEGATIVE_LABEL = "not_setosa"
LABEL_KEY = "species"



correct = 0      # Count of correct predictions
wrong = 0        # Count of wrong predictions
total = 0        # Total samples processed
y_pred_list = []  # List of all predictions made

=======
correct = 0
wrong = 0
total = 0
y_pred_list = []
>>>>>>> Stashed changes

flower1 = {
    "id": "flower1",
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2,
    "species": "setosa"
}

flower2 = {
    "id": "flower2",
    "sepal_length": 4.9,
    "sepal_width": 3.0,
    "petal_length": 1.4,
    "petal_width": 0.2,
    "species": "setosa"
}

dataset = [flower1, flower2]

threshold = 2.5
positive_label = "setosa"
negative_label = "versicolor"

for sample in dataset:
    if sample["petal_length"] < threshold:
        y_pred = positive_label
    else:
        y_pred = negative_label

    y_pred_list.append(y_pred)
    total += 1

    if y_pred == sample["species"]:
        correct += 1
    else:
        wrong += 1

    print(f'id={sample["id"]} | true={sample["species"]} | pred={y_pred} | petal_length={sample["petal_length"]}')

accuracy = (correct / total) * 100

print(f"Correct: {correct}")
print(f"Wrong: {wrong}")
print(f"Total: {total}")
print(f"Accuracy (%): {accuracy}")
print(f"All predictions: {y_pred_list}")