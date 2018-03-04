def LRclassVector(inX,weights):
    from sigmoid import sigmoid
    prob = sigmoid(sum(inX * weights))
    if prob > 0.5 :
        return 1.0
    else:
        return 0.0