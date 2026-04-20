def create_empty_prediction_list():
    return []


def create_flower1():
    return {
        "id": "flower1",
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2,
        "species": "setosa"
    }


def create_flower2():
    return {
        "id": "flower2",
        "sepal_length": 4.9,
        "sepal_width": 3.0,
        "petal_length": 1.4,
        "petal_width": 0.2,
        "species": "setosa"
    }


def create_dataset():
    flower1 = create_flower1()
    flower2 = create_flower2()
    return [flower1, flower2]


def get_threshold():
    return 2.5


def get_positive_label():
    return "setosa"


def get_negative_label():
    return "versicolor"


def predict_species(sample, threshold, positive_label, negative_label):
    if sample["petal_length"] < threshold:
        return positive_label
    else:
        return negative_label


def add_prediction(prediction_list, prediction):
    prediction_list.append(prediction)


def increase_total(total):
    return total + 1


def is_prediction_correct(predicted_label, true_label):
    return predicted_label == true_label


def increase_correct(correct):
    return correct + 1


def increase_wrong(wrong):
    return wrong + 1


def print_sample_result(sample, predicted_label):
    print(
        f'id={sample["id"]} | true={sample["species"]} | pred={predicted_label} | petal_length={sample["petal_length"]}'
    )


def calculate_accuracy(correct, total):
    return (correct / total) * 100


def print_summary(correct, wrong, total, accuracy, prediction_list):
    print(f"Correct: {correct}")
    print(f"Wrong: {wrong}")
    print(f"Total: {total}")
    print(f"Accuracy (%): {accuracy}")
    print(f"All predictions: {prediction_list}")


def process_dataset(dataset, threshold, positive_label, negative_label, prediction_list):
    correct = 0
    wrong = 0
    total = 0

    for sample in dataset:
        predicted_label = predict_species(sample, threshold, positive_label, negative_label)
        add_prediction(prediction_list, predicted_label)
        total = increase_total(total)

        if is_prediction_correct(predicted_label, sample["species"]):
            correct = increase_correct(correct)
        else:
            wrong = increase_wrong(wrong)

        print_sample_result(sample, predicted_label)

    return correct, wrong, total


def main():
    prediction_list = create_empty_prediction_list()
    dataset = create_dataset()
    threshold = get_threshold()
    positive_label = get_positive_label()
    negative_label = get_negative_label()

    correct, wrong, total = process_dataset(
        dataset,
        threshold,
        positive_label,
        negative_label,
        prediction_list
    )

    accuracy = calculate_accuracy(correct, total)
    print_summary(correct, wrong, total, accuracy, prediction_list)


main()


def calculate_power(base_val, exponent_val):
    result = base_val ** exponent_val
    return result

base_value = 2
exponent_value = 3

result = calculate_power(exponent_value, base_value)
print(result)
