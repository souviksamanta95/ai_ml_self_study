# ISLR Study — Python

Working through *An Introduction to Statistical Learning with Applications in Python* (James, Witten, Hastie, Tibshirani).

## Structure

Each chapter folder contains up to three notebooks:

| Notebook | Purpose |
|---|---|
| `concepts.ipynb` | Walkthrough of the chapter's key ideas — theory, intuition, figures |
| `applied.ipynb` | Applied exercises from the end of the chapter |
| `implementation.ipynb` | From-scratch implementations (no sklearn) to build real intuition |

Not every chapter has all three — `implementation.ipynb` is only included where building from scratch is instructive.

## Chapters

| Folder | Chapter | Topics |
|---|---|---|
| `ch02_statistical_learning` | Ch 2 | Bias-variance tradeoff, MSE, KNN |
| `ch03_linear_regression` | Ch 3 | Simple/multiple regression, inference, model fit |
| `ch04_classification` | Ch 4 | Logistic regression, LDA, QDA, Naive Bayes, KNN |
| `ch05_resampling` | Ch 5 | Cross-validation, bootstrap |
| `ch06_linear_model_selection` | Ch 6 | Subset selection, ridge, lasso, PCR, PLS |
| `ch07_moving_beyond_linearity` | Ch 7 | Polynomials, step functions, splines, GAMs |
| `ch08_tree_methods` | Ch 8 | Decision trees, bagging, random forests, boosting |
| `ch09_svm` | Ch 9 | Maximal margin classifier, SVMs, SVR |
| `ch10_deep_learning` | Ch 10 | Neural nets, CNNs, RNNs, dropout, batch norm |
| `ch12_unsupervised` | Ch 12 | PCA, K-means, hierarchical clustering |

## Notes

- Ch 11 (Survival Analysis) skipped — lower priority for DS/ML goals.
- The `implementation.ipynb` notebooks use only numpy/pandas — no sklearn — to build real understanding.
- Applied notebooks use real datasets from the `ISLP` package where available.
