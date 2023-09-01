# Q-learning
### Learning Objective:
The primary goal of this player is to maximize its expected cumulative reward over time by learning the optimal policy for Blackjack.

### Q-Value Updates:
The key distinction between these players lies in how they update their Q-values.
While the "One-Step Changes" player updates Q-values at the end of an hand for each action equally,
the "Decay Step" player updates Q-values periodically, considering rewards with decay rate over a series of actions.

### Learning Rate:
Both players use a learning rate of 0.1,
which determines the extent to which new information influences their decisions.
A lower learning rate typically leads to more stable learning but slower adaptation.

### Decay Rate:
The "Decay Step" player uses a decay rate of 0.9 for its Q-value updates.
This rate controls how much past experiences affect the current Q-values,
allowing the player to strike a balance between recent and historical knowledge.

# Experimentation
Under the compare folder you can find my training process, as you can see I tried to train my models and exmaine the result for each 10X rounds.

## Important Lesson:
The most significant lesson learned from experimenting with these trained players is that, despite their efforts to learn and adapt, neither method comes close to the effectiveness of the basic strategy in Blackjack. The basic strategy, which is based on rigorous mathematical analysis, remains the most reliable and profitable approach for playing Blackjack. It serves as a reminder that while reinforcement learning methods can be powerful, they may not always outperform well-established strategies in certain domains.

## Learning curve:
As showen in the following chart we can see that the One-Step Q-learning algorithem has learned his strategy from the very first 1000 rounds train.  
Also we can see that the Decay Step method has started low (almost like the random strategy) and trained until the training wasn't effective anymore (around 1 million rounds).
![Comparison graph](https://github.com/Bar-A-94/BlackJack/blob/master/compare/compare%201000%20games%20for%20each%20training%20session.png?raw=true)

## Compare between decision tables:
