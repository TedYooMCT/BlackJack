## Player Types
In this Blackjack project, I have implemented different player types, each with its unique strategy for making decisions in the game.   
These player types offer a range of strategies and approaches to playing Blackjack, from random choices to highly optimized decision-making based on mathematical probabilities and reinforcement learning techniques. You can choose to play as any of these players or pit them against each other to see how their strategies compare.   
Here are the definitions of each player type:

### 1. Random Player
The Random Player is a simple player that makes decisions completely at random. It doesn't consider the current state of the game or any strategy.  

### 2. Human Player
The Human Player allows you to control the game by entering your decisions through prompts. You play as the human participant, making choices based on your understanding of the game's rules.  

### 3. Basic Strategy Player
The Basic Strategy Player follows the predefined basic strategy for Blackjack. This strategy is based on mathematical probabilities and provides recommendations for each possible player hand against the dealer's card. The Basic Strategy Player adheres strictly to this strategy when making decisions.   
[read more](https://wizardofodds.com/games/blackjack/strategy/4-decks/)   

### 4. Expectancy Player
The Expectancy Player uses a table that calculates the expected value for each possible action based on the current state of the game. It chooses the action with the highest expected value. This player takes into account the probabilities of different outcomes and selects the action that maximizes expected gains.
it's not known strategy - I made it myself.   
[read more](https://en.wikipedia.org/wiki/Expected_value) about expectancy   

### 5. Q-learning (One-Step) Player
The Q-learning (One-Step) Player employs the Q-learning reinforcement learning algorithm. this player updates the Q-values for the entire play as one step without decay. It learns to make optimal decisions by adjusting its Q-values based on the outcomes of complete plays.   

### 6. Q-learning (Decay-Step) Player
The Decay Step Q-Learning Player utilizes the Q-learning algorithm with a unique twist - the Q-values are updated over discrete steps, or "decays," rather than continuously throughout each play. 
