import torch

A= torch.tensor([[[
    [1,2],
    [5,6],
]]],dtype=float)
B,C =A.shape

norm = A.reshape(B,C)
norm = torch.linalg.norm(norm,ord=2,dim=-1,keepdim = True)
norm = norm.repeat(1,C)
B = A/norm
print(A.shape)