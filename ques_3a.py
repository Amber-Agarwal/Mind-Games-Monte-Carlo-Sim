import numpy as np
import time
class Alice:
    def __init__(self):
        self.past_play_styles = np.array([1,1])  
        self.results = np.array([1,0])           
        self.opp_play_styles = np.array([1,1])  
        self.points = 1
        self.opponent_points = len(self.results)-self.points
    def play_move(self):
        """
        Decide Alice's play style for the current round. Implement your strategy for 3a here.
        
        Returns: 
            0 : attack
            1 : balanced
            2 : defence

        """
        if 15*self.points<29*self.opponent_points:
            return 0
        else:
            return 2
        
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Alice's knowledge after each round based on the observed results.
        
        Returns:
            None
        """
        self.past_play_styles = np.append(self.past_play_styles, own_style)
        self.opp_play_styles = np.append(self.opp_play_styles, opp_style)
        self.results = np.append(self.results, result)
        self.points += result
        if result == 1:
            self.opponent_points += 0
        elif result == .5:
            self.opponent_points += .5
        else:
            self.opponent_points += 1

class Bob:
    def __init__(self):
        # Initialize numpy arrays to store Bob's past play styles, results, and opponent's play styles
        self.past_play_styles = np.array([1,1]) 
        self.results = np.array([0,1])          
        self.opp_play_styles = np.array([1,1])   
        self.points = 1

    def play_move(self):
        """
        Decide Bob's play style for the current round.

        Returns:
            Returns: 
            0 : attack
            1 : balanced
            2 : defence
        
        """
        move = np.random.choice([0, 1, 2])
        return move
        
    
    def observe_result(self, own_style, opp_style, result):
        """
        Update Bob's knowledge after each round based on the observed results.
        
        Returns:
            None
        """
        self.past_play_styles = np.append(self.past_play_styles, own_style)
        self.opp_play_styles = np.append(self.opp_play_styles, opp_style)
        self.results = np.append(self.results, result)
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
    


def monte_carlo(num_rounds):
    """
    Runs a Monte Carlo simulation of the game for a specified number of rounds.
    
    Returns:
        None
    """
    num_rounds-=2
    alice = Alice()
    bob = Bob()

    for _ in range(num_rounds):
        payoff_matrix = update_payoff_matrix(alice.points, bob.points)
        simulate_round(alice, bob, payoff_matrix)

    # After the simulation, you can analyze Alice's and Bob's performance
    print(f"Alice's Points: {alice.points}")
    print(f"Bob's Points: {bob.points}")
    #return alice.points
 

# Run Monte Carlo simulation with a specified number of rounds
if __name__ == "__main__":
    #start = time.perf_counter()
    monte_carlo(num_rounds=100000)
    #end = time.perf_counter()
    #print(end-start)
    
