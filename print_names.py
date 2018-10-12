import os

for file in os.listdir("./"):
    if file.endswith(".txt"):
        name = os.path.join(file)
        name = os.path.basename(name)
        os.path.splitext(name)[0]
        print(name)
