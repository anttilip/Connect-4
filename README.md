# Connect-4

This project is a python implementation a popular of  board game "Connect four", containing an AI opponent. I'm using a heuristic Negamax algorithm, which is a variant of a Minimax algorithm. Negamax can be used due to zero-sum property of Connect-4. The algorithm calculates the best moves in a game tree and chooses best strategy to a chosen depth. 


## Evaluation
The evaluation function uses all pre-calculated 4 length arrays which can lead to a victory. If one of those arrays contain both players' pieces, that array can not lead to a victory and is thus skipped. Otherwise the array is rated based on how many pieces the player has in it. The players score for each game state is just a sum of all array ratings.

## Negamax
Since Connect-4 has around 4*10^12 different game states, evaluating all of the states is not an option so heuristic algorithm is needed. Negamax searches the best move by evaluating every possible game state that can happen within a six moves. With this depth the AI is decent and unbeatable with my skills. However, negamax could have tremendous speed improvements if I have time to implement alpha-beta pruning, which greatly reduces the amount of game states to be searched.
