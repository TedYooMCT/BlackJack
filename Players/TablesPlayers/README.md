## Table Players: Basic and Expectancy
In this Blackjack project, we introduce two distinct strategies employed by the "Table Players":
the "Basic Strategy Player" and the "Expectancy Player."
These players rely on predefined tables that guide their decision-making during gameplay,
offering two different approaches to optimizing their Blackjack performance.

## Basic Strategy Player
### Description:
The "Basic Strategy" is a disciplined and mathematically grounded player who adheres to a predetermined strategy table.   
This table provides recommendations for each possible player hand based on the dealer's upcard.   
The Basic Strategy Player makes decisions that minimize the house edge and maximize the player's chances of success.

### Strategy Table:
The Basic Strategy Player relies on a table that outlines the best course of action for every possible combination of player hand and dealer upcard.
This table is a product of rigorous statistical analysis and probability calculations, making it a highly reliable reference.   
There are 3 tables - hard hand (no ace to use), soft hand (ace to use) and split hand (pair of some card).

## Expectancy Player
### Description:
The "Expectancy Player" takes a different approach by utilizing an expectancy table.
This table calculates the expected value of each possible action based on the current state of the game.
The Expectancy Player selects the action that maximizes expected gains, considering the probabilities of different outcomes.

### Expectancy Formula: 
The expectancy formula used by the Expectancy Player is as follows:
E(ξ) = Σ (P(ξ) * V(ξ))
where:
Σ represents the summation symbol, indicating the sum over all possible outcomes.
P(ξ) is the probability of a specific outcome ξ resulting from taking a certain action.
V(ξ) is the value associated with that outcome ξ.

### Table Calculation:
The Expectancy Player has a pre-calculated table that stores the expected values for each available action in various game scenarios.
These calculations are the result of extensive probability analysis and strategy optimization.
It's important to note that this player, its strategy, and the associated table were conceived and implemented as part of this project.
The Expectancy Player's strategy table uses the same format as the Basic Strategy Player (hard, soft and split)

## Results and Table Differences
### Results Analysis
Throughout the course of our experimentation, we conducted seven sets of games,
each consisting of 1000 rounds, to assess the performance of our Blackjack players
#### Basic Strategy Player
The results demonstrated a varying performance across different game sets. It achieved positive results in three out of seven sets,
showcasing its ability to consistently minimize losses and, at times, secure wins.
On average, the Basic Strategy Player showed resilience and an overall performance close to breakeven,
with a net result of -7 chips across all rounds.

#### Expectancy Player 
The Player displayed a more volatile performance, with fluctuating results in each game set.
It exhibited significant positive outcomes in two sets, highlighting its potential for substantial gains.
However, it also encountered periods of substantial losses in other sets, leading to negative net results.
The Expectancy Player's performance, had an average net result of -53 chips across all rounds.

#### Conclusion
The key takeaway from our experimentation is that both players exhibit unique strengths and weaknesses.
The Basic Strategy Player provides a stable and balanced approach, with a focus on minimizing losses,
while the Expectancy Player demonstrates moments of high profitability but with higher risk and volatility.
The choice between these players depends on the player's risk tolerance and strategic preferences,
underscoring the versatility of our Blackjack simulation environment.

### Table differences
#### Hard table: 
![Expectancy](https://github.com/Bar-A-94/BlackJack/blob/master/Players/TablesPlayers/Heat%20map%20tables/Expectancy%20Hard%20table.png)
![Basic](https://github.com/Bar-A-94/BlackJack/blob/master/Players/TablesPlayers/Heat%20map%20tables/Basic%20player%20Hard%20table.png)   

#### Soft table: 
![Expectancy](https://github.com/Bar-A-94/BlackJack/blob/master/Players/TablesPlayers/Heat%20map%20tables/Expectancy%20Soft%20table.png)
![Basic](https://github.com/Bar-A-94/BlackJack/blob/master/Players/TablesPlayers/Heat%20map%20tables/Basic%20player%20Soft%20table.png)   

#### Split table: 
![Expectancy](https://github.com/Bar-A-94/BlackJack/blob/master/Players/TablesPlayers/Heat%20map%20tables/Expectancy%20Split%20table.png)
![Basic](https://github.com/Bar-A-94/BlackJack/blob/master/Players/TablesPlayers/Heat%20map%20tables/Basic%20player%20Split%20table.png) 
