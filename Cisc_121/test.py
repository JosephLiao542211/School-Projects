def remove(string):
    if len(string)<=2:
        return("" if list(string)[0] == list(string)[1] else string)
    else:

        return (("".join([ remove(string[i:i + 2]) for i in range(0, len(string), 2) ]) ) if len(string)//2==0 else ("".join([ remove(string[i:i + 2]) for i in range(0, len(string)-1, 2) ]) )+string[-1])

