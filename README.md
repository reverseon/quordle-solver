# Quordle Solver
oleh Thirafi Najwan Kurniatama - 13520157
## Prerequisites
* program ini dicompile dan dites menggunakan Python versi 3.9.7

## Cara Menggunakan
Jalankan `python interactive.py` di direktori untuk memulai program.

## Contoh Expected Input dan Output

Quordle:

![Quordle](https://i.ibb.co/VSWkfxY/quordless.png)

Program:

```
Quordle Solver
--------------
Instruction:
Use 0 for grey response, 1 for yellow response, and 2 for green response separated with a comma. If the box is already guessed, just click enter.
Ex: GREEN GREEN GREY YELLOW GREY
In: 2,2,0,1,0
Turn 1
BEST GUESS: RAISE
Enter response for Box 1: 1,0,0,1,2
Enter response for Box 2: 0,0,0,0,0
Enter response for Box 3: 0,0,0,0,0
Enter response for Box 4: 1,0,2,0,2
Turn 2
BEST GUESS: PHONY
Enter response for Box 1: 1,0,2,0,0
Enter response for Box 2: 0,0,1,0,0
Enter response for Box 3: 0,0,0,0,2
Enter response for Box 4: 0,0,0,0,0
Box 1 answer is SPORE
Turn 3
BEST GUESS: GUMBO
Enter response for Box 1: 0,0,0,0,1
Enter response for Box 2: 0,1,1,0,1
Enter response for Box 3: 0,2,0,1,0
Enter response for Box 4: 0,0,0,0,0
Box 1 answer is SPORE
Turn 4
BEST GUESS: TRIDE
Enter response for Box 1: 0,1,0,0,2
Enter response for Box 2: 1,0,0,0,0
Enter response for Box 3: 0,0,0,0,0
Enter response for Box 4: 1,2,2,0,2
Box 1 answer is SPORE
Box 2 answer is MOULT
Box 4 answer is WRITE
Turn 5
BEST GUESS: MOULT
Enter response for Box 1: 0,1,0,0,0
Enter response for Box 2:
Enter response for Box 3: 0,0,1,1,0
Enter response for Box 4: 0,0,0,0,1
Box 1 answer is SPORE
Box 2 answer is MOULT
Box 3 answer is BULKY
Box 4 answer is WRITE
Turn 6
BEST GUESS: SPORE
Enter response for Box 1:
Enter response for Box 2:
Enter response for Box 3: 0,0,0,0,0
Enter response for Box 4: 0,0,0,1,2
Box 1 answer is SPORE
Box 2 answer is MOULT
Box 3 answer is BULKY
Box 4 answer is WRITE
Turn 7
BEST GUESS: BULKY
Enter response for Box 1:
Enter response for Box 2:
Enter response for Box 3:
Enter response for Box 4: 0,0,0,0,0
Box 1 answer is SPORE
Box 2 answer is MOULT
Box 3 answer is BULKY
Box 4 answer is WRITE
Turn 8
BEST GUESS: WRITE
Enter response for Box 1:
Enter response for Box 2:
Enter response for Box 3:
Enter response for Box 4:
Box 1 answer is SPORE
Box 2 answer is MOULT
Box 3 answer is BULKY
Box 4 answer is WRITE
All boxes are answered, exiting...
```
