# 2025-08-17 — Two Problems

## Problem 1 – Algebra
Given \(a + b = 12\) and \(ab = 35\).

**(a)** Compute \(a^2 + b^2\).

**(b)** Compute \(a^3 + b^3\).

**Solution:**
\[
\begin{aligned}
a^2 + b^2 &= (a + b)^2 - 2ab = 12^2 - 2\cdot 35 = 74, \\
a^3 + b^3 &= (a + b)^3 - 3ab(a + b) = 12^3 - 3\cdot 35\cdot 12 = 468.
\end{aligned}
\]

**Why this works:** These identities rewrite power sums in terms of \(a+b\) and \(ab\),
values we already know, avoiding solving for \(a\) and \(b\) individually.

## Problem 2 – Number Theory
Find the remainder when \(7^{2025}\) is divided by 100.

**Solution:**
We note that \(7^4 = 2401 \equiv 1 \pmod{100}\), so powers of 7 repeat every
four in this modulus.  Since \(2025 = 4\cdot 506 + 1\),
\(7^{2025} \equiv 7^1 \equiv 7 \pmod{100}\).

**Why this works:** When \(7^4 \equiv 1\) the multiplicative order of 7 modulo
100 divides 4, letting us reduce any exponent modulo 4.  Reducing the exponent
keeps calculations manageable while preserving the remainder.
