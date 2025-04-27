# CMPS 2200 Recitation 06
## Answers

**Name:**Mauricio Uribe
**Name:**Roberto Junqueira


Place all written answers from `recitation-07.md` here for easier grading.



- **2)**
- The work satisfies W = W(n-1) + W(n-2) + O(1).
Level 1: W = 1, Level 2: W = 2, Level 3: W = 4, and so on.
Each level doubles the work, and with n levels total, the work is leaf-dominated with W = O(2^n).

- **3)**
- The span satisfies S = S(n-1) + S(n-2) + O(1).
Level 1: span is 1, Level 2: span is 1, and so on.
Since the recursion is balanced, the span is O(n) because it decreases by one at each step.

- **4)**
- As n increases, the counts of the lower numbers increase significantly because higher Fibonacci numbers repeatedly call fib(2), fib(3), and so on. The larger the n, the more times the lower Fibonacci values are recomputed.

- **6)**
- The maximum number of times any fib value is called for a given n is one. This leads to a work of O(n), and since the algorithm iterates through the values, the span is also O(n).

- **8)**
- The maximum number of times a Fibonacci number is computed is once, leading to a work of O(n), and since there is an iterative for loop, the span is also O(n).
