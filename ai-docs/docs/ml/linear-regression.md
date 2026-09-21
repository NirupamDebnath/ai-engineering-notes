# Linear Regression

Status: Done

This note started from CS229 Lecture 2 and can be expanded over time with more math, examples, notebooks, and implementation details. It includes the core linear regression math and practical Python implementations using NumPy and scikit-learn.

## Big Picture

Linear regression is a supervised learning algorithm for predicting a continuous value.

Examples:

- Predict house price from size, number of rooms, and location-derived features.
- Predict exam score from hours studied.
- Predict temperature from time and weather measurements.

The core idea is to fit a linear function:

$$
h_\theta(x) = \theta^T x
$$

where:

- \(x\) is the feature vector.
- \(\theta\) is the parameter vector learned from data.
- \(h_\theta(x)\) is the prediction.

The notation \(h_\theta\) means "hypothesis parameterized by \(\theta\)".

## Training Data Notation

A training set contains \(m\) examples:

$$
\{(x^{(1)}, y^{(1)}), (x^{(2)}, y^{(2)}), \ldots, (x^{(m)}, y^{(m)})\}
$$

For each example:

- \(x^{(i)}\) is the input feature vector for example \(i\).
- \(y^{(i)}\) is the target value for example \(i\).
- \(m\) is the number of training examples.
- \(n\) is the number of input features, not counting the intercept feature.

To include an intercept term, add a constant feature:

$$
x_0 = 1
$$

So if the original example has two features:

$$
x = [\text{size}, \text{rooms}]
$$

then the model uses:

$$
x = [1, \text{size}, \text{rooms}]
$$

and:

$$
h_\theta(x) = \theta_0 + \theta_1 x_1 + \theta_2 x_2
$$

## Cost Function

The model should choose \(\theta\) so that predictions are close to the true values. For linear regression, CS229 uses the squared error cost:

$$
J(\theta) = \frac{1}{2} \sum_{i=1}^{m} \left(h_\theta(x^{(i)}) - y^{(i)}\right)^2
$$

The \(\frac{1}{2}\) is included because it cancels out when differentiating the square.

For one training example, the error is:

$$
h_\theta(x^{(i)}) - y^{(i)}
$$

The cost sums the squared errors across the full training set.

## Least Mean Squares

The linear regression fitting problem is also called least mean squares, or LMS.

The objective:

$$
\min_\theta J(\theta)
$$

means:

Find the parameter values \(\theta\) that minimize the squared prediction error.

There are two common ways to solve this:

- Gradient descent: iterative optimization.
- Normal equation: direct closed-form solution.

## Gradient Descent

Gradient descent repeatedly updates parameters in the direction that decreases the cost.

General update rule:

$$
\theta_j := \theta_j - \alpha \frac{\partial}{\partial \theta_j} J(\theta)
$$

where:

- \(\alpha\) is the learning rate.
- \(j\) indexes a parameter.
- \(\frac{\partial}{\partial \theta_j} J(\theta)\) is the gradient for that parameter.

For linear regression:

$$
\frac{\partial}{\partial \theta_j} J(\theta)
=
\sum_{i=1}^{m}
\left(h_\theta(x^{(i)}) - y^{(i)}\right)x_j^{(i)}
$$

### Partial Derivative Breakdown

Start with the squared error cost:

$$
J(\theta) =
\frac{1}{2}
\sum_{i=1}^{m}
\left(h_\theta(x^{(i)}) - y^{(i)}\right)^2
$$

To update one parameter \(\theta_j\), take the partial derivative with respect to that parameter:

$$
\frac{\partial}{\partial \theta_j} J(\theta)
=
\frac{\partial}{\partial \theta_j}
\frac{1}{2}
\sum_{i=1}^{m}
\left(h_\theta(x^{(i)}) - y^{(i)}\right)^2
$$

Move the derivative inside the sum:

$$
=
\sum_{i=1}^{m}
\frac{\partial}{\partial \theta_j}
\frac{1}{2}
\left(h_\theta(x^{(i)}) - y^{(i)}\right)^2
$$

Use the chain rule. Let the prediction error for example \(i\) be:

$$
e^{(i)} = h_\theta(x^{(i)}) - y^{(i)}
$$

Then:

$$
\frac{\partial}{\partial \theta_j}
\frac{1}{2}(e^{(i)})^2
=
e^{(i)}
\frac{\partial e^{(i)}}{\partial \theta_j}
$$

Because \(y^{(i)}\) is a constant, only the hypothesis depends on \(\theta_j\):

$$
\frac{\partial e^{(i)}}{\partial \theta_j}
=
\frac{\partial h_\theta(x^{(i)})}{\partial \theta_j}
$$

For one example, the hypothesis expands to:

$$
h_\theta(x^{(i)})
=
\theta_0x_0^{(i)}
+ \theta_1x_1^{(i)}
+ \cdots
+ \theta_jx_j^{(i)}
+ \cdots
+ \theta_nx_n^{(i)}
$$

The only term that changes with \(\theta_j\) is \(\theta_jx_j^{(i)}\), so:

$$
\frac{\partial h_\theta(x^{(i)})}{\partial \theta_j}
=
x_j^{(i)}
$$

Substitute back:

$$
\frac{\partial J(\theta)}{\partial \theta_j}
=
\sum_{i=1}^{m}
\left(h_\theta(x^{(i)}) - y^{(i)}\right)x_j^{(i)}
$$

Intuition:

- \(h_\theta(x^{(i)}) - y^{(i)}\) is the prediction error for example \(i\).
- \(x_j^{(i)}\) measures how much feature \(j\) contributed for that example.
- The sum aggregates that feature's error contribution across all training examples.
- The learning rate \(\alpha\) controls how large a correction step to take.

### Real-Life Example: House Price Prediction

Suppose the model predicts house price in thousands of dollars from house size in thousands of square feet.

Use one feature plus an intercept:

$$
x^{(i)} = [x_0^{(i)}, x_1^{(i)}]
$$

where:

- \(x_0^{(i)} = 1\) is the intercept feature.
- \(x_1^{(i)}\) is house size in thousands of square feet.
- \(y^{(i)}\) is the real sale price in thousands of dollars.

The hypothesis is:

$$
h_\theta(x^{(i)}) = \theta_0x_0^{(i)} + \theta_1x_1^{(i)}
$$

Assume the current model is:

$$
\theta_0 = 50, \qquad \theta_1 = 100
$$

So the model currently predicts:

$$
\text{price} = 50 + 100 \cdot \text{size}
$$

Now use two training examples:

| Example | Size \(x_1^{(i)}\) | Actual price \(y^{(i)}\) | Prediction \(h_\theta(x^{(i)})\) | Error \(h_\theta(x^{(i)}) - y^{(i)}\) |
| --- | ---: | ---: | ---: | ---: |
| 1 | 1.0 | 180 | 150 | -30 |
| 2 | 2.0 | 300 | 250 | -50 |

For the size parameter \(\theta_1\), the gradient is:

$$
\frac{\partial J(\theta)}{\partial \theta_1}
=
\sum_{i=1}^{m}
\left(h_\theta(x^{(i)}) - y^{(i)}\right)x_1^{(i)}
$$

Substitute the two examples:

$$
\frac{\partial J(\theta)}{\partial \theta_1}
=
(-30)(1.0) + (-50)(2.0)
=
-130
$$

The negative gradient means the current \(\theta_1\) is too small. The model is underpredicting, especially for larger houses, so the size coefficient should increase.

If \(\alpha = 0.001\), the update is:

$$
\theta_1 :=
100 - 0.001(-130)
=
100.13
$$

After this step, the model puts slightly more weight on house size:

$$
\text{price} = 50 + 100.13 \cdot \text{size}
$$

The same idea applies to \(\theta_0\), except the feature value is always \(x_0^{(i)} = 1\). That update adjusts the baseline prediction up or down.

So the LMS update becomes:

$$
\theta_j :=
\theta_j -
\alpha
\sum_{i=1}^{m}
\left(h_\theta(x^{(i)}) - y^{(i)}\right)x_j^{(i)}
$$

All parameters should be updated using the same old parameter vector. In implementation, compute all gradients first, then update \(\theta\).

## Batch Gradient Descent

Batch gradient descent uses all training examples to compute each update.

```text
repeat until convergence:
    for each parameter j:
        gradient[j] = sum over all examples of prediction_error * feature_j
    for each parameter j:
        theta[j] = theta[j] - alpha * gradient[j]
```

Characteristics:

- Stable direction because each step uses the whole dataset.
- Can be slow for very large datasets.
- Cost should usually decrease each iteration if the learning rate is reasonable.

### Batch Gradient Descent By Hand

This version implements the update rule directly with Python lists. It is useful for learning because every line maps back to the math:

$$
\theta_j := \theta_j - \alpha \sum_{i=1}^{m}
\left(h_\theta(x^{(i)}) - y^{(i)}\right)x_j^{(i)}
$$

```python
def predict_one(theta, row):
    return sum(parameter * feature for parameter, feature in zip(theta, row))


def batch_gradient_descent(X, y, learning_rate=0.01, iterations=1000):
    # X should already include the intercept column x_0 = 1.
    m = len(X)
    n = len(X[0])
    theta = [0.0 for _ in range(n)]

    for _ in range(iterations):
        gradients = [0.0 for _ in range(n)]

        # Batch step: use every training example before updating theta.
        for row, target in zip(X, y):
            prediction = predict_one(theta, row)
            error = prediction - target

            for j in range(n):
                gradients[j] += error * row[j]

        # Update all parameters together using the old theta values.
        for j in range(n):
            theta[j] -= learning_rate * gradients[j]

    return theta
```

Example with one feature:

```python
# Features: [intercept, house_size_in_1000_sqft]
X = [
    [1.0, 1.0],
    [1.0, 2.0],
    [1.0, 3.0],
]

# Prices in thousands of dollars
y = [180.0, 300.0, 420.0]

theta = batch_gradient_descent(
    X,
    y,
    learning_rate=0.01,
    iterations=1000,
)

print(theta)
```

Example output:

```text
[59.837, 120.072]
```

This is close to the line:

$$
\text{price} = 60 + 120 \cdot \text{size}
$$

How the code maps to the math:

| Code | Math |
| --- | --- |
| `prediction = predict_one(theta, row)` | \(h_\theta(x^{(i)})\) |
| `error = prediction - target` | \(h_\theta(x^{(i)}) - y^{(i)}\) |
| `gradients[j] += error * row[j]` | Adds \(\left(h_\theta(x^{(i)}) - y^{(i)}\right)x_j^{(i)}\) |
| `theta[j] -= learning_rate * gradients[j]` | Applies \(\theta_j := \theta_j - \alpha \frac{\partial J}{\partial \theta_j}\) |

The key detail is that all gradients are computed first, then all \(\theta\) values are updated together. If \(\theta_0\) is updated before computing \(\theta_1\)'s gradient, the update no longer uses one consistent old parameter vector.

## Stochastic Gradient Descent

Stochastic gradient descent, or SGD, updates parameters using one example at a time.

For each example \((x^{(i)}, y^{(i)})\):

$$
\theta_j :=
\theta_j -
\alpha
\left(h_\theta(x^{(i)}) - y^{(i)}\right)x_j^{(i)}
$$

Characteristics:

- Faster updates on large datasets.
- Noisier path toward the minimum.
- Often good enough in practice, especially when data is large.

## Matrix Form

Let:

$$
X =
\begin{bmatrix}
- (x^{(1)})^T - \\
- (x^{(2)})^T - \\
\vdots \\
- (x^{(m)})^T -
\end{bmatrix}
$$

where \(X\) has shape \(m \times (n+1)\) after adding the intercept column.

Let:

$$
y =
\begin{bmatrix}
y^{(1)} \\
y^{(2)} \\
\vdots \\
y^{(m)}
\end{bmatrix}
$$

Predictions for all examples:

$$
X\theta
$$

Cost:

$$
J(\theta) = \frac{1}{2}(X\theta - y)^T(X\theta - y)
$$

Gradient:

$$
\nabla_\theta J(\theta) = X^T(X\theta - y)
$$

Batch gradient descent in vector form:

$$
\theta := \theta - \alpha X^T(X\theta - y)
$$

## Normal Equation

The normal equation gives a direct solution without choosing a learning rate:

$$
\theta = (X^T X)^{-1}X^T y
$$

This comes from setting the gradient to zero:

$$
X^T(X\theta - y) = 0
$$

Expand:

$$
X^TX\theta - X^Ty = 0
$$

Move terms:

$$
X^TX\theta = X^Ty
$$

Multiply by \((X^TX)^{-1}\):

$$
\theta = (X^TX)^{-1}X^Ty
$$

Use the normal equation when:

- The number of features is small enough.
- You want an exact least-squares solution.
- Matrix inversion is computationally acceptable.

Use gradient descent when:

- The number of features is large.
- The dataset is large.
- You want an iterative method that scales better.
- You are using an optimizer-based library model such as `SGDRegressor`.

## Probabilistic Interpretation

Linear regression can also be justified probabilistically.

Assume the target is generated as:

$$
y^{(i)} = \theta^T x^{(i)} + \epsilon^{(i)}
$$

where \(\epsilon^{(i)}\) is random noise.

Assume the noise follows a Gaussian distribution:

$$
\epsilon^{(i)} \sim \mathcal{N}(0, \sigma^2)
$$

Then:

$$
y^{(i)} | x^{(i)}; \theta \sim \mathcal{N}(\theta^T x^{(i)}, \sigma^2)
$$

The likelihood of observing the dataset is:

$$
L(\theta) =
\prod_{i=1}^{m}
\frac{1}{\sqrt{2\pi}\sigma}
\exp
\left(
-\frac{(y^{(i)} - \theta^T x^{(i)})^2}{2\sigma^2}
\right)
$$

Maximizing this likelihood is equivalent to minimizing:

$$
\sum_{i=1}^{m}
(y^{(i)} - \theta^T x^{(i)})^2
$$

So least squares is not just a convenient loss. It is the maximum likelihood estimate under Gaussian noise assumptions.

## Locally Weighted Linear Regression

Standard linear regression learns one global linear model.

Locally weighted linear regression instead fits a different model for each query point \(x\), giving nearby training examples higher weight.

Weighted cost:

$$
J(\theta) =
\frac{1}{2}
\sum_{i=1}^{m}
w^{(i)}
\left(h_\theta(x^{(i)}) - y^{(i)}\right)^2
$$

A common weight function:

$$
w^{(i)} =
\exp
\left(
-\frac{(x^{(i)} - x)^2}{2\tau^2}
\right)
$$

where:

- \(x\) is the query point.
- \(x^{(i)}\) is a training point.
- \(\tau\) is the bandwidth parameter.

If \(\tau\) is small, only very close points matter. If \(\tau\) is large, many points matter and the result becomes closer to ordinary linear regression.

Locally weighted regression is non-parametric in the sense that it does not compress learning into one fixed parameter vector. It keeps the training data and fits a local model at prediction time.

## Practical Implementation Details

Important implementation choices:

- Add an intercept column of ones before training.
- Scale features when using gradient descent, especially if feature ranges differ.
- Start with small random or zero parameters.
- Track cost over iterations.
- If cost increases or becomes `nan`, reduce the learning rate.
- Use the normal equation for small datasets and gradient descent for larger datasets.
- In everyday Python, use scikit-learn for training, evaluation, scaling, train/test splits, and pipelines.
- Use NumPy directly when you want to connect the implementation closely to the math.

Feature scaling example:

$$
x_j := \frac{x_j - \mu_j}{s_j}
$$

where:

- \(\mu_j\) is the mean of feature \(j\).
- \(s_j\) can be the standard deviation or range of feature \(j\).

## Practical Python Implementation

The most common way to implement linear regression in Python is to use scikit-learn. It gives you tested implementations, train/test splitting, preprocessing, metrics, and a consistent API across models.

Install dependencies:

```bash
pip install numpy scikit-learn
```

### scikit-learn Version

Use this style for normal application code and notebooks.

```python
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler


# Features: [house_size_sqft, bedrooms]
X = np.array(
    [
        [650.0, 1.0],
        [800.0, 2.0],
        [1200.0, 2.0],
        [1500.0, 3.0],
        [1800.0, 3.0],
        [2200.0, 4.0],
        [2600.0, 4.0],
        [3000.0, 5.0],
    ]
)

# Target: house price in thousands of dollars
y = np.array([72.0, 90.0, 135.0, 160.0, 190.0, 230.0, 270.0, 310.0])

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=7,
)

model = make_pipeline(
    StandardScaler(),
    LinearRegression(),
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Predictions:", predictions.round(2))
print("Actual:", y_test)
print("MAE:", round(mean_absolute_error(y_test, predictions), 2))
print("RMSE:", round(mean_squared_error(y_test, predictions) ** 0.5, 2))
print("R^2:", round(r2_score(y_test, predictions), 3))

new_house = np.array([[1600.0, 3.0]])
predicted_price = model.predict(new_house)[0]
print("Predicted price:", round(predicted_price, 2), "thousand dollars")
```

Why this is the usual implementation:

- `train_test_split` checks performance on data the model did not train on.
- `StandardScaler` keeps feature scales well behaved.
- `Pipeline` prevents preprocessing mistakes by fitting scaling only on training data.
- `LinearRegression` uses a tested least-squares solver internally.
- Metrics make the model's error visible instead of only printing coefficients.

### Reading Coefficients

Because the model uses `StandardScaler`, the learned coefficients are in scaled feature units. To inspect them:

```python
linear_model = model.named_steps["linearregression"]

print("Intercept:", linear_model.intercept_)
print("Coefficients:", linear_model.coef_)
```

The coefficients answer:

- How does predicted price change when a scaled feature increases by one unit?
- Which features are pushing predictions up or down?

They do not automatically prove causation. For example, house size and bedroom count are correlated, so coefficient signs can be surprising in a tiny dataset.

### NumPy Version Close To The Math

When the goal is to connect code to the normal equation, use NumPy directly. Prefer `np.linalg.lstsq` over manually computing \((X^TX)^{-1}X^Ty\), because solving least squares directly is more numerically stable than explicitly inverting a matrix.

```python
import numpy as np


# Features: [house_size_sqft, bedrooms]
X_raw = np.array(
    [
        [650.0, 1.0],
        [800.0, 2.0],
        [1200.0, 2.0],
        [1500.0, 3.0],
        [1800.0, 3.0],
        [2200.0, 4.0],
    ]
)
y = np.array([72.0, 90.0, 135.0, 160.0, 190.0, 230.0])

feature_means = X_raw.mean(axis=0)
feature_scales = X_raw.std(axis=0)
X_scaled = (X_raw - feature_means) / feature_scales

# Add the intercept column x_0 = 1.
X = np.c_[np.ones(X_scaled.shape[0]), X_scaled]

theta, residuals, rank, singular_values = np.linalg.lstsq(
    X,
    y,
    rcond=None,
)

new_house = np.array([[1600.0, 3.0]])
new_house_scaled = (new_house - feature_means) / feature_scales
new_house_with_intercept = np.c_[np.ones(new_house_scaled.shape[0]), new_house_scaled]
prediction = new_house_with_intercept @ theta

print("Theta:", theta.round(3))
print("Prediction:", round(prediction[0], 2), "thousand dollars")
print("Matrix rank:", rank)
```

Example output:

```text
Theta: [146.167  55.084  -0.504]
Prediction: 170.47 thousand dollars
Matrix rank: 3
```

This NumPy version directly matches:

$$
\theta = (X^TX)^{-1}X^Ty
$$

but avoids explicitly forming the inverse.

## How To Read The Parameters

When features are normalized before training:

- \(\theta_0\) is the prediction at average feature values.
- \(\theta_1\) is the effect of increasing house size by one standard deviation.
- \(\theta_2\) is the effect of increasing bedrooms by one standard deviation.

If you train without normalization, the parameters are easier to connect to raw units, but gradient descent is usually harder to tune. If features are correlated, coefficient signs and magnitudes can be surprising even when predictions are accurate.

## Common Failure Modes

| Problem | Symptom | Fix |
| --- | --- | --- |
| Learning rate too high | Cost increases or explodes | Reduce \(\alpha\) |
| Features not scaled | Slow or unstable convergence | Normalize features |
| Missing intercept | Model forced through origin | Add \(x_0 = 1\) |
| Singular \(X^TX\) | Normal equation fails | Remove duplicate features or use regularization |
| Outliers | Fitted line pulled strongly | Inspect data and consider robust methods |
| Nonlinear relationship | High bias, poor fit | Add polynomial/features or use another model |

## Study Checklist

- Understand the hypothesis \(h_\theta(x) = \theta^T x\).
- Know why the intercept feature \(x_0 = 1\) is added.
- Derive the gradient of the squared error cost.
- Implement batch gradient descent by hand.
- Implement linear regression with scikit-learn.
- Compare scikit-learn's least-squares fit with NumPy's `np.linalg.lstsq`.
- Explain why Gaussian noise leads to least squares.
- Understand how \(\tau\) controls locally weighted linear regression.

## Open Questions

- How does regularization change the normal equation?
- What happens when features are highly correlated?
- How can polynomial features turn linear regression into a nonlinear curve fit?
- When should mean squared error be replaced by another loss?
