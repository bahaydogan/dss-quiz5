import numpy as np

THETA = 0.5  # fixed threshold
ALPHA = 0.1  # learning rate

X = np.array([
    [1, 0, 0],  # idx=0 -> X1=1, X2=0, X3=0
    [1, 0, 1],  # idx=1 -> X1=1, X2=0, X3=1
    [1, 1, 0],  # idx=2 -> X1=1, X2=1, X3=0
    [1, 1, 1],  # idx=3 -> X1=1, X2=1, X3=1
], dtype=float)
y = np.array([1, 1, 1, 0], dtype=int)

# weights after iteration4:
W = np.array([0.7, -0.2, -0.1], dtype=float)

start_iter = 5
print("Continuing training from iteration5 with initial weights:")

idx = 0
iteration = start_iter
errors_by_iter = {}
epoch = 0
while True:
    epoch += 1
    # print("Epoch " + str(epoch) +"\n")
    epoch_errors = 0
    for _ in range(4):
        x = X[idx]
        target = int(y[idx])
        net = float(np.dot(W, x))
        pred = 1 if net > THETA else 0
        E = target - pred
        errors_by_iter[iteration] = E


        print(f"iteration{iteration}: Net={net:.1f} Predicted={pred} E={E}", end="")

        # weight update
        if E != 0:
            W = W + ALPHA * E * x
            print(f" then: W1={W[0]:.1f} W2={W[1]:.1f} W3={W[2]:.1f}")
            epoch_errors += 1
            # print("epoch_errors: " + str(epoch_errors)+ "\n")
        else:
            print("")


        iteration += 1
        idx = (idx + 1) % 4


    if epoch_errors == 0:
        # print("Bir epoch tamamen hatasızsa dur")
        break


print(f"Eğitim durdu: epoch={epoch}, son iterasyon=iteration{iteration-1}")
print(f"Final weights: W1={W[0]:.1f}, W2={W[1]:.1f}, W3={W[2]:.1f}")

# guess 'Y' for X1=0.5, X2=0.5, X3=0.5
x_new = np.array([0.5, 0.5, 0.5], dtype=float)
net_new = float(np.dot(W, x_new))
pred_new = 1 if net_new > THETA else 0

print("\nGuess Y for X1=0.5, X2=0.5, X3=0.5")
print(f"Net={net_new:.2f} Threshold={THETA} => Y={pred_new}")
