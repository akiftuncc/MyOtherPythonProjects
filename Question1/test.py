from Question1 import nqueens

nqueens1 = nqueens(int(input("Enter a N value: ")))
nqueens1.set_state()
nqueens1.count_attacking_pairs()
print(nqueens1)
a = input("to end program press a key")