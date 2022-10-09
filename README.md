# An Automated Sports Betting/Trading Bot by Duncan Park
#### Contact: dpark6@nd.edu




### Overall Goal: Create a bot in python that, using data scraped from sports betting website, calculates implied odds and seeks arbitrage, employing this information to place paper bets[^1] and tracks performance of a portfolio.


- [x] Target 1: Be able to display all available odds for any event on sports betting site[^2] and calculate implied odds for these odds.


- [ ] Target 2: Be able to place theoritical wagers manually and keep track of these bets' performances in a portfolio.


- [ ] Target 3: Implement an automated bot that calculates and seeks arbitrage in mispricing of bets. Focus on simple types of bets in which only one outcome can win, as opposed to complex prop bets.


- [ ] End Target: Bot succesfully places bets when finding arbitrage, with stake of wager depending on size of arbitrage. Will have to see if arbitrage actually occurs at all on website from which I am getting odds from, so may result in betting on bets with the least amount of book edge.


- [ ] Bonus Target: Using machine learning, create model for one specific type of bet for a specific sport. Find a way to implement this model in trading bot, in which the bot finds which bets have low house edge and the model predicts an outcome significant different that the implied odds do.



### Current Progress:
- In initial stages, simply planning out organization of scripts and how to best utilize different data structures.



[^1]: I use "paper bets", meaning simulated bets with no monetary value. Coined from paper trading traditional equities. Cannot wager money for legal reasons. 

[^2]: Using Bovada for odds, as it does not require an account to view odds and make json requests.
