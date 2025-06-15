# Payoff Matrix based on Alice's and Bob's strategy choices
import numpy as np
import time
M=1000000007

def mod_add(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return (a+b)%M

def mod_multiply(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return (a*b)%M

def mod_divide(a, b):
    a=(a%M+M)%M
    b=(b%M+M)%M
    return mod_multiply(a, pow(b, M-2, M))
class Alice:
    def __init__(self):
        self.past_play_styles = np.array([1,1])  
        self.results = np.array([1,0])           
        self.opp_play_styles = np.array([1,1])  
        self.points = 1
        self.opponent_points = 1

        
    def play_move(self,tot_rounds):
        """
        Decide Alice's play style for the current round. Implement your strategy for 3a here.
        
        Returns: 
            0 : attack
            1 : balanced
            2 : defence

        """
        payoff_matrix = update_payoff_matrix(self.points, self.opponent_points)
        attack_expectation = 0
        balanced_expectation =0
        defence_expectation =0
        for i in range(3):
            p_win, p_draw, p_lose = payoff_matrix[0][i]

            # Recursively calculate future points based on current outcomes
            new_alice_win = (1+dp_table[int(2*self.points + 2)][int(2*self.opponent_points)][tot_rounds - 1])
            new_draw = 1/2 + dp_table[int(2*self.points+1)][int(2*self.opponent_points+1)][tot_rounds-1]  # Draw adds 0.5 to both
            new_alice_loss = dp_table[int(2*self.points)][int(2*self.opponent_points+2)][tot_rounds - 1]

            # Expected points for this move
            attack_expectation += (p_win * new_alice_win + p_draw * new_draw + p_lose * new_alice_loss)

        for i in range(3):
            p_win, p_draw, p_lose = payoff_matrix[1][i]

            # Recursively calculate future points based on current outcomes
            new_alice_win = (1+dp_table[int(2*self.points + 2)][int(2*self.opponent_points)][tot_rounds - 1])
            new_draw = 1/2 + dp_table[int(2*self.points+1)][int(2*self.opponent_points+1)][tot_rounds-1]  # Draw adds 0.5 to both
            new_alice_loss = dp_table[int(2*self.points)][int(2*self.opponent_points+2)][tot_rounds - 1]

            # Expected points for this move
            balanced_expectation += (p_win * new_alice_win + p_draw * new_draw + p_lose * new_alice_loss)

        for i in range(3):
            p_win, p_draw, p_lose = payoff_matrix[2][i]

            # Recursively calculate future points based on current outcomes
            new_alice_win = (1+dp_table[int(2*self.points + 2)][int(2*self.opponent_points)][tot_rounds - 1])
            new_draw = 1/2 + dp_table[int(2*self.points+1)][int(2*self.opponent_points+1)][tot_rounds-1]  # Draw adds 0.5 to both
            new_alice_loss = dp_table[int(2*self.points)][int(2*self.opponent_points+2)][tot_rounds - 1]

            # Expected points for this move
            defence_expectation += (p_win * new_alice_win + p_draw * new_draw + p_lose * new_alice_loss)
    
        if defence_expectation>=balanced_expectation and defence_expectation>=attack_expectation:
            return 2

        elif defence_expectation>=balanced_expectation and attack_expectation>=defence_expectation:
            return 0
        elif balanced_expectation>=defence_expectation and attack_expectation>=balanced_expectation:
            return 0
        elif balanced_expectation>=defence_expectation and attack_expectation<=balanced_expectation:
            return 1
        
    def play_move_greedy(self):
        """
        Decide Alice's play style for the current round. Implement your strategy for 3a here.
        
        Returns: 
            0 : attack
            1 : balanced
            2 : defence

        """
        if 29*self.points<15*self.opponent_points:
            return 2
        else:
            return 0            

            

        
        
    
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
def update_payoff_matrix(na, nb): # updating the payoff matrix
    total_points = na + nb
    p1_attack_attack = nb / total_points
    p3_attack_attack = na / total_points

    payoff_matrix = [
        [[p1_attack_attack, 0, p3_attack_attack], [7/10, 0, 3/10], [5/11, 0, 6/11]],  # Alice Attack
        [[3/10, 0, 7/10], [1/3, 1/3, 1/3], [3/10, 1/2, 1/5]],                        # Alice Balanced
        [[6/11, 0, 5/11], [1/5, 1/2, 3/10], [1/10, 4/5, 1/10]]                       # Alice Defense
    ]
    return payoff_matrix

# Initialize DP table (adjust dimensions as needed)
dp_table = [[[-1 for _ in range(202)] for _ in range(202)] for _ in range(202)]


def optimal_strategy(na, nb, tot_rounds): # strategy based on the dp approach which is deterministic
    """
    Calculate the optimal strategy for Alice maximize her points in the future rounds
    given the current score of Alice(na) and Bob(nb) and the total number of rounds(tot_rounds).
    
    Return the answer in form of a list [p1, p2, p3],
    where p1 is the probability of playing Attacking
    p2 is the probability of playing Balanced
    p3 is the probability of playing Defensive
    """
    expected_points(tot_rounds)
    payoff_matrix = update_payoff_matrix(na,nb)
    attack_expectation = 0
    balanced_expectation =0
    defence_expectation =0
    for i in range(3):
        p_win, p_draw, p_lose = payoff_matrix[0][i]

        # Recursively calculate future points based on current outcomes
        new_alice_win = (1+dp_table[int(2*na + 2)][int(2*nb)][tot_rounds - 1])
        new_draw = 1/2 + dp_table[int(2*na+1)][int(2*nb+1)][tot_rounds-1]  # Draw adds 0.5 to both
        new_alice_loss = dp_table[int(2*na)][int(2*nb+2)][tot_rounds - 1]

        # Expected points for this move
        attack_expectation += (p_win * new_alice_win + p_draw * new_draw + p_lose * new_alice_loss)

    for i in range(3):
        p_win, p_draw, p_lose = payoff_matrix[1][i]

        # Recursively calculate future points based on current outcomes
        new_alice_win = (1+dp_table[int(2*na + 2)][int(2*nb)][tot_rounds - 1])
        new_draw = 1/2 + dp_table[int(2*na+1)][int(2*nb+1)][tot_rounds-1]  # Draw adds 0.5 to both
        new_alice_loss = dp_table[int(2*na)][int(2*nb+2)][tot_rounds - 1]

        # Expected points for this move
        balanced_expectation += (p_win * new_alice_win + p_draw * new_draw + p_lose * new_alice_loss)

    for i in range(3):
        p_win, p_draw, p_lose = payoff_matrix[2][i]

        # Recursively calculate future points based on current outcomes
        new_alice_win = (1+dp_table[int(2*na + 2)][int(2*nb)][tot_rounds - 1])
        new_draw = 1/2 + dp_table[int(2*na+1)][int(2*nb+1)][tot_rounds-1]  # Draw adds 0.5 to both
        new_alice_loss = dp_table[int(2*na)][int(2*nb+2)][tot_rounds - 1]

        # Expected points for this move
        defence_expectation += (p_win * new_alice_win + p_draw * new_draw + p_lose * new_alice_loss)

    if defence_expectation>=balanced_expectation and defence_expectation>=attack_expectation:
        return [0,0,1]

    elif defence_expectation>=balanced_expectation and attack_expectation>=defence_expectation:
        return [1,0,0]
    elif balanced_expectation>=defence_expectation and attack_expectation>=balanced_expectation:
        return [1,0,0]
    elif balanced_expectation>=defence_expectation and attack_expectation<=balanced_expectation:
        return [0,1,0]
    
def play_move_greedy(self): # greedy strategy for carrying out the game
    """
    Decide Alice's play style for the current round. Implement your strategy for 3a here.
    
    Returns: 
        0 : attack
        1 : balanced
        2 : defence

    """
    if 29*self.points<15*self.opponent_points:
        return 2
    else:
        return 0   


def optimal_strategy_1(na, nb, tot_rounds): # to calculate the expectation using the dp_table made
    """
    Calculate the optimal strategy for Alice to maximize her points in future rounds
    given the current score of Alice (na) and Bob (nb), and the total number of rounds (tot_rounds).

    Return the maximum expected points Alice can earn.
    """
    if tot_rounds == 0:
        return 1  # Base case: No rounds left, 0
    
    if dp_table[int(2*na)][int(2*nb)][tot_rounds] != -1:  # Check if result is already computed
        return dp_table[int(2*na)][int(2*nb)][tot_rounds]

    payoff_matrix = update_payoff_matrix(na, nb)
    max_expected_points = -float('inf')
    
    # Explore all possible moves (0: Attack, 1: Balanced, 2: Defense)
    for alice_move in range(3):
        t_expected_points = 0
        for bob_move in range(3):  # Bob plays randomly, so check all moves
            p_win, p_draw, p_lose = payoff_matrix[alice_move][bob_move]

            # Recursively calculate future points based on current outcomes
            new_alice_win = (1+optimal_strategy_1(na + 1, nb, tot_rounds - 1))
            new_draw = (1/2 + optimal_strategy_1(na + .5, nb + .5, tot_rounds - 1))  # Draw adds 0.5 to both
            new_alice_loss = optimal_strategy_1(na, nb + 1, tot_rounds - 1)

            # Expected points for this move
            n_expected_points = (p_win * new_alice_win + p_draw * new_draw + p_lose * new_alice_loss)
            t_expected_points += n_expected_points / 3  # Divide by 3 for random bob_move

        
        max_expected_points = max(max_expected_points, t_expected_points)

    dp_table[int(2*na)][int(2*nb)][tot_rounds] = max_expected_points  # Memoize result
    return max_expected_points

def expected_points(tot_rounds): # generating maximum expected value using our deterministic dp approach
    """
    Given the total number of rounds (tot_rounds), calculate the expected points that Alice can score,
    assuming that Alice plays optimally in each round.
    """
    return optimal_strategy_1(1,1,tot_rounds-2)

def simulate_round(alice, bob, payoff_matrix,tot_rounds):
    """
    Simulates a single round of the game between Alice and Bob.
    
    Returns:
        None
    """
    alice_move = alice.play_move(tot_rounds)
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

def simulate_round_greedy(alice, bob, payoff_matrix):
    """
    Simulates a single round of the game between Alice and Bob.
    
    Returns:
        None
    """
    alice_move = alice.play_move_greedy()
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
    expected_points(num_rounds)
    alice = Alice()
    bob = Bob()

    for i in range(num_rounds):
        payoff_matrix = update_payoff_matrix(alice.points, bob.points)
        simulate_round(alice, bob, payoff_matrix,i)

    # After the simulation, you can analyze Alice's and Bob's performance
    #print(f"Alice's Points: {alice.points}")
    #print(f"Bob's Points: {bob.points}")
    return alice.points

def monte_carlo_greedy(num_rounds): # monte carlo simulation for the greedy round as done in part 3a
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
        simulate_round_greedy(alice, bob, payoff_matrix)

    # After the simulation, you can analyze Alice's and Bob's performance
    # print(f"Alice's Points: {alice.points}")
    # print(f"Bob's Points: {bob.points}")
    return alice.points
#t1 = time.perf_counter()

v1=0

T = 25
k = 100000//T
for i in range(100000//T):
    v1+= monte_carlo_greedy(num_rounds=T)
print(v1/k,expected_points(T))    # comparing the expectation value of the greedy and the dp approach


print(expected_points(25))

# t2 = time.perf_counter()
# print(t2-t1)
