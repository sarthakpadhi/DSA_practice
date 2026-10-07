# 1983E. I Love Balls

- **Link:** https://codeforces.com/problemset/problem/1983/E
- **Difficulty:** CF Div round, problem E
- **Topics:** Math, Expected Value, Modular Inverse
- **Date solved:** 2026-10-07
- **Status:** ⚠️ Not verified against official samples (could not reach Codeforces to pull them)

## Problem
There are `n` balls, `k` of which are special, each with a value. Alice and Bob alternate turns,
each drawing a uniformly random remaining ball and adding its value to their score. Drawing a
special ball lets the same player draw again (if any balls remain); drawing a non-special ball
passes the turn. Alice goes first. Return each player's expected total score, modulo 1e9+7.

## Approach
Only the relative order of the balls matters, and only the non-special balls actually decide
whose turn it is. This reduces to a "dots and dashes" style counting argument:

- Line up the `m = n - k` non-special balls in draw order (0-indexed). Turns only pass on a
  non-special draw, so the ball at an even position is taken by Alice and the ball at an odd
  position is taken by Bob.
- The `k` special balls each fall into one of the `m + 1` gaps around the non-special balls
  (gap 0 is before the first non-special draw, gap 1 is between the 1st and 2nd, and so on).
  Whoever's turn it is during that gap takes the ball, and gap "ownership" alternates starting
  with Alice at gap 0 — same even/odd idea as above, just shifted by one slot.

So each ball's destination only depends on which of its equally-likely slots it lands in:

- A non-special ball has `m` equally likely positions, of which `(m + 1) // 2` belong to Alice.
  So Alice's expected share of the non-special sum `T` is `T * ((m + 1) // 2) / m`.
- A special ball has `m + 1` equally likely gaps, of which `m // 2 + 1` belong to Alice. So
  Alice's expected share of the special sum `S` is `S * (m // 2 + 1) / (m + 1)`.

`alice = S * (m // 2 + 1) / (m + 1) + T * ((m + 1) // 2) / m` (all divisions as modular inverses),
and `bob = total - alice`.

## Complexity
- **Time:** O(n) per test case (sum + two modular exponentiations)
- **Space:** O(n) to hold the values

## Notes / Gotchas
- All arithmetic is mod 1e9+7; division is done via `pow(x, MOD - 2, MOD)`.
- `m == 0` (no non-special balls) is a special case: all value goes to whoever ends up with it
  before any pass, so the fallback returns `(total, 0)`.
- Not yet checked against the official sample I/O — confirm on Codeforces before trusting this.
