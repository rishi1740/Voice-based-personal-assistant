def processing(data):
    text = data
    text=text.lower()#converting to lower case
    tokens = text.split()
    command=[]
    noise=["a","the","an","and","or","if","is","for","are","on","in","it"]#useless command
    for i in tokens:
        if i not in noise :
            command.append(i)
    data= " ".join(command)
    return data
