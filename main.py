iceCream = 100
queue = ["A","C","O","A"]
dic ={"A": 5, "C": 7, "O": 2}

while dic[queue[0]]<=iceCream:
  first = queue.pop(0)
  iceCream-= dic[first]
  queue.append(first)
  print(queue)
  print(iceCream)

def flatten(S):
    if S == []:
        return S
    if isinstance(S[0], list):
        return flatten(S[0]) + flatten(S[1:])
    return S[:1] + flatten(S[1:])
s=[[1,2],[3,4],[1,2,3,[9,6,7]]]
print(flatten(s))
  

