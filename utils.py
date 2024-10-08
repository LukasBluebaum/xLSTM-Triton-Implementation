import torch


def check(*inputs, name='A', atol=1e-2, rtol=1e-2):
    for i, (a, b) in enumerate(zip(inputs[::2], inputs[1::2])):
        if isinstance(b, list):
            b = torch.tensor(b)
        c = torch.allclose(a.cpu(), b.cpu(), atol=atol, rtol=rtol)
        c1 = torch.isclose(a.cpu(), b.cpu(), atol=atol, rtol=rtol)
        if not c:
            print(name)
            print(f"{i}\n{a}\n{b}\n{c1}\nNon-Matching Values A:\n{a[c1 == False]}\n"
                  f"Non-Matching Values B:\n{b[c1 == False]}\n Percentage non-matching: "
                  f"{format(torch.sum(c1 == False) / torch.numel(a), '.10f')}")
            return
    print(f"{name} -- EQUAL")
