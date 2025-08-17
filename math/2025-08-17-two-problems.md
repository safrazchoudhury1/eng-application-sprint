# 2025-08-17 — Two Problems

## Problem 1 – Algebra
Given \(a + b = 12\) and \(ab = 35\).

**(a)** Compute \(a^2 + b^2\).

**(b)** Compute \(a^3 + b^3\).

**Solution:**
We have \(a^2 + b^2 = (a + b)^2 - 2ab = 144 - 70 = 74\).
Also \(a^3 + b^3 = (a + b)^3 - 3ab(a + b) = 1728 - 1260 = 468\).

## Problem 2 – Number Theory
Find the remainder when \(7^{2025}\) is divided by 100.

**Solution:**
Since \(7^4 = 2401 \equiv 1 \ (\bmod\ 100)\), the powers of \(7\) repeat every 20 in mod 100 because \(7^{20} = (7^4)^5 \equiv 1\). We can write \(2025 = 20 \times 101 + 5\), so \(7^{2025} \equiv 7^5 \ (\bmod\ 100)\). Computing \(7^5 = 16807\), the last two digits are 07, so the remainder is **7**.
