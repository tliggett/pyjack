# pyjack21

**pyjack21** is a blackjack simulator aimed for use in jupyter notebooks.

## Usage

Simulations are run through the BlackJackTable class.

```
from pyjack21 import BlackJackTable
```

To run a simulation, use the code below:

```
table = BlackJackTable(hands=2000, decks=6, player_count=player_count)
table.run()
blackjack_data = table.df
```

**Optional Parameters:**
+ *hands:* the number of hands to be played
+ *decks:* the number of decks in a shoe of cards
+ *player_count:* the number of players at the table

### Using the data

After simulation, a BlackJackTable holds a pandas dataframe with the results of the game. These results can be accessed using BlackJackTable.df:

```
blackjack_data = table.df
```

A csv format is coming soon. For now, write the csv using pandas.DataFrame.to_csv:

```
blackjack_data.to_csv('results.csv')
```
