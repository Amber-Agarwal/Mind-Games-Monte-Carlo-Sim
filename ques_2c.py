import numpy as np
import time
class Alice:
    def __init__(self):
        self.past_play_styles = np.array([1, 1])  
        self.results = np.array([1, 0])           
        self.opp_play_styles = np.array([1, 1])  
        self.points = 1  # Alice's points
        self.wins = 1

    def play_move(self):
        if self.results[-1] == 0:
            return 1  # Bob won the previous round, play balanced
        if self.results[-1] == 0.5:
            return 0  # Previous round was a draw, play aggressive
        if self.results[-1] == 1:
            if ((len(self.results) - self.points) * 11) > (6 * (len(self.results))):
                return 0  # Play aggressive when behind
            else:
                return 2  # Play defensive when ahead

    def observe_result(self, own_style, opp_style, result):
        self.past_play_styles = np.append(self.past_play_styles, own_style)
        self.opp_play_styles = np.append(self.opp_play_styles, opp_style)
        self.results = np.append(self.results, result)
        self.points += result
        if result == 1:
            self.wins += 1

        
class Bob:
    def __init__(self):
        self.past_play_styles = np.array([1, 1]) 
        self.results = np.array([0, 1])          
        self.opp_play_styles = np.array([1, 1])   
        self.points = 1  # Bob's points
    
    def reset(self):
        self.past_play_styles = np.array([1, 1])  
        self.results = np.array([0, 1])           
        self.opp_play_styles = np.array([1, 1])  
        self.points = 1  # Reset points

    def play_move(self):
        if self.results[-1] == 1:
            return 2  # Bob won the last round, play defensively
        elif self.results[-1] == 0.5:
            return 1  # Draw, play balanced
        else:  
            return 0  # Lost last round, play aggressively
        
    def observe_result(self, own_style, opp_style, result):
        self.past_play_styles = np.append(self.past_play_styles, own_style)
        self.results = np.append(self.results, result)
        self.opp_play_styles = np.append(self.opp_play_styles, opp_style)
        self.points += result
 

def update_payoff_matrix(alice_points, bob_points):
    """
    Updates the payoff matrix based on the current points of Alice and Bob.

    Returns:
        The payoff matrix for the current round.
    """
    total_points = alice_points + bob_points
    p1_attack_attack = bob_points / total_points
    p3_attack_attack = alice_points / total_points

    payoff_matrix = [
    [[p1_attack_attack, 0, p3_attack_attack], [7/10, 0, 3/10], [5/11, 0, 6/11]],    # Alice Attack
    [[3/10, 0, 7/10], [1/3, 1/3, 1/3], [3/10, 1/2, 1/5]],                          # Alice Balanced
    [[6/11, 0, 5/11], [1/5, 1/2, 3/10], [1/10, 4/5, 1/10]]                         # Alice Defence
]

    
    return payoff_matrix


def simulate_round(alice, bob, payoff_matrix):
    """
    Simulates a single round of the game between Alice and Bob.
    
    Returns:
        None
    """
    alice_move = alice.play_move()
    bob_move = bob.play_move()
    p_win,p_draw,p_lose = payoff_matrix[alice_move][bob_move]
    result = np.random.choice([1, 0.5, -1], p=[p_win, p_draw, p_lose])
    if result == 1:
        alice_result = 1
        bob_result = 0
        alice.observe_result(alice_move, bob_move, alice_result)
        bob.observe_result(bob_move, alice_move, bob_result)
    elif result == 0.5:
        alice_result = 0.5
        bob_result = 0.5
        alice.observe_result(alice_move, bob_move, alice_result)
        bob.observe_result(bob_move, alice_move, bob_result)
    else:
        alice_result= 0
        bob_result = 1
        alice.observe_result(alice_move, bob_move, alice_result)
        bob.observe_result(bob_move, alice_move, bob_result)
    

def estimate_tau(T):
    """
    Estimate the expected value of the number of rounds taken for Alice to win 'T' rounds.
    Your total number of simulations must not exceed 10^5.

    Returns:
        Float: estimated value of E[tau]
    """

    counter = []
    count=0
    tally = 0
    k=0
    while (tally+k)<=100000: #  ensuring that the total iterations dont go over 1e5
        alice = Alice()# reset for new setup
        bob = Bob()# reset for new setup
        count = 0
        
        while alice.wins<T:

            payoff_matrix = update_payoff_matrix(alice.points, bob.points)
            simulate_round(alice, bob, payoff_matrix)
            count+=1
        counter.append(count)
        tally+=count
        k+=1
    sum = 0
    for i in range(k):
        sum += counter[i]
    return (sum/k)+2
print(estimate_tau(25))
    # After the simulation, you can analyze Alice's and Bob's performance
    # print(f"Alice's Points: {alice.points}")
    # print(f"Bob's Points: {bob.points}")
    
 
    
        
        
    