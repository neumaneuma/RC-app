# Ultimate TicTacToe

Ultimate TicTacToe is like regular TicTacToe except for two main differences:

1. There is 1 big board and 9 mini boards. To claim a space on the big board you must win the corresponding mini board.
2. The space that your opponent claims on any mini board determines which space on the big board you have to play in next.

For example, if player one claims the mini board space #2 in big board space #0...

```
 | |o |  | |  |  | | 
----- | ----- | -----
 | |  |  | |  |  | | 
----- | ----- | -----
 | |  |  | |  |  | | 
      |       |      
------|-------|------
      |       |      
 | |  |  | |  |  | | 
----- | ----- | -----
 | |  |  | |  |  | | 
----- | ----- | -----
 | |  |  | |  |  | | 
      |       |      
------|-------|------
      |       |      
 | |  |  | |  |  | | 
----- | ----- | -----
 | |  |  | |  |  | | 
----- | ----- | -----
 | |  |  | |  |  | | 
      |       |      
```

... then player two will have to play somewhere in big board space #2 (in this example player two chose mini board space #8).

```
 | |o |  | |  |  | | 
----- | ----- | -----
 | |  |  | |  |  | | 
----- | ----- | -----
 | |  |  | |  |  | |x
      |       |      
------|-------|------
      |       |      
 | |  |  | |  |  | | 
----- | ----- | -----
 | |  |  | |  |  | | 
----- | ----- | -----
 | |  |  | |  |  | | 
      |       |      
------|-------|------
      |       |      
 | |  |  | |  |  | | 
----- | ----- | -----
 | |  |  | |  |  | | 
----- | ----- | -----
 | |  |  | |  |  | | 
      |       |      
```