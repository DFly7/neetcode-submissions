# Problem Notes

Personal notes on problems I found hard, want to revisit, or spotted a useful pattern in.

---

## Hard Problems

Problems that took multiple attempts or needed a rethink.

| Problem | Category | Why it was hard |
|:---|:---|:---|
| | | |

---

## Revisit

Problems to come back to and redo from scratch.

| Problem | Category | Notes |
|:---|:---|:---|
| [top-k-elements-in-list](../Data%20Structures%20%26%20Algorithms/top-k-elements-in-list) | Arrays & Hashing | Right idea but missed key patterns — redo from scratch |
| [valid-sudoku](../Data%20Structures%20%26%20Algorithms/valid-sudoku) | Arrays & Hashing | Revisit the 3x3 box index trick |

---

## Close But No Cigar

Right idea, wrong execution — off-by-one, missed an edge case, slightly wrong data structure, etc.

| Problem | Category | What I got wrong |
|:---|:---|:---|
| [string-encode-and-decode](../Data%20Structures%20%26%20Algorithms/string-encode-and-decode) | Arrays & Hashing | Used `#word#length` instead of `length#word` — breaks when length > 9 (multi-digit). Flipping the order fixed it, rest of the solution was spot on |
| [products-of-array-discluding-self](../Data%20Structures%20%26%20Algorithms/products-of-array-discluding-self) | Arrays & Hashing | Knew the prefix/postfix pattern but included the current element in each — prefix[i] and postfix[i] must exclude index i |
| [valid-sudoku](../Data%20Structures%20%26%20Algorithms/valid-sudoku) | Arrays & Hashing | Close but didn't get `(row // 3, col // 3)` to map a cell to its 3x3 box index |

---

## Patterns & Tricks

Reusable ideas worth remembering.

| Pattern | When to use it |
|:---|:---|
| | |
