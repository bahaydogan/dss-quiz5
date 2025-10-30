import pandas as pd
import numpy as np

# Initial parameters
W1 = 0.7
W2 = -0.2
W3 = -0.1
a = 0.1  # learning rate
theta = 0.5  # threshold (fixed)

# Data
data = {
    'X1': [1, 1, 1, 1],
    'X2': [0, 0, 1, 1],
    'X3': [0, 1, 0, 1],
    'Y': [1, 1, 1, 0]
}

df = pd.DataFrame(data)

# Activation function
def activation(net, threshold):
    return 1 if net > threshold else 0

# Training function
def train_perceptron(W1, W2, W3, a, theta, df, start_iteration=5, target_iteration=14):
    iteration = start_iteration
    consecutive_zeros = 0
    results = []

    print("=" * 80)
    print(f"PERCEPTRON TRAINING - Starting from Iteration {start_iteration} to Iteration {target_iteration}")
    print("=" * 80)
    print(f"Initial Weights: W1={W1}, W2={W2}, W3={W3}")
    print(f"Learning Rate (a): {a}")
    print(f"Threshold (Ø): {theta}")
    print(f"Goal: Achieve E=0 for iterations 11, 12, 13, and 14")
    print("=" * 80)

    while iteration <= target_iteration:
        epoch_error = 0
        iteration_details = []

        for idx, row in df.iterrows():
            X1_val = row['X1']
            X2_val = row['X2']
            X3_val = row['X3']
            Y_actual = row['Y']

            # Calculate NET
            NET = W1 * X1_val + W2 * X2_val + W3 * X3_val

            # Apply activation function
            Y_predicted = activation(NET, theta)

            # Calculate error
            E = Y_actual - Y_predicted
            epoch_error += abs(E)

            # Store details
            iteration_details.append({
                'sample': idx + 1,
                'X1': X1_val,
                'X2': X2_val,
                'X3': X3_val,
                'NET': NET,
                'Predicted': Y_predicted,
                'Actual': Y_actual,
                'Error': E,
                'W1_before': W1,
                'W2_before': W2,
                'W3_before': W3
            })

            # Update weights if there's an error
            if E != 0:
                W1 = W1 + a * E * X1_val
                W2 = W2 + a * E * X2_val
                W3 = W3 + a * E * X3_val

        # Print iteration summary
        print(f"\nIteration {iteration}:")
        print("-" * 80)
        for detail in iteration_details:
            print(f"  Sample {detail['sample']}: X1={detail['X1']}, X2={detail['X2']}, X3={detail['X3']}")
            print(f"    NET = {detail['W1_before']:.1f}*{detail['X1']} + {detail['W2_before']:.1f}*{detail['X2']} + {detail['W3_before']:.1f}*{detail['X3']} = {detail['NET']:.1f}")
            print(f"    Predicted = {detail['Predicted']}, Actual = {detail['Actual']}, Error = {detail['Error']}")

        print(f"\n  Total Epoch Error: {epoch_error}")

        if epoch_error == 0:
            consecutive_zeros += 1
            print(f"  ✓ E=0 (consecutive count: {consecutive_zeros})")
            print(f"  Weights remain: W1={W1:.1f}, W2={W2:.1f}, W3={W3:.1f}")
        else:
            consecutive_zeros = 0
            print(f"  ✗ E={epoch_error} (resetting consecutive count)")
            print(f"  Updated Weights: W1={W1:.1f}, W2={W2:.1f}, W3={W3:.1f}")

        results.append({
            'iteration': iteration,
            'epoch_error': epoch_error,
            'W1': W1,
            'W2': W2,
            'W3': W3,
            'consecutive_zeros': consecutive_zeros
        })

        iteration += 1

    print("\n" + "=" * 80)
    print("TRAINING COMPLETE!")
    print("=" * 80)
    print(f"Final Weights: W1={W1:.1f}, W2={W2:.1f}, W3={W3:.1f}")
    print(f"Total Iterations: {target_iteration - start_iteration + 1} (iterations {start_iteration}-{target_iteration})")
    print(f"Consecutive zeros at end: {consecutive_zeros}")
    if consecutive_zeros >= 4:
        print(f"✓ Goal achieved: E=0 for iterations {target_iteration-3}, {target_iteration-2}, {target_iteration-1}, and {target_iteration}")
    print("=" * 80)

    return W1, W2, W3, results

# Task 1: Train the perceptron starting from iteration 5
print("\nTASK 1: Training Perceptron")
print("Previous iterations (1-4) summary:")
print("  Iteration 1: NET=0.6, P=1, E=0, Weights: W1=0.6, W2=-0.2, W3=-0.1")
print("  Iteration 2: NET=0.5, P=0, E=1, Weights: W1=0.7, W2=-0.2, W3=0.0")
print("  Iteration 3: NET=0.5, P=0, E=1, Weights: W1=0.8, W2=-0.1, W3=0.0")
print("  Iteration 4: NET=0.7, P=1, E=-1, Weights: W1=0.7, W2=-0.2, W3=-0.1")

final_W1, final_W2, final_W3, training_results = train_perceptron(W1, W2, W3, a, theta, df, start_iteration=5, target_iteration=14)

# Task 2: Predict Y for X1=0.5, X2=0.5, X3=0.5
print("\n\nTASK 2: Prediction for New Input")
print("=" * 80)
X1_test = 0.5
X2_test = 0.5
X3_test = 0.5

NET_test = final_W1 * X1_test + final_W2 * X2_test + final_W3 * X3_test
Y_test = activation(NET_test, theta)

print(f"Input: X1={X1_test}, X2={X2_test}, X3={X3_test}")
print(f"Using Final Weights: W1={final_W1:.1f}, W2={final_W2:.1f}, W3={final_W3:.1f}")
print(f"Threshold (Ø): {theta}")
print(f"\nNET = {final_W1:.1f}*{X1_test} + {final_W2:.1f}*{X2_test} + {final_W3:.1f}*{X3_test}")
print(f"NET = {NET_test:.2f}")
print(f"\nActivation Function: Y = (NET > Ø ? 1 : 0)")
print(f"Y = ({NET_test:.2f} > {theta} ? 1 : 0)")
print(f"\n>>> Predicted Y = {Y_test}")
print("=" * 80)

# Create summary table
print("\n\nSUMMARY TABLE")
print("=" * 80)
summary_df = pd.DataFrame(training_results)
print(summary_df.to_string(index=False))
print("=" * 80)

