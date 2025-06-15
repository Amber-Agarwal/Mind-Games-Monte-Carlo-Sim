# Mind Games - Assignment Solutions

This repository contains my solutions to Assignment 1 of the course **MTL106: Probability and Stochastic Processes** at IIT Delhi, taught by Professor S. Dharmaraja. The assignment focuses on analyzing optimal strategies for a chess-like game between Alice and Bob, where players can choose different playing styles (aggressive, balanced, defensive) each round.

## Problem Overview
Alice and Bob play a game where they can choose their playing style each round. The outcome probabilities depend on:
- Current scores of both players
- Their chosen playing styles
- Bob's strategy (predictable or random)

The assignment involves solving probability problems and implementing Monte Carlo simulations to validate strategies.

## Solution Files

### Problem 1: Both players always attack
1. **ques_1.py** - Probability and expectation calculations
   - `calc_prob()`: Probability of specific win counts
   - `calc_expectation()`: Expected value of the sum of outcomes
   - `calc_variance()`: Variance of the sum of outcomes

### Problem 2: Bob reacts to previous outcomes
1. **ques_2a.py** - Greedy strategy implementation
2. **ques_2b.py** - Non-greedy vs greedy strategy comparison
3. **ques_2c.py** - Expected rounds for Alice to reach T wins

### Problem 3: Bob plays randomly
1. **ques_3a.py** - Strategy to maximize current round points
2. **ques_3b.py** - Strategy to maximize points over T future rounds

## Key Insights

### Problem 1
- Implemented dynamic programming to calculate win probabilities
- Derived expectation and variance using combinatorial methods
- Used modular arithmetic for large numbers (mod 10⁹+7)

### Problem 2
- Designed adaptive strategies based on game history
- Implemented payoff matrix that evolves with scores
- Compared greedy vs non-greedy strategies using DP

### Problem 3
- Formulated optimal strategies against random opponent
- Implemented value iteration for finite horizon decision making
- Validated results through Monte Carlo simulations

## How to Run
Each solution file is self-contained and can be run independently:
```bash
python ques_1.py
python ques_2a.py
python ques_2b.py
python ques_2c.py
python ques_3a.py
python ques_3b.py
```

## Results
| Problem | Key Result |
|---------|------------|
| 1a      | Probability for (96,25) wins: 0.08639488 |
| 1b      | Expectation for t=25: 333333344 |
| 2c      | Expected rounds for 25 wins: ~7 |

## Theoretical Notes
See [MTL106_A1.pdf](MTL106_A1.pdf) for complete problem statements and [mtl106assigntheory_2_.pdf](mtl106assigntheory_2_.pdf) for my handwritten solutions and derivations.

Developed by **Amber Agarwal**
