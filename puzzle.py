from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(

    # Either A is a knight or a knave, can't be both
    Biconditional(AKnight, Not(AKnave)),

    # If A is a knight, then what he says is true
    # If what A says is true, then he is a knight
    Biconditional(AKnight, And(AKnight, AKnave))

)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    
    # A is either a knight or a knave, but not both
    Biconditional(AKnight, Not(AKnave)),
    
    # B is either a knight or a knave
    Biconditional(BKnight, Not(BKnave)),

    # A says both are knaves
    # If a is a knight then what he says is true
    # And vice versa
    Biconditional(AKnight, And(AKnave, BKnave))

)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    
    # A is either a knight or a knave but not both
    Biconditional(AKnight, Not(AKnave)),

    # B is either a knight or a knave but not both
    Biconditional(BKnight, Not(BKnave)),

    # A says A and B are the same
    # If A is a knight, then it is true that
    # A is a knight and B is a knight
    # Or A is a knave and B is a knave
    Biconditional(AKnight, Or(And(AKnight, BKnight), And(AKnave, BKnave))),

    # B says A and B are different
    # Same logic
    Biconditional(BKnight, Or(And(AKnight, BKnave), And(AKnave, BKnight)))

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    
    # A is either a knight or a knave but not both
    Biconditional(AKnight, Not(AKnave)),

    # B is either a knight or a knave but not both
    Biconditional(BKnight, Not(BKnave)),

    # C is either a knight or a knave but not both
    Biconditional(CKnight, Not(CKnave)),

    # A says either AKnight or Aknave but not both
    Biconditional(AKnight, And(Or(AKnight, AKnave), Not(And(AKnight, AKnave)))),

    # B says "A said AKnave"
    Biconditional(BKnight, Biconditional(AKnight, AKnave)),

    # B says CKnave
    Biconditional(BKnight, CKnave),

    # C says AKnight
    Biconditional(CKnight, AKnight)

)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
