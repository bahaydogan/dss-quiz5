# Perceptron Learning Algorithm - Results Summary

## Initial Parameters
- **W1** = 0.7 (starting from iteration 5)
- **W2** = -0.2
- **W3** = -0.1
- **Learning Rate (a)** = 0.1
- **Threshold (Ø)** = 0.5 (fixed)

## Training Data
| X1 | X2 | X3 | Y |
|----|----|----|---|
| 1  | 0  | 0  | 1 |
| 1  | 0  | 1  | 1 |
| 1  | 1  | 0  | 1 |
| 1  | 1  | 1  | 0 |

## Formula
- **NET** = W1*X1 + W2*X2 + W3*X3
- **Activation Function**: C = (NET > Ø ? 1 : 0)
- **Weight Update**: W_new = W_old + a * E * X

## Task 1: Training Results (Iterations 5-14)

### Iteration 5
- Sample 1: NET=0.7, Predicted=1, Actual=1, Error=0
- Sample 2: NET=0.6, Predicted=1, Actual=1, Error=0
- Sample 3: NET=0.5, Predicted=0, Actual=1, Error=1 → **Weights Updated**
- Sample 4: NET=0.6, Predicted=1, Actual=0, Error=-1 → **Weights Updated**
- **Total Error**: 2
- **Updated Weights**: W1=0.7, W2=-0.2, W3=-0.2

### Iteration 6
- Sample 1: NET=0.7, Predicted=1, Actual=1, Error=0
- Sample 2: NET=0.5, Predicted=0, Actual=1, Error=1 → **Weights Updated**
- Sample 3: NET=0.6, Predicted=1, Actual=1, Error=0
- Sample 4: NET=0.5, Predicted=0, Actual=0, Error=0
- **Total Error**: 1
- **Updated Weights**: W1=0.8, W2=-0.2, W3=-0.1

### Iteration 7
- Sample 1: NET=0.8, Predicted=1, Actual=1, Error=0
- Sample 2: NET=0.7, Predicted=1, Actual=1, Error=0
- Sample 3: NET=0.6, Predicted=1, Actual=1, Error=0
- Sample 4: NET=0.5, Predicted=0, Actual=0, Error=0
- **Total Error**: 0 (1st consecutive E=0)
- **Weights Unchanged**: W1=0.8, W2=-0.2, W3=-0.1

### Iteration 8
- Sample 1: NET=0.8, Predicted=1, Actual=1, Error=0
- Sample 2: NET=0.7, Predicted=1, Actual=1, Error=0
- Sample 3: NET=0.6, Predicted=1, Actual=1, Error=0
- Sample 4: NET=0.5, Predicted=0, Actual=0, Error=0
- **Total Error**: 0 (2nd consecutive E=0)
- **Weights Unchanged**: W1=0.8, W2=-0.2, W3=-0.1

### Iteration 9
- Sample 1: NET=0.8, Predicted=1, Actual=1, Error=0
- Sample 2: NET=0.7, Predicted=1, Actual=1, Error=0
- Sample 3: NET=0.6, Predicted=1, Actual=1, Error=0
- Sample 4: NET=0.5, Predicted=0, Actual=0, Error=0
- **Total Error**: 0 (3rd consecutive E=0)
- **Weights Unchanged**: W1=0.8, W2=-0.2, W3=-0.1

### Iteration 10
- Sample 1: NET=0.8, Predicted=1, Actual=1, Error=0
- Sample 2: NET=0.7, Predicted=1, Actual=1, Error=0
- Sample 3: NET=0.6, Predicted=1, Actual=1, Error=0
- Sample 4: NET=0.5, Predicted=0, Actual=0, Error=0
- **Total Error**: 0 (4th consecutive E=0)
- **Weights Unchanged**: W1=0.8, W2=-0.2, W3=-0.1

### Iteration 11 ✓
- Sample 1: NET=0.8, Predicted=1, Actual=1, Error=0
- Sample 2: NET=0.7, Predicted=1, Actual=1, Error=0
- Sample 3: NET=0.6, Predicted=1, Actual=1, Error=0
- Sample 4: NET=0.5, Predicted=0, Actual=0, Error=0
- **Total Error**: 0 ✓ (Target: 11th iteration E=0)
- **Weights Unchanged**: W1=0.8, W2=-0.2, W3=-0.1

### Iteration 12 ✓
- Sample 1: NET=0.8, Predicted=1, Actual=1, Error=0
- Sample 2: NET=0.7, Predicted=1, Actual=1, Error=0
- Sample 3: NET=0.6, Predicted=1, Actual=1, Error=0
- Sample 4: NET=0.5, Predicted=0, Actual=0, Error=0
- **Total Error**: 0 ✓ (Target: 12th iteration E=0)
- **Weights Unchanged**: W1=0.8, W2=-0.2, W3=-0.1

### Iteration 13 ✓
- Sample 1: NET=0.8, Predicted=1, Actual=1, Error=0
- Sample 2: NET=0.7, Predicted=1, Actual=1, Error=0
- Sample 3: NET=0.6, Predicted=1, Actual=1, Error=0
- Sample 4: NET=0.5, Predicted=0, Actual=0, Error=0
- **Total Error**: 0 ✓ (Target: 13th iteration E=0)
- **Weights Unchanged**: W1=0.8, W2=-0.2, W3=-0.1

### Iteration 14 ✓
- Sample 1: NET=0.8, Predicted=1, Actual=1, Error=0
- Sample 2: NET=0.7, Predicted=1, Actual=1, Error=0
- Sample 3: NET=0.6, Predicted=1, Actual=1, Error=0
- Sample 4: NET=0.5, Predicted=0, Actual=0, Error=0
- **Total Error**: 0 ✓ (Target: 14th iteration E=0)
- **Weights Unchanged**: W1=0.8, W2=-0.2, W3=-0.1

## Summary Table

| Iteration | Epoch Error | W1  | W2   | W3   | Consecutive Zeros |
|-----------|-------------|-----|------|------|-------------------|
| 5         | 2           | 0.7 | -0.2 | -0.2 | 0                 |
| 6         | 1           | 0.8 | -0.2 | -0.1 | 0                 |
| 7         | 0           | 0.8 | -0.2 | -0.1 | 1                 |
| 8         | 0           | 0.8 | -0.2 | -0.1 | 2                 |
| 9         | 0           | 0.8 | -0.2 | -0.1 | 3                 |
| 10        | 0           | 0.8 | -0.2 | -0.1 | 4                 |
| **11**    | **0**       | 0.8 | -0.2 | -0.1 | 5                 |
| **12**    | **0**       | 0.8 | -0.2 | -0.1 | 6                 |
| **13**    | **0**       | 0.8 | -0.2 | -0.1 | 7                 |
| **14**    | **0**       | 0.8 | -0.2 | -0.1 | 8                 |

### Key Results
- ✅ **Goal Achieved**: E=0 for iterations 11, 12, 13, and 14
- **Final Converged Weights**: W1=0.8, W2=-0.2, W3=-0.1
- **Convergence Iteration**: 7 (first E=0)
- **Total Consecutive Zeros**: 8 iterations (7-14)

---

## Task 2: Prediction for New Input

### Input
- X1 = 0.5
- X2 = 0.5
- X3 = 0.5

### Calculation
Using final weights: **W1=0.8, W2=-0.2, W3=-0.1**

```
NET = W1×X1 + W2×X2 + W3×X3
NET = 0.8×0.5 + (-0.2)×0.5 + (-0.1)×0.5
NET = 0.4 + (-0.1) + (-0.05)
NET = 0.25
```

### Activation
```
Y = 1 if NET > θ (0.5), else 0
Y = 1 if 0.25 > 0.5, else 0
Y = 0 (since 0.25 ≤ 0.5)
```

### **Result: Y = 0**

---

## Conclusion
The perceptron successfully converged after iteration 7 with final weights **W1=0.8, W2=-0.2, W3=-0.1**. The model achieved zero error for iterations 11, 12, 13, and 14 as required. For the test input (X1=0.5, X2=0.5, X3=0.5), the predicted output is **Y=0**.
- **Total Error**: 0 ✓ (Target: 14th iteration E=0)
- **Weights Unchanged**: W1=0.8, W2=-0.2, W3=-0.1

## Final Weights (Optimal Solution)
- **W1 = 0.8**
- **W2 = -0.2**
- **W3 = -0.1**

## Task 2: Prediction for New Input

**Input**: X1=0.5, X2=0.5, X3=0.5

**Calculation**:
```
NET = W1*X1 + W2*X2 + W3*X3
NET = 0.8*0.5 + (-0.2)*0.5 + (-0.1)*0.5
NET = 0.4 - 0.1 - 0.05
NET = 0.25
```

**Activation**:
```
Y = (NET > Ø ? 1 : 0)
Y = (0.25 > 0.5 ? 1 : 0)
Y = 0
```

### **Answer: Y = 0**

## Summary
- Training completed successfully for **14 total iterations** (iterations 5-14)
- Achieved 4 consecutive iterations with E=0 at iterations **11, 12, 13, and 14** ✓
- Final optimal weights: **W1=0.8, W2=-0.2, W3=-0.1**
- Prediction for (0.5, 0.5, 0.5): **Y = 0**

