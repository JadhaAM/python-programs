class item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def FractionalKnapsack(W, arr):
    arr.sort(key=lambda x:(x.value/x.weight), reverse = True)
    finalValue = 0.0

    for item in arr:
        if item.weight <= W:
            W -= item.weight
            finalValue += item.value
        else:
            finalValue += item.value * W/ item.weight
            break

    return finalValue

if __name__ == "__main__":
    W = 50
    arr = [item(60, 10), item(100, 20), item(120, 30)]
    max_val = FractionalKnapsack(W, arr)
    print("Maximum value", max_val)