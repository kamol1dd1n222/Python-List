words = ["kitob", "dastur", "AI", "hello", "python"]
print(words)
kattalar = list()
for i in range(len(words)):
    if len(words[i]) > 5:
        kattalar.append(words[i])
print(kattalar)