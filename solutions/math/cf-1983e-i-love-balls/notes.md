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
Split the total value into the special-ball sum `S` and non-special-ball sum `T`. Each special
ball is drawn before the game can hinge on turn order in the same way, so its expected share for
Alice reduces to a fixed fraction independent of draw order. The non-special balls get split
based on parity of turns among the `m = n - k` non-special draws. Alice's expected score is
computed as a combination of `S` and `T` scaled by modular-inverse fractions; Bob's is the
remainder (`total - alice`).

## Complexity
- **Time:** O(n) per test case (sum + two modular exponentiations)
- **Space:** O(n) to hold the values

## Notes / Gotchas
- All arithmetic is mod 1e9+7; division is done via `pow(x, MOD - 2, MOD)`.
- `m == 0` (no non-special balls) is a special case: all value goes to whoever ends up with it
  before any pass, so the fallback returns `(total, 0)`.
- Not yet checked against the official sample I/O — confirm on Codeforces before trusting this.
