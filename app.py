from flask import Flask, render_template

app = Flask(__name__)

def combinations():
    DieA = range(1, 7)
    DieB = range(1, 7)
    count = 0
    for i in DieA:
        for j in DieB:
            count += 1
    return count

def allcombinations():
    DieA = range(1, 7)
    DieB = range(1, 7)
    count = 0
    mat = []
    for i in DieA:
        temp = []
        for j in DieB:
            temp.append([i, j])
        mat.append(temp)
    return mat

def prob(DieA, DieB):
    combinations = []
    for i in DieA:
        for j in DieB:
            s = i + j
            combinations.append(s)

    count = {}
    probabilities = {}
    for i in combinations:
        count[i] = count.get(i, 0) + 1

    for i in range(2, 13):
        count_i = count.get(i, 0)
        probability_i = count_i / len(combinations)
        probabilities[i] = {"count": count_i, "probability": round(probability_i,5)}

    return probabilities

def undoom_dice(Die_A, Die_B):
    New_Die_A = [i - 3 if i > 4 else i for i in Die_A]
    New_Die_B = [j + 2 if j % 2 == 0 else j for j in Die_B]
    return sorted(New_Die_A), sorted(New_Die_B)

@app.route('/')
def index():
    total_combinations = combinations()

    DieA = range(1, 7)
    DieB = range(1, 7)

    original_probabilities = prob(DieA, DieB)
    all_possible_combinations = allcombinations()
    New_Die_A, New_Die_B = undoom_dice(list(DieA), list(DieB))
    modified_probabilities = prob(New_Die_A, New_Die_B)

    return render_template('index.html',
                           total_combinations=total_combinations,
                           all_possible_combinations=all_possible_combinations,
                           original_probabilities=original_probabilities,
                           modified_probabilities=modified_probabilities)

if __name__ == '__main__':
    app.run(debug=True)
