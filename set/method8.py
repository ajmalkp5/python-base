order1={"cb","tika","fishfry","friedrice","vb","gheeroast"}
order2={"cb","friedrice","nan","upuma","vegmeals","idly"}

# union_order=order1.union(order2)
# intersectiion_order=order1.intersection(order2)
# new_order=union_order.difference(intersectiion_order)

new_order=order1.symmetric_difference(order2) #symmetricdiffernce=2ilum ullaath ozich baakki ullath
print(new_order)