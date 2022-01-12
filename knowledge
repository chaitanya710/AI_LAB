def tell(kb,rule):
    kb.append(rule)
combinations=[(True,True, True),(True,True,False),
              (True,False,True),(True,False, False),
              (False,True, True),(False,True, False),
              (False,False,True),(False,False,False)]
def ask(kb,q):
    for c in combinations:
        s = all(rule(c) for rule in kb)
        f = q(c)
        print(s, f)
        if s != f and s != False:
            return 'Does not entail'
    return 'Entails'
# Test 1
# Knowledge base array
kb = []

## Rule 1
r1 = lambda x: x[0] or x[1] and (x[0] and x[1])

## Tell KB Rule 1
tell(kb, r1)

## Tell Rule 2
r2 = lambda x: (x[0] or x[1]) and x[2]
tell(kb, r2)

## Query
q = lambda x: x[0] and x[1] and (x[0] or x[1])

## Ask KB Query
ask(kb, q)
True True
False True
True False
'Does not entail'
print("Use variables: p,q,r, operators: ^:and ,v:or, ~:not")
Use variables: p,q,r, operators: ^:and ,v:or, ~:not
print("Tell the knowledge base")
n = int(input("Enter the no of expressions: "))
for i in range(n):
  expr = input("Enter the expression: ")
  expr = expr.replace("p","x[0]")
  expr = expr.replace("q", "x[1]")
  expr = expr.replace("r", "x[2]")
  expr = expr.replace("v", " or ")
  expr = expr.replace("^", " and ")
  expr = expr.replace("~", " not ")
  expr = "lambda x: " + expr 
  tell(kb, eval(expr)) 
Tell the knowledge base
Enter the no of expressions: 3
Enter the expression: (p^q)vr
Enter the expression: ~qv~r
Enter the expression: ~p^~q
print("Querying the Knowledge base")
expr = input("Enter you query: ")
expr = expr.replace("p","x[0]")
expr = expr.replace("q", "x[1]")
expr = expr.replace("r", "x[2]")
expr = expr.replace("v", " or ")
expr = expr.replace("^", " and ")
expr = expr.replace("~", " not ")
expr = "lambda x: " + expr 
ask(kb, eval(expr)) 
Querying the Knowledge base
Enter you query: p^~q
False False
False False
False True
False True
False False
False False
True False
'Does not entail'
