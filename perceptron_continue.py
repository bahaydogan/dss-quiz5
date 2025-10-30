THETA = 0.5  # fixed threshold
ALPHA = 0.1  # learning rate

# Data
X1 = [1, 1, 1, 1]
X2 = [0, 0, 1, 1]
X3 = [0, 1, 0, 1]
Y =  [1, 1, 1, 0]

# Start from the end of iteration4
# iteration4 ended with: W1=0.7, W2=-0.2, W3=-0.1
W = [0.7, -0.2, -0.1]

start_iter = 5
end_iter = 14  # run analysis up to iteration 14 (no stop on 4 consecutive zeros)

print("Task1: iteration5–14 analizi (dört ardışık E=0 koşul olarak kullanılmıyor)")

# Iterate over the dataset cyclically for a fixed number of iterations
idx = 0  # next sample index to use (0..3). After iteration4, next is sample 1 (index 0)
errors_by_iter = {}
for iteration in range(start_iter, end_iter + 1):
    x = [X1[idx], X2[idx], X3[idx]]
    target = Y[idx]
    net = W[0]*x[0] + W[1]*x[1] + W[2]*x[2]
    pred = 1 if net > THETA else 0
    E = target - pred
    errors_by_iter[iteration] = E

    # Print iteration log
    print(f"iteration{iteration}: Net={net:.1f} Predicted={pred} E={E}", end="")

    # Update if error
    if E != 0:
        # perceptron update: W += alpha * E * x
        W[0] += ALPHA * E * x[0]
        W[1] += ALPHA * E * x[1]
        W[2] += ALPHA * E * x[2]
        print(f" then: W1={W[0]:.1f} W2={W[1]:.1f} W3={W[2]:.1f}")
    else:
        print("")

    # Advance dataset index
    idx = (idx + 1) % 4

# Verification for the sought answer
expected_block = [11, 12, 13, 14]
all_zero = all(errors_by_iter.get(i, None) == 0 for i in expected_block)
print(
    f"Aranan cevap kontrolü: iterations {expected_block} için E=0 -> {all_zero}"
)
print(f"Final weights after iteration{end_iter}: W1={W[0]:.1f}, W2={W[1]:.1f}, W3={W[2]:.1f}")

# Compute Y for X1=X2=X3=0.5 using final weights
x_new = [0.5, 0.5, 0.5]
net_new = W[0]*x_new[0] + W[1]*x_new[1] + W[2]*x_new[2]
pred_new = 1 if net_new > THETA else 0

print("\nTask2: Infer Y for X1=0.5, X2=0.5, X3=0.5")
print(f"Net={net_new:.2f} Threshold={THETA} => Y={pred_new}")
