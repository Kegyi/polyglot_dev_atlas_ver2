acts=[(1,4),(3,5),(0,6),(5,7),(8,9),(5,9)]
acts.sort(key=lambda x:x[1])
res=[]; last=-1
for s,e in acts:
    if s>last: res.append((s,e)); last=e
print('Selected',res)
